# Producción: cuatro rutas y gates

**Gate de ejecución vigente:** [CREATIVE_EVIDENCE_GATE.md](CREATIVE_EVIDENCE_GATE.md). Antes del G4, el agente debe demostrar por separado la viabilidad real de cada técnica, y antes de presentar una tanda como «diversa», comprobar material y visualmente que **no reutiliza el mismo formato de clips stock, texto y end card**. Gate técnico ≠ gate creativo ≠ datos reales de audiencia.

## Decisión antes de producir

Buscar **pregunta de marketing + historia + material disponible**, no «qué herramienta es más espectacular». Si el riesgo técnico es alto, producir un test de **3–5 segundos** antes de escribir/renderizar 30 segundos. No comprometer presupuesto para explorar.

| Ruta | Técnica mínima viable | Valor | Mayor riesgo | Estado por defecto |
|---|---|---|---|---|
| A. Comercial de situación cotidiana | Clip de móvil real con iluminación natural + montaje/sonido; IA solo para apoyo | Escena cercana y creíble con producto como resolución | Actuación, sonido y derechos, error de continuidad | `CONCEPT_READY`, filmación sin validar |
| B. Caricatura / personaje 3D | Blender + rig original/licenciado + animación básica y cámara; alternativa 2D explícitamente etiquetada | Humor recurrente, continuidad de personajes | Rig, actuación, lip-sync y tiempo de render | `NOT_VALIDATED` hasta render original |
| C. Contenido natural de mascota | Video original/stock con licencia para anuncio + texto, montaje y voces | Material auténtico, poca artificialidad | Derechos, audio, claridad del remate | `CONCEPT_READY`, derechos por comprobar |
| D. Demostración útil del producto | Grabación auténtica de app/captura verificada, PII retirada, narración y cortes | Promesa clara y prueba de funcionamiento | UI inventada, privacidad y falta de gancho | `CONCEPT_READY`, assets por verificar |

**No presentar animación de fotogramas fijos como B (3D narrativo)**. Una prueba de FFmpeg puede validar edición/títulos/audio, pero nunca personajes animados 3D.

## Pipeline universal

### G0. Brief / autorización
Determinar producto, público, canal, fecha, lengua, objetivo y CTA; diferenciar post orgánico de anuncio pagado. Revisar permiso para usar materiales, grabaciones y publicar; `ad_spend=0` salvo autorización expresa.

### G1. Cuatro tratamientos breves
Por cada ruta: logline, gancho de 0–3 segundos, pequeña tensión, remate, aparición del producto, CTA, assets y riesgos de síntesis. Con hipótesis distintas, evitar fingir un A/B aislado. Definir éxito en una frase observacional.

### G2. Inventario de activos y derechos
Tabla por asset: ID, origen, tipo, derechos comerciales/atribución, consentimiento, versión, vigencia, riesgo de PII, resolución, decisión `APPROVED/PENDING/REJECTED`. La existencia en internet no concede permiso. Para música: original o licencia que cubra anuncio y plataforma, no inferir que «royalty-free» permite cualquier uso.

### G3. Prueba barata de viabilidad
5 segundos con el elemento de máximo riesgo: por ejemplo, voz y movimientos faciales 3D, credibilidad de escena humana o legibilidad de captura móvil. Medir render y revisar el resultado. Si no cumple, iterar una vez bajo límite acordado y cambiar ruta o documentar bloqueo; no quemar créditos.

### G4. Producción corta
Solo después de G3, shotlist, clips cortos, transiciones motivadas, música/voz con derechos, mezcla y subtítulos. Comenzar con 9:16 y duración experimental 15–30 s, **no regla universal**. Conservar masters y pistas editables o parámetros reproducibles.

### G5. QA técnico y creativo
Gate en [QUALITY_AND_RIGHTS.md](QUALITY_AND_RIGHTS.md), revisión manual con sonido/sin sonido y en teléfono. No publicar con `TECHNICAL_SMOKE_PASS` únicamente. El estado `PILOT_QA_PASS` solo se concede cuando el MP4, el contenido creativo, la legibilidad, los derechos y los claims han sido comprobados.

### G6. Publicación autorizada
Entregar archivo y copy/CTA, verificar requisitos de plataforma vigentes, avisos/etiquetado de IA y derechos. Publicación orgánica, anuncios y gasto requieren permiso específico. Registrar fecha, versión, destino y parámetros de atribución si el producto ya los soporta.

### G7. Interpretación crítica
Seguimiento con denominadores y ventana iguales; distinguir retención y clic de utilidad/registro. Diseñar una segunda ronda aislando variables; no declarar ganadora una técnica por uno o dos videos con públicos diferentes.

## Contrato de cuatro prototipos

Para comparar técnicas, la primera tanda puede tener cuatro **muestras cortas** (una por ruta) pero no publicar automáticamente todas. Una técnica queda validada solamente si existe media renderizada con metadatos, assets acreditados, revisión visual y aceptación. Los guiones, moodboards o herramientas instaladas son `PREPRODUCTION`.

| Formato de entrega | Mínimo por prototipo |
|---|---|
| Brief | Objetivo y mensaje verdadero |
| Historia | Gancho, tensión y resolución |
| Hoja de planos | Duración, visual, audio, activos y derechos |
| Media | MP4 real verificado + portada/cuadros de control cuando se renderiza |
| Informe | `STATUS`, costes monetarios y de trabajo, limitaciones, siguiente cambio |
| Evidencia de audiencia | `NOT_PUBLISHED` hasta publicar con permiso y recibir datos |

## Selección adaptativa

Un video puede mezclar rutas (por ejemplo, real con mascota + captura app). Etiquetar el **método dominante** para evitar atribuir un resultado a una técnica aislada. En una segunda ronda conservar concepto, CTA, duración, audiencia y distribución para cambiar **una variable** cuando sea posible.

## Antipatrones

- «El video se hizo solo»: omite edición, selección y nuevas generaciones.
- «$0» sin comprobar créditos, derechos, horas o render.
- «IA cinematográfica» sin actuación creíble.
- «Éxito» medido solo con likes o vistas sin duración/alcance.
- Identificar al espectador anónimo mediante su comportamiento en redes.
- Transformar la foto de un perro ajeno en mascota de la marca sin permiso.
