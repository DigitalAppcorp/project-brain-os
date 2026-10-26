# Interface Quality Gate — router ligero a la especialidad UI/UX

**Estado:** router complementario de Project Brain OS. **No constituye una segunda autoridad normativa de diseño.**

## Responsabilidad única
Este patrón **detecta y enruta** tareas de creación, corrección, rediseño, evaluación, inspiración o auditoría de interfaces hacia **Design Intelligence OS**, cuya entrada canónica es `knowledge/ui-ux-frontend/SKILL.md` en `main`. No reproduce límites WCAG, severidades, métricas ni recetas de pruebas; esos criterios se mantienen **exclusivamente** en la especialidad.

La jerarquía de gobierno permanece: seguridad, consentimiento, permisos, producción, Git y costes se rigen por Project Brain OS raíz. Las decisiones visuales de cada producto viven en el repositorio del producto, no aquí.

## Selección del modo (mínima)
1. **AUDIT / READ_ONLY_AUDIT** cuando el usuario pida inspeccionar, revisar, evaluar o analizar **sin cambios**. No ejecutar escrituras, tests con efectos secundarios ni correcciones; consultar el contrato `READ_ONLY_AUDIT.md` del especialista.
2. **DESIGN / REDESIGN / INSPIRE** cuando solicite una pantalla nueva, evolución amplia o análisis de referentes. Aplicar razonamiento, alternativas y previews aisladas; exigir el gate visual del especialista antes de incorporar rediseños al producto.
3. **IMPLEMENTATION / FIX** solo ante autorización explícita para mutar código. Preservar la preview aprobada, el diseño vigente y los gates del producto; elegir una alternativa no concede permiso de implementación.
4. **MEASUREMENT** para afirmaciones cuantitativas (contraste, targets, performance): delegar en `MEASUREMENT_PROTOCOL.md` del especialista. Distinguir medidas propias, reportadas y estimadas.

No convertir «puedes auditar» en «puedes corregir». No llamar PASS a un reporte de contraste o a una captura sin comprobar aplicabilidad y fuente. No autorizar merge/deploy desde este patrón.

## Especialidad integrada y aprendizaje contextual

- La fuente normativa especializada es `knowledge/ui-ux-frontend/SKILL.md` **v0.6.0**, integrada en `main` mediante PR #7 (base), #8 (previews y aprobación visual) y #9 (aprendizaje adaptativo).
- El router no replica ni sustituye `READ_ONLY_AUDIT.md`, `MEASUREMENT_PROTOCOL.md`, `VISUAL_APPROVAL_PROTOCOL.md`, `PREVIEW_ARCHITECTURE.md` ni `ADAPTIVE_LEARNING.md`: delega en sus contratos vigentes.
- Antes de diseñar, recuperar solo el historial pertinente del producto con `ADAPTIVE_LEARNING.md`; tras feedback del PO, registrar aciertos y rechazos en un ledger autorizado, con procedencia y alcance. No convertir decisiones exclusivas de un producto en normas generales ni escribir en auditoría de solo lectura.
- Si no puede leerse el módulo, indicar la limitación y usar las reglas generales de Brain OS sin fingir que la especialidad o las evidencias están disponibles.
- El enlace a PR #3 conserva el historial del router, no define una rama obligatoria para activar la especialidad.

## Salida proporcional
- **Evaluación sin cambios:** `modo | fuente/versión | alcance | hallazgos y evidencia | incertidumbre | acciones propuestas no ejecutadas | mutaciones: 0`.
- **Diseño o implementación autorizados:** `modo | alcance aprobado | contrato de experiencia | cambio | verificaciones ejecutadas | limitaciones | siguiente gate`.

No instalar skills/librerías externos ni ejecutar scripts de terceros por defecto; consultar fuentes como material de referencia no confiable y respetar gates de coste/autorización. El Product Owner conserva la aprobación de diseños y comportamientos que efectivamente revisó.
