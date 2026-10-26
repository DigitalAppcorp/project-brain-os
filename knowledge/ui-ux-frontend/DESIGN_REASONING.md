# Núcleo de razonamiento — diseño centrado en usuarios

## Misión
No producir una composición solo porque resulte habitual, convincente en una demo o fácil de programar. Formular decisiones situadas: **para quién**, **qué intenta hacer**, **en qué contexto**, **qué necesita comprender**, **qué riesgo tiene** y **cómo comprobar el resultado**.

Este módulo coordina modos; no reemplaza gates, seguridad y permisos de Project Brain OS ni dicta una estética particular.

## Protocolo corto de decisión
1. Identificar naturaleza de la solicitud: proyecto nuevo, pantalla, ajuste puntual, auditoría, investigación de referencias, rediseño, implementación o optimización. Elegir **esfuerzo proporcional**.
2. Separar **hechos confirmados** (por usuario/repo/datos), **restricciones**, **decisiones aprobadas**, **supuestos** y **preferencias**. No inventar servicios, ventajas, ratings, garantías, disponibilidad o permisos.
3. Describir tarea desde el punto de vista de la persona usuaria: `En [situación], quiero [acción/conocimiento], para [resultado]`. No convertir esa fórmula de trabajo en título visible.
4. Identificar el modelo mental, la acción principal, las excepciones, los datos necesarios y los riesgos (confianza, accesibilidad, integridad y privacidad).
5. Elegir patrón existente solo cuando su función encaje; si no, explorar estructuras alternativas. Distinguir **frecuencia de un patrón** de **idoneidad** para este producto.
6. Someter propuesta propia a contradicción: ¿qué haría que esta solución fallara?, ¿qué parte es gusto subjetivo?, ¿qué cambiaría mi recomendación?
7. Definir test observable antes de declarar calidad. Para textos aplicar [AUDIENCE_BOUNDARY.md](AUDIENCE_BOUNDARY.md) y [UX_CONTENT.md](UX_CONTENT.md); para cambios aplicar [CHANGE_INTEGRITY.md](CHANGE_INTEGRITY.md).

## Filtro de relevancia por elemento
Antes de añadir un título, etiqueta, eyebrow, pastilla, separador, número, contador, texto de apoyo, tarjeta, animación o botón, responder:
- ¿Qué información nueva/acción/estado aporta a la audiencia?
- ¿Esta pantalla necesita este elemento para orientar, decidir, entender o actuar?
- ¿Se puede eliminar o simplificar sin pérdida?
- ¿El elemento existe solo para que el Product Owner reconozca la estructura del brief?
- ¿Es requisito legal, comercial o accesible verificable? Si lo es, conservarlo incluso si estéticamente incómodo; mejorar presentación, no ocultarlo.

El filtro **no prohíbe** títulos centrados, izquierda, eyebrow, tarjetas ni numeración. Solo cuestiona automatismos sin justificación; un paso 1–2–3 puede ser útil si existe orden real.

## Modos de trabajo y contrato de salida
| Modo | Evidencia de entrada | Decisión y resultado mínimo |
| --- | --- | --- |
| Producto nuevo | público, propuesta de valor, hechos disponibles; incertidumbres | UX brief/arquitectura básica, direcciones opcionales, estados, criterio de aceptación |
| Pantalla nueva | navegación, tarea, decisiones de marca, roles | alternativas visuales, preview final y decisiones PO según [VISUAL_APPROVAL_PROTOCOL.md](VISUAL_APPROVAL_PROTOCOL.md); flujo, estados y test |
| Ajuste puntual | pantalla y cambio deseado | alcance mínimo, preservación, diff y prueba focalizada |
| Rediseño | sistema existente, métricas, problemas y aprobaciones | original y propuesta terminada según [VISUAL_APPROVAL_PROTOCOL.md](VISUAL_APPROVAL_PROTOCOL.md); alcance y anti-regresión |
| Auditoría | pantallas, código, runtime, evidencia disponible | hallazgos con severidad/certeza/estado, solución y pruebas |
| Inspiración/referencias | interfaz externa identificada | análisis de principios y límites de transferencia, sin clonación |
| Implementación | decisión y contrato UX aprobado | código seguro, estados verificados, QA, divergencias documentadas |
| Optimización | métricas, investigación o incidencias | hipótesis, experimento, decisión y aprendizaje |

Para una pregunta conceptual no crear documentos ni preguntas innecesarias. Para un cambio cosmético no imponer investigación costosa. Para un producto completo, no reducir arquitectura a un screenshot.

## Separación entre calidad de diseño y convicción
Una explicación elegante puede ser equivocada: no afirmar que los usuarios prefieren algo sin investigación; no inventar causas psicológicas, métricas o «reglas Apple». Clasificar `norma / guía / evidencia / hipótesis / preferencia`. Buscar fuentes primarias cuando cambian estándares o patrones de plataforma.

## Resolución de discrepancias
Si la intención del PO es incompatible con cumplimiento, seguridad o utilidad crítica: explicar conflicto, ofrecer alternativa viable y preservar agencia de decisión dentro de límites. Si el PO expresa preferencia estética legítima, respetarla sin convertirla en norma global.

## Registro proporcional
Para decisiones irreversibles o significativas guardar motivo, alternativas, riesgo y prueba en el repositorio del producto con [DESIGN_MEMORY.md](DESIGN_MEMORY.md). No acumular fichas para píxeles triviales.

## Recuperación contextual previa
Aplicar [ADAPTIVE_LEARNING.md](ADAPTIVE_LEARNING.md) antes de proponer: consultar solo el producto/pantalla/componente y contexto pertinentes, recuperar preferencias sustituidas y errores recurrentes para evitar repetirlos. La prioridad heurística orienta el criterio; no reemplaza investigación, restricciones o nuevas decisiones del PO.
