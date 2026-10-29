// Real browser capture of PAZO's actual interactive Demo mode (English).
// App hosted LOCALLY. Supabase requests are synthetic-blocked. No production writes.
import { spawn } from 'node:child_process'
import { mkdirSync } from 'node:fs'
import { resolve } from 'node:path'
import assert from 'node:assert/strict'
import { createRequire } from 'node:module'

const appDir=resolve(process.env.PAZO_APP_DIR || './pazo-src')
const outDir=resolve(process.env.PAZO_VIDEO_OUT || './video-renders/delivery/real_demo')
mkdirSync(outDir,{recursive:true})
const require=createRequire(resolve(appDir,'package.json'))
const {chromium}=require('playwright')
const origin='http://127.0.0.1:5488'
const server=spawn(process.execPath,[resolve(appDir,'node_modules/vite/bin/vite.js'),'--host','127.0.0.1','--port','5488','--strictPort'],{
  cwd:appDir,
  env:{...process.env,VITE_SUPABASE_URL:'https://mrybvqdebbgcayuvgkkr.supabase.co',
    VITE_SUPABASE_PUBLISHABLE_KEY:'sb_publishable_synthetic_guest_e2e_only',VITE_MAPBOX_ACCESS_TOKEN:''},
  stdio:['ignore','pipe','pipe']
})
let serverOutput=''
server.stderr.on('data',v=>{serverOutput+=v.toString().slice(-1800)})
server.stdout.on('data',v=>{serverOutput+=v.toString().slice(-1800)})
const pause=(ms)=>new Promise(done=>setTimeout(done,ms))
let browser
try {
  let ready=false
  for(let i=0;i<85;i++){
    if(server.exitCode!==null) throw Error('Vite died '+serverOutput.slice(-700))
    try { const r=await fetch(origin);if(r.ok){ready=true;break} } catch {}
    await pause(350)
  }
  assert(ready,'Vite startup timeout '+serverOutput.slice(-650))
  browser=await chromium.launch({headless:true,args:['--no-sandbox']})
  const context=await browser.newContext({
    viewport:{width:390,height:844},deviceScaleFactor:1,locale:'en-US',
    reducedMotion:'no-preference',isMobile:true,hasTouch:true,serviceWorkers:'block',
    recordVideo:{dir:outDir,size:{width:390,height:844}},
  })
  const page=await context.newPage()
  const blocked=[]
  const errors=[]
  page.on('pageerror',e=>errors.push(e.message))
  await page.route('**/*',async route=>{
    const request=route.request()
    const u=new URL(request.url())
    if(u.origin===origin) return route.continue()
    if(u.hostname==='mrybvqdebbgcayuvgkkr.supabase.co'){
      if(u.pathname.endsWith('/rpc/pazo_public_maintenance_status'))
        return route.fulfill({status:200,contentType:'application/json',body:JSON.stringify({
          enabled:false,message_es:'Solo demostración local',message_en:'Local demonstration only',updated_at:'2026-10-29T00:00:00Z'
        })})
      blocked.push(request.method()+' '+u.pathname)
      return route.fulfill({status:403,contentType:'application/json',body:'{"code":"LOCAL_DEMO_DENIED"}'})
    }
    if(u.hostname==='images.unsplash.com' && request.resourceType()==='image')return route.continue()
    return route.abort()
  })
  // Editorial click feedback only; never modify PAZO's own controls or workflow.
  await page.addInitScript(()=>{
    document.addEventListener('pointerdown',event=>{
      const el=document.createElement('span')
      el.setAttribute('data-pazo-video-click','true')
      el.style.cssText=[
        'position:fixed','pointer-events:none','z-index:2147483647',
        'width:62px','height:62px','border:3px solid #D5E74C',
        'background:rgba(213,231,76,.18)','border-radius:50%',
        'transform:translate(-50%,-50%)',
        'transition:opacity 450ms ease-out,scale 450ms ease-out',
        'opacity:1'
      ].join(';')
      el.style.left=event.clientX+'px'
      el.style.top=event.clientY+'px'
      document.body.appendChild(el)
      requestAnimationFrame(()=>{el.style.opacity='0';el.style.scale='1.45'})
      setTimeout(()=>el.remove(),550)
    },true)
  })
  await page.goto(origin,{waitUntil:'domcontentloaded',timeout:35000})
  const demo=page.getByRole('button',{name:'Demo',exact:true})
  await demo.waitFor({timeout:20000})
  await page.screenshot({path:resolve(outDir,'evidence_01_welcome.png')})
  await pause(1200)
  await demo.click()
  await page.getByText('Demo mode.',{exact:true}).waitFor({timeout:15000})
  await page.getByText(/Luna found her new|Luna encontró su nuevo/).first().waitFor({timeout:12000}).catch(()=>{})
  await pause(1900)
  await page.screenshot({path:resolve(outDir,'evidence_02_feed.png')})
  // A genuine in-memory demo like; the demo never writes a real event/DB row.
  const like=page.getByRole('button',{name:/Like:\s*42|Me gusta:\s*42/}).first()
  if(await like.count()){
    await like.click()
    await pause(850)
  }else{
    console.log('LIKE_LABEL_ABSENT — showing other valid interaction')
  }
  const nav=page.getByRole('navigation',{name:/PAZO|Navegación/})
  await nav.getByRole('button',{name:/Communities|Comunidades/}).click()
  await page.getByRole('heading',{name:/Discover communities|Descubre comunidades/}).waitFor({timeout:12000})
  await pause(1500)
  await page.screenshot({path:resolve(outDir,'evidence_03_communities.png')})
  const firstCommunity=page.getByText('Gatos de LA').first()
  await firstCommunity.click()
  await pause(1300)
  await page.getByRole('button',{name:/Search PAZO|Buscar en PAZO/}).first().click()
  await page.getByRole('heading',{name:/Explore PAZO|Explora PAZO/}).waitFor({timeout:12000})
  await pause(950)
  const search=page.getByRole('searchbox',{name:/Search examples|Buscar ejemplos/})
  await search.fill('Luna',{timeout:10000})
  await pause(1500)
  await page.screenshot({path:resolve(outDir,'evidence_04_search.png')})
  const back=page.getByRole('button',{name:/Back|Volver/}).first()
  if(await back.count())await back.click()
  await pause(450)
  // Video capture is finished; no account creation; no login or hosted writes.
  const saved=page.video()
  await context.close()
  await saved.saveAs(resolve(outDir,'browser_real_demo.webm'))
  assert.deepEqual(blocked,[],'Unexpected attempted hosted endpoint(s)')
  assert.deepEqual(errors,[],'Unexpected browser runtime error(s)')
  console.log('REAL_DEMO_CAPTURE_PASS English / actual DOM clicks / local synthetic data / zero hosted writes')
}catch(e){console.error('CAPTURE_FAILED',String(e),serverOutput.slice(-900));throw e}
finally{
  await browser?.close()
  server.kill('SIGTERM')
}
