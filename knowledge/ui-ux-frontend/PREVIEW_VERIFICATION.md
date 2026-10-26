# Verificación de previews — 26 de octubre de 2026

## Fuente y alcance

Continuación aislada de PR #7: base `5f1cf4bfe7da00a748d877ad7d96dabb2001e91d`, rama `feat/visual-approval-20261026`. PR #7 y #3 observados abiertos y draft. PR #3 HEAD `0ebfe4b2a43aeeae91ba539302425b740e7397fd`: router compatible que delega en la especialidad; no requiere duplicar ni modificar reglas. Main observado `8dc1fd5bfa17f8f85d69ae644ee558cf7fa18787`; no se modificó. Brain OS core permanece en 1.4.1, módulo propuesto 0.5.0.

Integración PAZO inspeccionada solo mediante lecturas de AGENTS y su gate UI: referencia al Brain OS y decisiones visuales específicas que deben permanecer en el producto. No se infiere que los PR estén instalados o fusionados. Ninguna pantalla real se construyó ni cambió por esta prueba.

## Herramientas y resultados reales

- Node `24.21.0` y Chrome local reutilizados; no se descargó otro navegador.
- Microsoft `@playwright/cli` `0.1.22`, instalado con versión fija en `~/.local/share/design-preview-tools`, tres paquetes instalados; sin paquetes, skills ni hooks en PAZO. Versionado de instalación conservado en package-lock local.
- Token Savior disponible con perfil optimized existente. No se cambió WORKSPACE_ROOTS (apunta al checkout de pilotos); no se usó su índice para consultar el nuevo checkout ni se activaron memoria, reescritura o benchmarks. Navegación documental acotada por archivos.
- Utilidad Node incluida: `init`, `serve` y `fingerprint` ejecutados realmente con carpeta de demo externa al producto. Servidor en `127.0.0.1:5317`. Sesión CLI `visual-approval-demo` y servidor propio cerrados al terminar; archivos preservados.
- Capturas reales a **1440×900** y **390×844** (esta última full-page, altura de documento 1063). Inspeccionadas visualmente por el agente, **no aprobadas por el PO**. Mobile: `innerWidth=390`, `scrollWidth=390`; no desbordamiento horizontal observado en esa demo.
- Tab enfocó «Ver alcance de la prueba». Click local cambió a `#detalle` y `scrollY=219`; atrás devolvió `/`. Red inspeccionada con `requests --static`: único GET `http://127.0.0.1:5317/`, HTTP200.
- Guard de raíces solapadas rechazó `init` dentro del producto antes de crear la carpeta. Segundo `init` sobre versión existente rechazó EEXIST. GET/HEAD200, POST405. No se afirma una auditoría de seguridad exhaustiva del servidor.
- `node --check` y revisión de diff ejecutados. Comparación de `git status --porcelain` antes/después en PAZO: idéntica, conservando cambios previos. No se ejecutó código PAZO ni servicios reales; no se usaron secretos, backend, pagos ni despliegues.

Demo congelada: SHA-256 de `index.html` = `842432e9809740fef78baed7fc751f8fb9222ebf4a7a66d90d74513519b7e247`, igual al asset [preview-demo.html](assets/preview-demo.html).

Capturas: [escritorio](evidence/preview-demo-desktop.png), [móvil](evidence/preview-demo-mobile.png).

## Comprobación documental y autorizaciones

Referencias relativas comprobadas en el módulo y README raíz, con rutas existentes; sin reescribir los módulos de normas. Revisión de casos del contrato, **no evaluación conductual de un agente**:

| Caso | Resultado definido por el protocolo |
| --- | --- |
| «Elijo B» | Refinar en aislamiento; no transferir al producto |
| «Apruebo B v2» | Baseline visual aprobado; implementación pendiente si falta permiso |
| «Apruebo B v2 y autorizo implementarla en X» | Registrar ambas decisiones; ejecutar alcance sin pedir de nuevo |
| Cambio significativo posterior | Nueva versión y revisión del delta; conservar aprobación de partes intactas |
| Ajuste pequeño preciso ya autorizado | Registro/preview proporcionados; sin tres alternativas ni ampliación arbitraria |
| Build verde o silencio del PO | Sin aprobación inferida |
| Permiso para implementar | No implica permiso de publicación |

## Limitaciones

- `quick_validate.py` de skill-creator fue ejecutado con Python UTF-8 y PyYAML del entorno existente de Token Savior. Rechaza `version`, `reviewed_at` y `status` del frontmatter. Mismo resultado comprobado en baseline v0.4.0 y en esta versión; se conserva la convención existente de Brain OS. YAML y referencias se validan por separado. No afirmar PASS de ese validador genérico.
- La demo comprueba infraestructura estática. App temporal compleja, transferencia a producto y comparación con diseño aprobado: **NOT_TESTED**, porque no se solicitó ni aprobó una pantalla de producto. El procedimiento está documentado, no demostrado con PAZO.
- Las autorizaciones son instrucciones y evidencia durable; no existe un motor automático que impida al agente escribir código ni que certifique identidad del PO. La revisión humana sigue siendo necesaria.
- PR de revisión sin merge, instalación/activación global no realizada; otros chats deben cargar la referencia de esta rama. Loopback accesible únicamente desde esta computadora. Sin conformidad WCAG global, batería comparativa del modelo, benchmarks ni ahorro de tokens cuantificado.

## Archivos

Creados: protocolo, arquitectura, este informe, [registro de aprobación](templates/VISUAL_APPROVAL_RECORD.md), [servidor/helper](scripts/preview.mjs), asset demo y dos capturas.

Integrados mediante cambios localizados: SKILL, DESIGN_REASONING, CREATIVE_EXPLORATION, CHANGE_INTEGRITY, QUALITY_GATES, DESIGN_MEMORY, README del módulo, MAINTENANCE y README raíz. SKILL raíz, PR #3, main y PAZO sin cambios de esta tarea.
