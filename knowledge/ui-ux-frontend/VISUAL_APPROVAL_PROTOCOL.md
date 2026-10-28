# Protocolo de decisión y revisión visual

Fuente única especializada. Complementa [QUALITY_GATES.md](QUALITY_GATES.md) y Brain OS: **no concede permisos de implementación, merge, datos, gasto ni publicación**. Una consulta/auditoría continúa siendo solo lectura. Mecánica: [PREVIEW_ARCHITECTURE.md](PREVIEW_ARCHITECTURE.md).

## Elegir el carril antes de diseñar

| Carril | Condición y responsabilidad | Gate estético |
| --- | --- | --- |
| UI nueva en alcance autorizado | El PO autorizó la mejora; Design OS decide patrón, jerarquía, composición, contenido y estados, critica y corrige internamente | DESIGN_QA_PASS; PO_VISUAL_ACCEPTED=NOT_REQUESTED. No pedir al PO elegir variantes ni rescatar una composición débil |
| Rediseño dirigido por PO | El PO pide cambiar una pantalla/dirección previamente aceptada: recuperar evidencia de esa intención y preservar lo ajeno al delta | Gate profesional y revisión del PO contra su intención, salvo delegación explícita vigente. No inventar una aceptación anterior |
| Decisión fuera de alcance | Cambio de propuesta/identidad aprobada, navegación estructural, promesa comercial, seguridad/cumplimiento o gasto | Escalar solo esa decisión genuina; no usarla como pretexto para microaprobaciones |
| Corrección técnica sin delta visual | No cambia composición/contenido/interacción visual | Pruebas de invariantes; no imponer un proceso estético ni alternativas |

Una pieza nueva rechazada es feedback sobre ese patrón concreto, no un veto universal ni una orden de rediseñar toda la aplicación. Las instrucciones recientes y explícitas del PO prevalecen; conservar su fuente y alcance. **Autonomía de diseño no es autorización de lanzamiento.**

## Gate profesional autónomo obligatorio

1. Recuperar propósito, audiencia, tarea, sistema real aprobado, estados y aprendizaje pertinente. Registrar **alineación con el brief**: requisitos expresos, interpretación de las referencias, supuestos y evidencia que los satisface. Identificar a qué pieza aplica una referencia: un aviso transitorio y un estado propio de pantalla son superficies distintas. No sustituir el aviso independiente solicitado por contenido de página, convertir el error de pantalla en ese aviso ni omitir ilustraciones solicitadas por preferencia minimalista; son ejemplos de fidelidad al encargo, no patrones universales. Preguntar internamente si simplificar o eliminar la pieza nueva resuelve mejor la tarea sin incumplir el encargo. Separar hechos, hipótesis y preferencias.
2. Cuando el problema lo requiera, explorar al menos dos estructuras distintas en aislamiento. Comparar también con no añadir nada. Descartar ornamento, duplicación de acciones y alternativas que solo cambian colores. Seleccionar una dirección con razones y trade-offs; no hacer votación ni presentar una tarea de selección al PO.
3. Inspeccionar **capturas completas del runtime**, vistas realmente por el revisor, con contenido representativo: pendiente/lento, contenido, vacío, error y recuperación cuando apliquen; idiomas/viewports pertinentes. No limitarse al componente. Registrar qué datos/condiciones se forzaron, fuentes reales/fallback, versión, capturas y límites. Probar interacción, scroll/dock y foco aparte de la imagen.
4. Hacer una pasada adversarial separada, preferentemente por un revisor independiente autorizado y disponible: ¿qué parece arbitrario?, ¿se integra mejor en una superficie existente?, ¿el vacío es intencional o residual?, ¿qué ocurre bajo error/carga?, ¿compiten acciones?, ¿por qué es mejor que no añadir nada? Si no se usa segundo revisor, identificar la pasada separada y sus límites. Listar defectos concretos, corregir, recapturar y comparar antes de decidir.
5. Evaluar jerarquía, composición, continuidad, espacio negativo, densidad/carga cognitiva, identidad, tipografía/copy, significado de CTA y estados. Targets, contraste, overflow, build y CI son necesarios según alcance, **nunca suficientes para PASS visual**. Sin evidencia de composición/estados: NOT_EVALUATED o DESIGN_QA_FAIL, aunque ingeniería pase.
6. Guardar decisión profesional, razones, alternativas descartadas, fallos/correcciones observables y riesgos. Si no supera el gate, seguir corrigiendo dentro del alcance; no pedir al PO otra orden técnica ni aceptación estética rutinaria. Escalar solo bloqueo humano/productivo real.

El criterio no es una cuota de documentos ni una puntuación estética fabricada. Para un ajuste inocuo basta evidencia acotada. No exigir estados que no existan: justificar NOT_APPLICABLE. No llamar normal a una espera artificialmente infinita de laboratorio; revisar también condiciones resueltas.

## Evidencia y estados separados

Usar [registro](templates/VISUAL_APPROVAL_RECORD.md), enlazado desde el DIR. Guardar producto/superficie, autorización vigente, carril, versión/commit, capturas completas, estados/idiomas/viewports, crítica y correcciones. La evaluación profesional interna y la decisión del PO ocupan campos distintos:

- DESIGN_QA_PASS / DESIGN_QA_FAIL / NOT_EVALUATED: decisión profesional identificada y sustentada. No implica aceptación del PO.
- PO_VISUAL_ACCEPTED: YES solo con mensaje recuperable y alcance visto; NOT_REQUESTED para nueva UI ordinaria; PENDING cuando el carril dirigido requiere decisión.
- IMPLEMENTATION_AUTHORIZED: fuente y alcance propios; elegir una referencia o auditar no lo concede.
- ENGINEERING_READY: pruebas funcionales, seguridad e invariantes, independiente del gate artístico.
- RELEASE_AUTHORIZED: decisión separada del producto. Ningún estado anterior la crea.

Una captura creada pero no inspeccionada no acredita revisión. Si faltan capturas/runtime y son necesarios, registrar el límite; no cerrar el gate ni fingir revisión del PO. Si un mensaje del PO acepta preview y autoriza implementación inequívocamente, conservarlo y no pedirlo otra vez. Revisiones voluntarias del PO se registran como tales sin convertirlas en condición para toda UI futura.

## Preservación y aprendizaje

Recuperar invariantes antes de modificar y contrastar con la implementación mediante [CHANGE_INTEGRITY.md](CHANGE_INTEGRITY.md). No sustituir marca, tipografía, información ni funciones aprobadas por gusto; una corrección local no autoriza rediseño global. Congelar versiones y documentar diferencias; no actualizar un baseline para ocultar un defecto.

Registrar feedback contextual con [ADAPTIVE_LEARNING.md](ADAPTIVE_LEARNING.md), distinguiendo etapa/artefacto y aprobación de referencia frente a implementación. El reemplazo corregido por el agente no gana una aceptación del PO ficticia. No guardar preferencias de un producto en el OS ni escribir ledger en READ_ONLY_AUDIT. Las evaluaciones reproducibles del método viven en [EVALUATIONS.md](EVALUATIONS.md); verificar un registro no equivale a medir calidad artística ni a demostrar superioridad del modelo.
