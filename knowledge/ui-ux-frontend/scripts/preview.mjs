import fs from 'node:fs/promises';
import path from 'node:path';
import http from 'node:http';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';

// Static preview helper. Never imports or executes product code.
const [command, ...args] = process.argv.slice(2);
const options = {};
for (let i = 0; i < args.length; i += 2) {
  if (!['--root', '--product-root', '--port'].includes(args[i]) || !args[i + 1]) {
    throw new Error('Usage: preview.mjs init|serve|fingerprint --root PATH --product-root PATH [--port 5317]');
  }
  options[args[i].slice(2)] = args[i + 1];
}
if (!['init', 'serve', 'fingerprint'].includes(command) || !options.root || !options['product-root']) {
  throw new Error('Require init|serve|fingerprint, --root and --product-root. See PREVIEW_ARCHITECTURE.md.');
}
const inside = (parent, child) => {
  const rel = path.relative(parent, child);
  return rel === '' || (!rel.startsWith(`..${path.sep}`) && rel !== '..' && !path.isAbsolute(rel));
};
const product = await fs.realpath(options['product-root']);
const requested = path.resolve(options.root);
// Resolve existing ancestors too, so junctions cannot hide a nested destination.
async function resolveDestination(target) {
  try { return await fs.realpath(target); }
  catch (error) {
    if (error.code !== 'ENOENT') throw error;
    const parent = path.dirname(target);
    if (parent === target) throw error;
    return path.join(await resolveDestination(parent), path.basename(target));
  }
}
const root = await resolveDestination(requested);
if (inside(product, root) || inside(root, product)) throw new Error('Preview and product roots must not overlap.');

if (command === 'init') {
  await fs.mkdir(path.dirname(root), { recursive: true });
  await fs.mkdir(root); // Refuse overwriting an existing version.
  const demo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../assets/preview-demo.html');
  await fs.copyFile(demo, path.join(root, 'index.html'));
  console.log(`Created synthetic demo: ${root}`);
} else if (command === 'fingerprint') {
  const files = [];
  async function scan(dir) {
    for (const entry of (await fs.readdir(dir, { withFileTypes: true })).sort((a, b) => a.name.localeCompare(b.name))) {
      const target = path.join(dir, entry.name);
      const resolved = await fs.realpath(target);
      if (entry.isSymbolicLink() || !inside(root, resolved)) throw new Error('No symlinks or external files in frozen preview.');
      if (entry.isDirectory()) await scan(target);
      else if (entry.isFile()) files.push({ path: path.relative(root, target).split(path.sep).join('/'), sha256: createHash('sha256').update(await fs.readFile(target)).digest('hex') });
    }
  }
  await scan(root);
  console.log(JSON.stringify({ algorithm: 'sha256', files }, null, 2));
} else {
  if (!(await fs.stat(root)).isDirectory()) throw new Error('Preview root must be a directory.');
  const port = Number(options.port || 5317);
  if (!Number.isInteger(port) || port < 1024 || port > 65535) throw new Error('Invalid local port.');
  const mime = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml', '.woff2': 'font/woff2' };
  const server = http.createServer(async (req, res) => {
    res.setHeader('Content-Security-Policy', "default-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self'; connect-src 'none'; img-src 'self' data:; font-src 'self'; form-action 'none'; frame-src 'none'; object-src 'none'; base-uri 'none'");
    res.setHeader('Cache-Control', 'no-store');
    res.setHeader('X-Content-Type-Options', 'nosniff');
    if (!['GET', 'HEAD'].includes(req.method)) { res.writeHead(405); res.end(); return; }
    try {
      const pathname = decodeURIComponent(new URL(req.url, 'http://127.0.0.1').pathname);
      let target = path.resolve(root, `.${pathname}`);
      if (!inside(root, target)) throw new Error('Outside preview');
      target = await fs.realpath(target);
      if (!inside(root, target)) throw new Error('Outside preview');
      if ((await fs.stat(target)).isDirectory()) target = await fs.realpath(path.join(target, 'index.html'));
      if (!inside(root, target)) throw new Error('Outside preview');
      const data = await fs.readFile(target);
      res.writeHead(200, { 'Content-Type': mime[path.extname(target)] || 'application/octet-stream' });
      res.end(req.method === 'HEAD' ? undefined : data);
    } catch { res.writeHead(404); res.end(); }
  });
  server.on('error', error => { console.error(error.message); process.exitCode = 1; });
  server.listen(port, '127.0.0.1', () => console.log(`Preview: http://127.0.0.1:${port} (Ctrl+C to stop)`));
  for (const signal of ['SIGINT', 'SIGTERM']) process.on(signal, () => server.close());
}
