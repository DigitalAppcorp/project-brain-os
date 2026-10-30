# Video OS v0.5 — Dirección integral de guion a pantalla (Director's Package)

**Estado:** método documentado, no prueba de nivel cinematográfico alcanzado. Fecha: 2026-10-29. Aplica a spots, cortos, demostraciones y 3D, con intensidad proporcional al encargo.

## Problema que corrige

Un **animatic narrativamente legible** puede seguir viéndose como maqueta: personajes con geometría primitiva, expresiones rígidas, iluminación plana, materiales sin detalle, cámara obstruida y pantalla del producto ilegible. Ni el guion escrito ni Blender funcionando validan el acabado. **No confundir aprobación de historia con aprobación de animación, arte, sonido o publicación.** Evitar construir actores primero y buscarles trama después.

## Contrato de dirección de una pieza nueva

Un director responsable produce un **paquete de dirección completo** antes de iniciar la producción definitiva. Los campos se adaptan según medio, sin convertir un reel corto en un trámite burocrático:

1. **Propuesta de audiencia / intención G0:** destinatario, situación, transformación A→B, recompensa (risa, emoción o utilidad), lugar causal del producto, promesa y payoff, acción al final, métrica y fuentes/limitaciones. No inventar valor para justificar un render.
2. **Guion literario:** logline, deseo visible del protagonista, obstáculo, escalada con causa y efecto, elección y resolución, gag o recompensa, voz/diálogos exactos o decisión deliberada de silencio, acciones legibles sin rótulos.
3. **Guion técnico continuo:** timecode y duración de **cada plano**, objetivo del corte, escala y lente/ángulo motivados, blocking, recorrido de cámara, acting por poses y ojos, utilería interactiva, continuidad espacial y sonido en la toma. Suma de duraciones consistente.
4. **Biblia de actuación:** objetivo emocional y acción física por personaje; anticipation, eye-lines, weight shift, contact, lead/follow, settle, timing/spacing y expresión facial. No substituir actuación por movimiento mecánico, loops aleatorios o interpolación lineal.
5. **Biblia de arte:** estilo definido por imágenes/frames originales con derechos; model sheets, escala, rasgos consistentes, topología y rig de personajes, set plan/floorplan, texturas/materiales, paleta, iluminación por plano y profundidad. Priorizar recursos de personajes de calidad sobre fondos/efectos prescindibles.
6. **Diseño de sonido:** línea exacta, rol y tiempo de cada diálogo, ambiente, foley causal, silencios, entradas musicales, transiciones sonoras, mezcla, derechos y control de inteligibilidad.
7. **Prueba de producto:** captura real autorizada con rama/entorno/fecha, demo explícitamente etiquetada cuando corresponda; sin UI falsa, datos personales ni logros inventados. La ficción visual no debe presentarse como conducta de usuario real.
8. **Plan de factibilidad:** software y recursos verificados, GPU/RAM, licencias, coste de assets/renders, duración de pruebas, alternativa si falla el acting, seguridad. Si la ruta gratuita no alcanza acabado, no reetiquetar maqueta como cine.
9. **Revisión de intención y coherencia:** test sin rótulos, lectura a velocidad real, resolución del conflicto y cierre. Un chiste donde la marca se pega al final sin causación no satisface pieza comercial.

## Puertas de calidad diferenciadas

- **D0 STORY:** propuesta, guion, emoción, causalidad y payoff claros; aprobación del relato **no** aprueba apariencia.
- **D1 ASSET/ART:** aprobar 1 frame de **personaje en pose**, 1 close-up expresivo y 1 encuadre del escenario con luces/materiales finales; inspeccionar silhouette, rig, cara, ojos, sombras, profundidad y acabado. Primitivas/lookdev no son final.
- **D2 MOTION/ACTING:** escena de 3–5 segundos con acting verdadero (anticipación→acción→reacción→settle) y contactos, sin roturas de malla, miradas erráticas, pops o deslizamiento. Si falla, corregir rig/poses antes de más escenas.
- **D3 ANIMATIC:** historia completa con storyboard, blocking, continuidad temporal y espacial, diálogos temporales y sonido esencial. Estado `STORY_APPROVED` separado de `VISUAL_FINISH_APPROVED`.
- **D4 FINAL COMPOSITING:** render/comp con estética coherente, físicas visuales, iluminación y texturas, fondos y profundidad, color consistente, UI auténtica legible, audio/licencias, sin obstrucciones de cámara. Un aumento de resolución no cuenta como corrección de un modelo malo.
- **D5 QA:** visionado integral a velocidad real en móvil con y sin audio, visualización cuadro a cuadro de los peores puntos, prueba técnica de decodificación, verificación de derechos/producto y revisión contraria. Usuario/tercero evalúa cuando se afirma revisión independiente; la segunda pasada de la misma IA es autocrítica y se etiqueta así.

En cualquier gate devolver `PASS_WITH_SCOPE`, `REVISE`, `REJECT`, `NOT_TESTED` o `BLOCKED`, con pruebas concretas. **Nadie declara VIDEO_READY** solamente porque hay personajes, animatic o MP4 reproducible.

## Tratamiento de hardware limitado

- Primero **asset reutilizable de alta calidad + set compacto + acting corto**, no cinco personajes low-poly, diez locaciones ni simulaciones caras.
- Animatic con proxies/workbench. Para render final medir muestra real de 1–3 fotogramas y memoria; Eevee/CPU u otra ruta según compatibilidad observada. La GPU compartida y 8 GB de RAM no equivalen a tarjeta con VRAM dedicada.
- Renderizar secuencias por planos y componer fuera de Blender, si ello reduce uso de RAM; preservar fuente, rigs, texturas, sonido y posibilidad de reproducir.
- Permitir cámara/reparto optimizados (primeros planos, humano fuera de cuadro cuando narrativamente tiene sentido); **no** ocultar a un personaje defectuoso y llamarlo «calidad».
- Si tras D1/D2 el resultado sigue rústico, levantar `ART_DIRECTION_FAIL` y proponer asset/rig autorizado o render remoto; no repetir el mismo pipeline sin aprendizaje.

## Revisión dura contra fallos históricos

| Falla | Pregunta / prueba de rechazo |
| --- | --- |
| Personaje «muñeco de bloques» | ¿El diseño, materiales, rig y cara cumplen la referencia final, o solo permiten visualizar la trama? |
| Rig inerte | ¿Pueden leerse pensamientos/decisiones en ojos, postura y pausa incluso sin música ni texto? |
| Set genérico | ¿Tiene profundidad, escala, luz orientada y utilería causal? ¿Se ven contactos y sombras creíbles? |
| Cámara atravesada por objetos | ¿Se inspeccionaron todos los frames o al menos el plano completo, no una miniatura? |
| QR/UI ininteligible | ¿Se reconoce el producto real y puede leerse en móvil? ¿Captura auténtica? |
| Música de relleno | ¿Cada silencio, cue y acento responde a la acción, sin sustituir actuación? |
| Render 1080 desde un blockout | ¿El acabado se mejoró en geometría/materiales/acting o solo se reescaló? |
| Guion humano irreal | ¿El comportamiento animal puede justificarse como actuación estilizada, o requiere conocimiento humano imposible? |
| «Élite» por prompting | ¿Hay revisión concreta de cuadros y trabajo real? ¿Se reconoció lo no probado? |

## Entregables y aprendizaje

Cada producción importante termina con: `director_brief.md`, `script.md`, `shotlist.csv`, `acting_bible.md`, `art_bible.md`, `sound_map.md`, `assets_licenses.md`, `animatic_preview.mp4`, `source_project.blend` (o medios editables), `master.mp4`, `QA_TIMECODES.md` y un `REPORT.md` que distinga estados. Ajustar carpeta/nombres al producto.

El aprendizaje va **al estándar reutilizable** solo cuando sea generalizable; el guion, modelos, presupuesto y resultados concretos del cliente pertenecen a su repositorio. La aprobación de un guion o el merge de documentación no demuestran que la animación real mejore; comparar evidencias del antes/después y reacción de espectadores.

**Dependencias normativas:** [INTENT_AND_STORY_STRATEGY.md](INTENT_AND_STORY_STRATEGY.md), [ELITE_STUDIO_WORKFLOW.md](ELITE_STUDIO_WORKFLOW.md), [EDITORIAL_INTELLIGENCE.md](EDITORIAL_INTELLIGENCE.md), [CREATIVE_EVIDENCE_GATE.md](CREATIVE_EVIDENCE_GATE.md), [QUALITY_AND_RIGHTS.md](QUALITY_AND_RIGHTS.md), [Expert Evidence Protocol](../../patterns/EXPERT_EVIDENCE_PROTOCOL.md).
