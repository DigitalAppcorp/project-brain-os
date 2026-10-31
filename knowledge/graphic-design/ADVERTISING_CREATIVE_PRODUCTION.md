# Graphic Design OS — Producción publicitaria real (corrección por regresión 2026-10-30)

## Por qué existe
El PO rechazó una colección de diez anuncios para PAZO: parecían portadas de libros, periódico o afiches editoriales. Tenían PNG correctos, textos legibles y colores de marca, pero **no diez ideas publicitarias**. El manifiesto marcaba `CREATIVE_REVIEW_CANDIDATE` sin cumplir el esquema/evidencia del validador real. La habilidad había sido fusionada tras pruebas de reglas, **no de competencia creativa sostenida**.

**Punto central:** obedecer un brief, declarar PASS o producir archivos es diferente de diseñar publicidad persuasiva. Una IA que solo añade más texto, formas geométricas y titulares a una imagen no está realizando dirección de arte.

## CAMBIO DE MÉTODO: idea → escena → arte, no copy → plantilla

### 0. Brief de una sola frase (marketing)
Por cada propuesta: «Para [audiencia que no conoce el producto], quiero que [acción] porque [tensión/beneficio comprobable], demostrado mediante [evidencia auténtica]». Sin una acción o tensión específica, no generar arte.

### 1. Elegir un mecanismo visual, no una categoría de estilo
Se debe poder describir **qué pasa dentro de la imagen sin leer el titular**:
- **Demostración en contexto real**: acción comprobable, por ejemplo un teléfono que efectivamente escanea un QR de una mascota; ninguna captura inventada.
- **Situación cotidiana con giro**: reacción humana/animal, contraste relevante con la función, humor visual auténtico.
- **Problema visualizado**: conflicto y resultado que la app realmente posibilita; ni una lista de funciones ni un claim emocional abstracto.
- **Momento espontáneo/social**: estilo de foto natural o contenido de creador, sin simular testimonios o usuarios.
- **Técnica visual inesperada**: escala, punto de vista, montaje compositivo o ilustración conceptual legible, elegida porque ayuda al mensaje.
- **Producto real, prueba real**: captura oficial de PAZO en un contexto original, no teléfono inventado ni mapa de fantasía.

Estos mecanismos son **herramientas exploratorias**, no cinco plantillas obligatorias. Para una colección variada, variar insight, acción de la imagen, escala/plano, contexto, presencia de personas, medio y relación con copy. Un anuncio solo de tipografía puede ser excelente, pero no debe dominar una serie si los demás ya son tipográficos.

### 2. Investigación visual OBLIGATORIA antes de producir
Para un lote completo, documentar al menos tres referencias publicitarias **actuales o pertinentes**, procedentes de anuncios reales (p. ej., Meta Ad Library / campañas oficiales de marcas), no exclusivamente de Dribbble, dashboards, carteles, cubiertas de libros o imágenes generadas con IA. Por cada referencia registrar:
- enlace, creador/marca, fecha o periodo conocido;
- **mecanismo publicitario** observable: situación, POV, objeto, emoción, demostración, ruptura de expectativa;
- por qué podría ayudar a nuestra audiencia; qué elementos *no* copiar;
- cómo se diferencia materialmente de las otras referencias.

**No copiar obras ni layouts**; estudiar oficio. Si no es posible recuperar referencias actuales, marcar `REFERENCES_NOT_VERIFIED` y trabajar solo en concepto exploratorio, no decir que hubo investigación.

Fuente de metodología: Meta Blueprint «Increase campaign performance with diversified creative» (diversificar concepto/motivadores y formatos): https://www.facebookblueprint.com/student/path/253130-increase-campaign-performance-with-diversified-creative. La diversidad NO es multiplicar variaciones del mismo póster.

### 3. Previsualización de conceptos sin texto ni logo
Antes de escribir todo el copy, crear **un boceto de escena** o describir de forma falsable:
- sujeto + acción + punto de vista + contexto + efecto emocional;
- qué prueba la imagen (no el título);
- qué significado cambia si quitamos las palabras;
- dónde se coloca el logo auténtico después;
- cómo se contará la misma idea en español y en inglés sin modificar la fotografía.

**Prueba:** si el boceto sin letras podría ser portada de libro, póster de evento, periódico o simple stock de mascota, y no tiene una situación/acción publicitaria, devolver a exploración. No es un veto global al diseño editorial; es una regresión contextual cuando el PO pidió anuncios modernos y no hay idea visual.

### 4. Producción profesional / separación de capas
- El generador visual produce **materia prima visual**, idealmente imagen sin logo, sin texto ni falsos UI. Un resultado en mosaico cuando se pidió imagen individual es un defecto; no cortarlo sin revisar si cada panel existe y tiene resolución/encuadre suficiente.
- Componer con herramienta capaz de posicionar, editar y revisar tipografía, logotipo oficial y fotografías individuales. No pedir al generador que adivine el logo.
- Si se anuncia una función, capturar su uso de la app real o usar una metáfora clara que no pretenda ser pantalla real.
- Prohibido crear ocho o diez anuncios partiendo de un encabezado verde y una lista de beneficios; esto es producción por plantilla.
- El resultado final deberá leerse y sentirse como publicidad de una app, no como un folleto de lectura editorial. El color, fuente o fotografía por sí solos no establecen ese criterio.

### 5. Prueba contra el sesgo editorial antes del lote
Revisar tres ejes por cada pieza terminada:
1. **Situación/idea visual:** ¿hay algo que hace detenerse, mostrar una acción o invitar a descubrir el producto? Si solo es «titular + foto recortada + logo», `CRAFT_REVISE`.
2. **Parecido de familia:** al lado de 2–3 piezas ya aprobadas, ¿la propuesta agrega otro mecanismo visual o solo altera texto/foto/color? Si es lo segundo, `DIVERSITY_REJECT`.
3. **Comercialidad y categoría:** sin descripción externa de Meta, ¿se entiende en 3 segundos qué es PAZO (app gratis) y qué acción concreta permite? Si no, `COLD_AUDIENCE_REVISE`.

Registrar cuál de las alternativas **se descartó y por qué**, antes de seleccionar la final. No fabricar revisión externa; autoevaluación no equivale a resultados de usuarios.

### 6. Evidencia ineludible
- **No** llamar `CREATIVE_REVIEW_CANDIDATE` a una colección con manifiesto simplificado. Crear manifesto compatible con schema_version=2 y ejecutar `scripts/validate_creatives.py`; conservar salida PASS/FAIL y referencias de los archivos exactos. Si no se corrió, `EVIDENCE_GATE_NOT_RUN` (no PASS).
- La inspección artística no es sustituible con este script: mostrar cada imagen individualmente y una matriz comparativa. Proporcionar veredicto creativo por imagen.
- La audiencia fría no se inventa. `COMPREHENSION_NOT_TESTED` hasta que personas sin contexto respondan a la prueba.
- Prohibido fusionar una mejora del OS basándose solo en tests de Python; exigir **una nueva ronda visual** con ejemplos claramente distintos.
- No guardar anuncios, fotos ni creativos PAZO en Brain OS/GitHub salvo petición explícita del PO; sí conservar reglas, lecciones y casos de fallo generalizables.

## Gating tras este incidente
- `PROCESS_DOCUMENTED`: instrucciones y regresiones en repositorio.
- `PROCESS_TESTED`: scripts de contrato PASS (no demuestra diseño).
- `ART_DIRECTION_REVIEWED`: 3 imágenes de nueva ejecución abiertas e inspeccionadas, con tres conceptos realmente diferentes.
- `OWNER_ACCEPTED`: el PO confirma que la creatividad responde al estándar visual. **No equivale a performance de campaña.**
- `CAMPAIGN_READY`: además cumplimiento de marca, producto, pruebas externas, privacidad, tracking y autorización.

Después del rechazo de un lote, **reducir a una prueba de 2–3 conceptos realmente distintos**, nunca repetir otros 10 automáticamente. La vía de recuperación es crear imágenes nuevas que prueben el método, no agregar más reglas sin ensayo.
