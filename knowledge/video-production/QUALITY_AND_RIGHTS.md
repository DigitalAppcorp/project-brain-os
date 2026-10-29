# QA audiovisual, ética, accesibilidad y derechos

## Gate de historia (exigir evidencia visual)

- En los primeros segundos hay un motivo para quedarse: conflicto, curiosidad, humor, ternura, utilidad o sorpresa. **No hay fórmula obligatoria** de 2 s.
- El remate resulta comprensible sin conocer previamente la app/marca.
- La marca o producto aparece en un momento **deliberado**, no forzado.
- Las expectativas de funcionalidades, precio, disponibilidad, resultados y garantías se sustentan en la versión publicada.
- La pieza no promete interacciones, comunidad, salvamento de mascotas ni testimonios ficticios.

## Gate de imagen / movimiento

- No hay saltos de identidad, manos/rostros imposibles, patas extra, labios mal sincronizados, mirada sin foco, físicas extrañas ni texto generado ilegible. Si falla el juicio visual, **cortar, regrabar o cambiar de técnica**.
- Composición vertical sin UI importante detrás de los controles de plataforma; safe areas a validar por destino (no un píxel universal).
- Estabilidad de exposición, nitidez, encuadre, continuidad, color y volumen entre clips.
- Cada pantalla de producto proviene de la versión real, revisada y sin datos personales; no fabricar botones, fotos de usuarios ni comunidad.
- Miniatura coherente con el contenido, no engañosa.

## Gate de sonido / subtítulos

- Diálogo inteligible, equilibrio con música y efectos, sin golpes de volumen; comprobar en móvil.
- La mezcla final puede medirse con FFmpeg `loudnorm` o similar, con criterio por plataforma; evitar declarar un objetivo único normativo para todos.
- Verificar licencia de música y voz; no clonar voz de alguien ni imitar a una persona sin permiso.
- Subtítulos legibles con contraste, segmentación y sincronización, revisión humana. Comprobar la comprensión sin sonido.

## Gate técnico reproducible

Al producir MP4:
- `ffprobe -v error -show_streams -show_format -of json archivo.mp4`; inspeccionar duración real, video, audio si se declara, resolución, fps, códec, tamaño.
- Decodificar el archivo completo con `ffmpeg -v error -i archivo.mp4 -f null -` y comprobar exit code.
- Extraer cuadros del inicio, medio y final y revisarlos; no solo una portada.
- Comprobar MP4 reproducible, formato vertical objetivo y pista AAC cuando corresponda.
- Guardar comandos de render/parámetros sin claves ni URLs privadas y resumen de hashes; confirmar ruta física antes de entregar enlaces.

## Derechos y veracidad

- Identificar titular/permiso de cada fotografía, clip, logo, modelo, rig, fuente tipográfica, música, SFX y voz. No asumir que una obra publicada es reutilizable comercialmente.
- Fuentes de terceros: guardar URL, licencia, fecha, captura del alcance autorizado y requisitos de atribución; en ausencia de permiso usar material original, propio u otra opción.
- Material generado por IA: comprobar términos aplicables al modelo/proveedor y evitar derechos/identidades de terceros; etiquetar cuando la plataforma/ley requiera.
- Si se simula una escena cotidiana, no presentarla como testimonio o documental real. Actores y resultados no se atribuyen a usuarios reales.
- Claims de salud, protección, seguridad y resultados requieren especial sustento. La FTC exige que publicidad sea veraz, no engañosa y sustentada: https://www.ftc.gov/business-guidance/advertising-marketing .
- Para recomendaciones/testimonios seguir guías oficiales FTC: https://www.ftc.gov/news-events/topics/truth-advertising/advertisement-endorsements .

## Revisión de portafolio y límites de claims

Aplicar [CREATIVE_EVIDENCE_GATE.md](CREATIVE_EVIDENCE_GATE.md): una muestra MP4 con tres clips licenciados, subtítulos y logo puede tener derechos y códec válidos sin ser una escena actuada o un spot cinematográfico. Para un lote solicitado como **estilos diferentes**, se requiere verificación comparativa de la gramática visual de todas las piezas, no solo una revisión individual. La ausencia de prueba de actuación, continuidad o interacción requerida genera `CREATIVE_FAIL` o `NOT_EVALUATED`, nunca `PILOT_QA_PASS`.

## Veredicto

El revisor asigna `PASS / REVISE / BLOCKED / NOT_CHECKED` a: narrativa, calidad visual, sonido, legibilidad, veracidad, derechos, técnica y ajuste de plataforma. Si algún gate crítico está `BLOCKED`, no publicar ni afirmar que el anuncio está listo. Una revisión estética del PO no acredita por sí sola permisos de uso.
