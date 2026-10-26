# Protocolo de aprobación visual

Fuente única de decisiones de aprobación visual del especialista. Complementa los gates de [QUALITY_GATES.md](QUALITY_GATES.md) y el gobierno de Brain OS; no concede permisos de producto, Git ni producción. Mecánica de previews: [PREVIEW_ARCHITECTURE.md](PREVIEW_ARCHITECTURE.md).

## Presentación según alcance

- **Pantalla nueva:** normalmente tres alternativas A/B/C visuales y claramente identificadas, con diferencias de composición pertinentes. Mostrar capturas o prototipos accesibles, contexto, ventajas y límites breves. Si el PO ya fijó el diseño o menos opciones representan mejor la tarea, justificar la reducción; no inventar alternativas cosméticas para completar una cuota.
- **Rediseño:** mostrar captura original con fuente/fecha/estado, problemas fundamentados y propuesta terminada. Si no existe acceso al original, declarar la limitación y recuperar una referencia antes de afirmar comparación. Separar defectos medidos de preferencias e hipótesis.
- **Cambio visual significativo:** siempre presentar preview final fiel antes de transferir al producto. Incluir estados y viewports pertinentes, fuentes y contenido representativos; JSX/CSS y descripciones por sí solos no son presentación visual.
- **Ajuste pequeño:** una comparación o recorte antes/después y registro breve bastan; no exigir tres conceptos ni un expediente. Una instrucción directa y precisa del PO puede autorizar ese delta acotado. Si el ajuste altera jerarquía, identidad, navegación o composición, reclasificar como significativo y presentar preview previa. Nunca extender una corrección puntual a un rediseño.

## Decisiones separadas

| Decisión | Evidencia necesaria | Qué permite |
| --- | --- | --- |
| Propuesta presentada | Artefacto accesible identificado por versión | Revisión, sin aprobación inferida |
| Alternativa seleccionada | Mensaje del PO que identifica A/B/C | Refinar esa alternativa en el entorno aislado |
| Preview final aprobada | PO acepta versión, superficies y estados mostrados | Fijar baseline visual, sin permiso automático de implementación |
| Implementación autorizada | Instrucción directa del PO con alcance y destino | Transferir únicamente el delta autorizado a rama de producto |
| Implementación verificada | Comparación baseline ↔ runtime y QA del alcance | Reportar fidelidad y diferencias; no inferir aceptación del PO |
| Implementación aceptada | PO acepta lo realmente mostrado de la implementación | Cerrar aceptación visual de ese alcance |
| Publicación autorizada | Gate y permiso aplicables de Brain OS/producto | Publicar solo dentro de ese permiso |

Las decisiones pueden constar en un mismo mensaje inequívoco, por ejemplo «Apruebo la preview B v2 y autorizo implementarla en la rama X». Conservar esa autorización y no volver a pedirla sin cambio material. «Me gusta B», silencio, build verde, recomendación del agente o aprobación de otra pantalla no autorizan implementar. Si el mensaje no distingue elección de ejecución y no existe autorización previa suficiente, pedir solo la decisión faltante.

## Evidencia durable

Usar [templates/VISUAL_APPROVAL_RECORD.md](templates/VISUAL_APPROVAL_RECORD.md), enlazado desde el DIR de [DESIGN_MEMORY.md](DESIGN_MEMORY.md). Registrar producto, superficie, ID/versión de preview, archivos y SHA-256 (o commit inmutable), viewports/estados, decisión exacta del PO, fecha, fuente recuperable del mensaje y límites. Estado inicial: **PENDING**, nunca aprobado por el agente. No almacenar secretos ni conversaciones completas.

La aprobación cubre solo el artefacto y alcance identificados. Cambiar contenido, assets, layout o estados de manera material crea una nueva versión y exige revisar el delta; conservar aprobaciones de partes intactas. Una captura antigua puede servir como evidencia histórica, no acredita una aprobación nueva ni el runtime actual.

## Preservación y control de deriva

Recuperar invariantes aprobadas antes de proponer. No sustituir tipografía, copy, tokens, composición o funciones por gusto del agente. Una necesidad de accesibilidad o integridad debe fundamentarse y resolverse con el menor delta; no legitima cambios visuales arbitrarios. Para divergencias, usar [CHANGE_INTEGRITY.md](CHANGE_INTEGRITY.md): restaurar el baseline o presentar el cambio significativo para decisión del PO antes de incorporarlo.

La selección no cambia permisos de backend ni datos; una preview aprobada no demuestra accesibilidad, funcionamiento, consentimiento comercial ni publicación. Si no se puede mostrar el resultado, marcar **BLOCKED** la revisión visual y documentar el límite; no declarar «revisado por el PO».

## Uso breve por el Product Owner

1. «Prepara una pantalla de [objetivo] y muéstrame alternativas» o «Muestra el original de [vista] y una propuesta de rediseño».
2. «Elijo B; ajusta [detalle]» para seguir diseñando en aislamiento.
3. «Apruebo B v2 y autorizo implementarla en [rama/alcance]» cuando el resultado esté listo.
4. Revisar comparación de implementación. Publicación sigue su gate independiente.

## Aprender de cada revisión
El agente recupera lecciones antes de diseñar y registra el feedback normal del PO después de revisar mediante [ADAPTIVE_LEARNING.md](ADAPTIVE_LEARNING.md), sin solicitar otro formulario. Usar ID/versión y fuente del registro visual para evitar duplicación; enlazar evento(s) de aprendizaje desde esa ficha. La etapa determina qué se aprobó: alternativa/referencia, preview o implementación. Prioridades y recompensas nunca crean autorización, y el contrato READ_ONLY_AUDIT impide escribir el ledger en ese modo.
