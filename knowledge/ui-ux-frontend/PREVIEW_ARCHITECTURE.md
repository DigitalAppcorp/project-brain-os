# Arquitectura de previews independientes

Aplica [VISUAL_APPROVAL_PROTOCOL.md](VISUAL_APPROVAL_PROTOCOL.md); aquí vive la mecánica, no otra política de aprobación. No instala nada en el producto ni necesita despliegues.

## Flujo reutilizable

1. Leer diseño real, rama/SHA, componentes, fuentes, tokens e invariantes. Capturar original solo desde evidencia existente o runtime autorizado sin efectos secundarios. No ejecutar el frontend real si sus fallbacks conectan a producción.
2. Crear carpeta hermana externa al producto, con subcarpetas por tarea/versión. HTML/CSS estático para prototipos simples; para interacciones complejas, app temporal con dependencias propias y datos sintéticos, sin importar `.env`, sesiones, secretos ni SDKs conectados. Copiar únicamente recursos necesarios y permitidos; registrar su procedencia. No modificar imports ni dependencias del producto.
3. Explorar estructuras distintas cuando el problema lo requiera y seleccionar internamente según el protocolo; no exigir una votación del PO. El servidor incluido solo sirve archivos estáticos: no compila React ni prueba backend. Para una app temporal usar su servidor en loopback y comprobar por separado aislamiento y fallback de red. Una rama aislada de implementación autorizada puede ejecutar el runtime real con transporte interceptado, sin cambios en main ni conexiones de escritura alojadas.
4. Inspeccionar con herramientas disponibles, capturar runtime completo y **ver** las imágenes; publicar evidencia para transparencia. No confundir captura creada con captura vista. Añadir estados, contenido realista y límites de fidelidad; solo esperar decisión estética del PO en el carril que la requiera.
5. Criticar y corregir la dirección seleccionada, recapturar y congelar versión: ejecutar `fingerprint`, guardar salida junto con capturas y registro profesional/PO separado. No editar una versión congelada; generar la siguiente.
6. Solo con autorización de implementación vigente transferir el delta al producto en rama permitida. Adaptar a componentes reales sin copiar dependencias, mocks o datos de demo. Conservar funciones e invariantes.
7. Comparar preview aprobada y runtime implementado con mismo viewport, tema, idioma, contenido y estado; inspeccionar código y probar interacciones relevantes. Mostrar lado a lado y registrar diferencias con [CHANGE_INTEGRITY.md](CHANGE_INTEGRITY.md). Una diferencia de píxeles por fuentes/entorno no demuestra por sí sola un defecto; tampoco un diff vacío acredita funcionamiento.

## Utilidad estática incluida (Node, sin dependencias)

Desde el checkout de Brain OS, reemplazar rutas por carpetas absolutas del entorno:

```powershell
node knowledge/ui-ux-frontend/scripts/preview.mjs init --root C:/design-previews/demo-v1 --product-root C:/work/product
node knowledge/ui-ux-frontend/scripts/preview.mjs serve --root C:/design-previews/demo-v1 --product-root C:/work/product --port 5317
node knowledge/ui-ux-frontend/scripts/preview.mjs fingerprint --root C:/design-previews/demo-v1 --product-root C:/work/product
```

`init` exige destino nuevo y copia una demo sintética; no crea una pantalla del producto. `serve` escucha solo `127.0.0.1`, acepta GET/HEAD, rechaza solapamiento con la raíz real del producto y escapes por enlaces simbólicos. CSP limita conexiones externas en esta demo estática; no constituye sandbox del sistema ni sustituye inspección de scripts. No servir archivos privados; toda la carpeta de preview es visible para procesos locales. `fingerprint` imprime SHA-256 de los archivos de la versión; guardar capturas/registro fuera de la carpeta congelada para no cambiar su identidad.

Detener con Ctrl+C al acabar; preservar archivos/evidencia. No cerrar servidores ni sesiones de otros trabajos. Esta utilidad no genera una aprobación ni bloquea técnicamente escrituras futuras del agente.

## Inspección con Microsoft Playwright CLI

Fuente: [repositorio oficial y comandos](https://github.com/microsoft/playwright-cli). Detectar primero `playwright-cli --version`, `--help`, Node y navegadores disponibles. Reutilizar una instalación compatible. Si falta, instalar una versión verificada con `npm install --prefix <carpeta-del-agente> --save-exact @playwright/cli@<version>`; invocar su ejecutable absoluto. No instalar skills/hooks, dependencias ni paquetes en el producto automáticamente. Si falta navegador, instalar solo el requerido con el comando que indique `open --help`/`install-browser --help` de esa versión, o reutilizar Chrome/Edge disponible.

Ejemplo desde una carpeta de evidencia externa al producto (ajustar sintaxis mediante `--help` de la versión instalada):

```text
playwright-cli -s=visual-task open http://127.0.0.1:5317 --browser=chrome
playwright-cli -s=visual-task resize 1440 900
playwright-cli -s=visual-task snapshot
playwright-cli -s=visual-task screenshot --filename=desktop.png
playwright-cli -s=visual-task resize 390 844
playwright-cli -s=visual-task screenshot --filename=mobile.png
playwright-cli -s=visual-task eval "() => ({width: innerWidth, scroll: document.documentElement.scrollWidth, height: document.documentElement.scrollHeight})"
playwright-cli -s=visual-task press Tab
playwright-cli -s=visual-task press PageDown
playwright-cli -s=visual-task close
```

Después de un snapshot usar referencias actuales para `click`, `fill` y navegación; capturar estado inicial y resultados pertinentes, error/vacío/loading solo cuando existan en el alcance. Comprobar scroll real y ausencia de recortes, atrás, teclado/foco, mobile/desktop cuando corresponda. `eval` y `run-code` ejecutan código: mantenerlos acotados a lectura o interacción sintética local autorizada. No iniciar sesión, enviar formularios ni navegar rutas que muten producción, usuarios, pagos o bases de datos. Auditar red de la demo y no conectar servicios reales para simular fidelidad.

Preferir CLI con salidas breves y snapshots bajo demanda. Usar Playwright MCP únicamente si una capacidad requerida no es practicable mediante CLI, documentando motivo; no añadirlo solo por costumbre. Las sesiones CLI persisten entre comandos, cerrarlas al terminar sin `close-all` ni `kill-all`.

## Evidencia y límites

Conservar fuente/versión de la herramienta, comando, resultado, SHA de Brain OS/producto, URL loopback, viewports, imágenes, manifiesto de fuentes y red observada. La prueba mínima es arranque + captura de demo aislada y comprobación de que el producto no cambió. No requiere benchmarks, suites extensas ni certificación WCAG. Ejemplo de resultados reales de esta integración: [PREVIEW_VERIFICATION.md](PREVIEW_VERIFICATION.md).

La política es un contrato de instrucciones, no una plataforma de autorización automática. Un enlace loopback solo es accesible en la computadora local; para otro dispositivo entregar capturas o un prototipo mediante un canal expresamente autorizado. La integración de la habilidad en `main` no instala automáticamente la utilidad local en otros equipos o chats: cada agente debe cargar el SKILL y comprobar sus herramientas. `patterns/INTERFACE_QUALITY_GATE.md` ya funciona como router integrado, sin duplicar criterios.
