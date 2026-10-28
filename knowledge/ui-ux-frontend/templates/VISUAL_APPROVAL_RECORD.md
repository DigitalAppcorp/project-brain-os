# Registro de aprobación visual

Plantilla; conservar por tarea fuera del OS y enlazar desde el DIR. Reglas: [protocolo canónico](../VISUAL_APPROVAL_PROTOCOL.md).

- Producto / rama / SHA / superficie:
- ID y versión de preview / alternativa:
- Archivos y fingerprint SHA-256 o commit inmutable:
- Capturas/prototipo presentado / viewports / idioma / tema / estados:
- Original y problemas fundamentados (rediseño):
- Fuentes/assets y procedencia / mocks / límites de fidelidad:
- Invariantes y delta solicitado:
- Carril: UI nueva autorizada / rediseño dirigido por PO / fuera de alcance / técnico sin delta visual:
- Autorización vigente y fuente (independiente del gate visual):
- Estructuras comparadas / por qué mejor que no añadir nada / dirección descartada:
- Runtime completo pendiente/contenido/vacío/error/recuperación: capturas vistas, condiciones forzadas y límites:
- Crítica adversarial separada: revisor/pasada, defectos, correcciones, recapturas y evidencia:
- DESIGN_QA_PASS / DESIGN_QA_FAIL / NOT_EVALUATED con razones observables:
- PO_VISUAL_ACCEPTED: NOT_REQUESTED para UI nueva ordinaria; YES únicamente con fuente; PENDING si el carril lo exige:

| Decisión | Estado inicial | PO / fecha / instrucción exacta / fuente recuperable | Alcance y límites |
| --- | --- | --- | --- |
| Selección profesional de dirección | NOT_EVALUATED | Interna para UI nueva; fuente PO si existe | |
| Aprobación PO de preview final cuando corresponde | NOT_REQUESTED | PENDING solo en carril dirigido que la exige | |
| Autorización de implementación | PENDING | | |
| Comparación con implementación | NOT_TESTED | Evidencia técnica; no aprobación del PO | |
| Aceptación PO de implementación cuando corresponde | NOT_REQUESTED | Nunca inferida de DESIGN_QA_PASS | |
| Publicación | NOT_AUTHORIZED | | |

Cambios posteriores, versión sustituida, autorizaciones previas todavía aplicables y siguiente decisión pendiente:

Eventos de aprendizaje derivados (IDs + ruta de ledger, si corresponde), aspectos conservados/corregidos y decisión pendiente: aplicar [ADAPTIVE_LEARNING.md](../ADAPTIVE_LEARNING.md) sin pedir información adicional al PO.
