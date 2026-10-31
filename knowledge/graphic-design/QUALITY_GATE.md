# Graphic Design OS — quality gate verificable

La calidad visual se decide ante el **arte final real**. Un doc sin diseño o un archivo raster técnicamente válido no pueden ser `CREATIVE_PASS`.

## Vetos sin ponderación (fallo automático)
1. **Mensaje falso**: beneficio, precio, identidad, datos, disponible en tiendas, testimonios o pantallas inventadas.
2. **Formato incumplido**: cantidad, relación de aspecto, archivos individuales, idiomas o formato solicitado incorrectos.
3. **Falta de distintividad de la serie**: diez piezas basadas en la misma estructura y retrato con solo cambios cosméticos, cuando se solicitó exploración de conceptos.
4. **Incomprensible en contexto**: no se entiende qué es el producto, para quién o qué ofrece en el tiempo/placement del brief.
5. **Mala producción**: texto cortado/incorrecto, imagen borrosa, recortes defectuosos, logos alterados, licencias no resueltas, máscara o montaje falso en material presentado como realidad.
6. **Falsa auditoría**: `PASS` declarado sin inspección de cada archivo final. No fabricar entrevistas ni revisión externa.

## Evaluación de oficio (rúbrica orientativa, no un score mágico)
- 20: **Idea visual propia**. ¿La imagen expresa un insight, tensión, gesto o metáfora, no solo una foto simpática?
- 20: **Claridad comercial**. Categoría, promesa y rol de marca comprensibles sin contexto previo.
- 15: **Composición y dirección de mirada**. Foco, encuadre, escala, ritmo, espacio negativo y relación sujeto/texto deliberados.
- 15: **Tipografía y copy visual**. Titular, legibilidad, espaciado, fraseo y jerarquía elegidos para el arte.
- 10: **Calidad y autenticidad de imagen**. Fotografía/ilustración/retocado consistente y sin detalles generativos defectuosos.
- 10: **Identidad y singularidad**. Reconocible como marca sin convertir cada pieza en su clon.
- 10: **Ejecución y contexto**. Crop, tamaño, accesibilidad, licencias, salida, CTA/placement correctos.

Los puntos son guías para discusión; `85+` no autoriza nada si hay veto. No afirmar revisión independiente si solo hubo autocrítica de un agente.

## Cinco revisiones observables
**1. Miniatura**: abrir el final a un tamaño comparable al teléfono; lectura visual en un segundo y comprensión candidata en tres.
**2. Arte pleno**: mirar cada pieza individualmente, no solo un contact sheet. Revisar texturas, recortes, puntuación, calidad fotográfica, logotipo y bordes.
**3. Comparación de serie**: colocarlas juntas. Medir repetición de composición, fotografías, titulares y recursos; explicar diferencias visibles. Si parece una pantalla de dashboard repetida, `REJECT`.
**4. Test externo a ciegas**: mostrar la imagen sin explicar la tarea. Preguntas: "¿Qué se anuncia?", "¿Es gratis?", "¿Qué puedes hacer?", "¿Dónde actuarías?". Respuestas observadas con tamaño de muestra y limitaciones; si no se realizó, `NOT_TESTED`.
**5. Comprobación factual y de derechos**: referencia real de cada claim, revisión de los assets y reglas del placement. Sin autorización de publicación/gasto por elaborar la pieza.

## Protocolo de resultado
Por imagen: `ID | idea | archivo | formato | factual | visual | derechos | comprensión externa | veto | estado | cambios`.

Estados: `BRIEF_ONLY`, `COMP_IN_PROGRESS`, `CREATIVE_REVISE`, `CREATIVE_REJECT`, `CREATIVE_REVIEW_CANDIDATE`, `RIGHTS_PENDING`, `READY_FOR_PO_REVIEW`, `APPROVED_FOR_PUBLICATION`, `PERFORMANCE_MEASURED`.

**No confundir:** buena estética =/ conversión; satisfacción del Product Owner =/ respuesta de audiencia; contrato escrito =/ capacidad artística entrenada. Exigir evidencia posterior para modificar heurísticas.

## Gate adicional v0.2 — Identidad y comprensión
- **Logo source lock (B0)**: archivo oficial o referencia maestra facilitada por el PO, sin regeneración aproximada ni símbolos sustitutos; comprobar proporciones, icono/huella, espaciado, posición y contraste. La aceptación de composición nunca subsana un logo equivocado. `BRAND_REJECT` si falta.
- **Cold-audience outcome (C0)**: con el arte delante, la respuesta espontánea a `¿Qué es PAZO? ¿Es gratis? ¿Qué hago con él?` debe ser coherente con la función REAL que se anuncia. Una mención genérica de "free pet app" puede responder categoría/precio, pero no beneficio; por eso exigir una acción específica visible o expresada. Sin usuarios externos, `COMPREHENSION_NOT_TESTED`.
- **Feedback granular**: aprobación estética ≠ aprobación de marca ≠ comprensión de producto. Revisar cada dimensión por separado. La nota "me encantó" con "logo equivocado" se documenta como `DESIGN_LIKED / BRAND_FAIL`, no como pieza aprobada.

## v0.3 — El QA se realiza ANTES de mostrar un entregable
- Abrir los PNG/JPEG finales **de uno en uno**. El contacto sheet y las dimensiones no son inspección visual.
- Comprobar en el render visible que cada propuesta contiene la promesa que hace. Una pieza de QR sin QR visible o sin explicación efectiva de la acción es **CREATIVE_REJECT**, incluso si el titular es correcto.
- Contrastar material gráfico con lotes rechazados: una foto vieja recortada/colorizada sigue siendo el mismo asset; un titular nuevo no constituye variación visual sustantiva.
- Registrar hash del archivo revisado en visual_review.inspected_sha256; si el archivo cambia después de ese examen, revisar de nuevo.
- Ejecutar EXECUTION_PROTOCOL.md y scripts/validate_creatives.py. Fallo del verificador, imagen rechazada o ausencia de logo maestro = no hay READY_FOR_PO_REVIEW.
- Separar sin excepciones ART_DIRECTION, BRAND, PRODUCT_TRUTH, COLD_AUDIENCE_CLARITY, PRODUCTION_QUALITY, RIGHTS y COMPREHENSION_EXTERNAL. Resultado técnico no puede elevar el estado artístico.
- Si no es posible inspeccionar las imágenes, declarar VISUAL_NOT_TESTED y no entregar supuestos finales.
