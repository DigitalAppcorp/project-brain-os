# Herramientas, capacidad comprobada y fuentes (2026-10-28)

**Principio:** gratis ≠ ilimitado, instalado ≠ apto, clip exportado ≠ publicidad de calidad. Confirmar versiones, planes, licencias y permisos en cada producción.

## Stack por prioridad

| Rol | Opción | Licencia/coste base | Qué permite | Estado que se debe registrar |
|---|---|---|---|---|
| Edición, subtítulos, mezcla y formatos | **FFmpeg** | Software libre, ejecutable local sin créditos de generación | Cortar, unir, escalar, transiciones, audio, filtros, render a MP4 | Verificar `ffmpeg -version`, `ffprobe`, codecs y un archivo decodificado; no garantiza nivel cinematográfico |
| Personajes, rig y animación 3D | **Blender** | Gratuito, código abierto | Modelos, rigs, animación, luces, cámara, render; Python para automatizar | Verificar instalación, rig autorizado, export de 3–5 s y revisión de actuación. **La sola documentación no valida 3D** |
| Escenas humanas/mascotas naturales | Cámara real de móvil | Sin nueva suscripción; requiere permiso, tiempo y recursos | Actuación real creíble | Grabar original, revisar exposición/audio, cesión y localización |
| Video generado | Servicio opcional (Runway u otros) | Condiciones y créditos variables; **no dependencia** | Video sintético desde imagen o texto | Verificar precio actual, términos, artefactos, derechos; no gastar sin aprobación |
| Imagen de apoyo | Imagen propia / herramienta de imagen ya autorizada | Dependiente de plan y términos | Storyboard, ilustración o still | No confundir imagen animada con video 3D/narrativo |
| Narración/sonido | Grabación original y/o librería autorizada | Coste variable | Voces y música | Comprobar licencia de explotación comercial y medios; nunca inferir por ser «gratis» |

La conexión con una app, generador o almacenamiento de terceros **requiere autorización** y puede generar costes o compartir datos. No exportar información privada del producto a servicios externos sin permiso.

## Fuentes primarias consultadas

- Blender free/open source y pipeline: https://www.blender.org/features/
- Blender Python API oficial: https://docs.blender.org/api/main/index.html
- FFmpeg: https://ffmpeg.org/documentation.html
- FFmpeg filters (loudnorm, drawtext, etc.): https://ffmpeg.org/ffmpeg-filters.html
- TikTok creative: https://ads.tiktok.com/resources/help/article/creative-best-practices
- FTC publicidad veraz: https://www.ftc.gov/business-guidance/advertising-marketing
- FTC recomendaciones/testimonios: https://www.ftc.gov/news-events/topics/truth-advertising/advertisement-endorsements

Estas fuentes validan características y obligaciones generales, **no** los precios en una fecha concreta ni los resultados del usuario. Consultar primero la documentación oficial actual de cada plataforma antes de publicar, añadir audio de catálogo o contratar servicios.

## Matriz de verificación reproducible

`NOT_CHECKED`: no se intentó. `DOC_VERIFIED`: fuente primaria confirma que la tecnología existe. `TECHNICAL_SMOKE_PASS`: se renderizó/reprodujo un archivo y se inspeccionó su metadata. `VISUAL_QA_PASS`: pieza examinada con criterio. `RELEASE_READY`: derechos, claims, copy, formatos, aceptación y atribución revisados.

- FFmpeg: utilizar [scripts/render_smoke.py](scripts/render_smoke.py) con un still autorizado; probar MP4 y decodificación. El resultado es **una prueba de pipeline de montaje**, no una película 3D ni un anuncio evaluado.
- Blender: instalar y ejecutar prueba original cuando se decida la ruta B; no marcar PASS antes.
- Escenas humanas: prueba real de grabación/consentimiento antes de afirmar credibilidad.
- Demo de producto: captura real y permisos verificados; ninguna captura ilustrativa debe venderse como producto.
- Analítica: datos observados con fecha, denominador y alcance; cero observaciones no demuestra rechazo de audiencia.

## Archivo de evidencia por proyecto

Guardar bajo el repo del producto `production-evidence/<id>` o ruta equivalente: herramientas/versiones, licencias y manifiesto de materiales; guion/shotlist; comandos render; checksum del MP4; ffprobe; capturas inicio/medio/final; revisión de sonido y safe areas; estado de publicación y métricas reales cuando existan. Nunca incluir secretos o personas privadas.
