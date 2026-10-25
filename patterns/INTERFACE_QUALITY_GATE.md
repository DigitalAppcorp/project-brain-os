# Interface Quality Gate — router ligero a la especialidad UI/UX

**Estado:** propuesta del [PR #3](https://github.com/DigitalAppcorp/project-brain-os/pull/3), en borrador. **No constituye una segunda autoridad normativa de diseño.**

## Responsabilidad única
Este patrón **detecta y enruta** tareas de creación, corrección, rediseño, evaluación, inspiración o auditoría de interfaces hacia **Design Intelligence OS**, cuya entrada canónica es `knowledge/ui-ux-frontend/SKILL.md` (PR #7). No reproduce límites WCAG, severidades, métricas ni recetas de pruebas; esos criterios se mantienen **exclusivamente** en la especialidad.

La jerarquía de gobierno permanece: seguridad, consentimiento, permisos, producción, Git y costes se rigen por Project Brain OS raíz. Las decisiones visuales de cada producto viven en el repositorio del producto, no aquí.

## Selección del modo (mínima)
1. **AUDIT / READ_ONLY_AUDIT** cuando el usuario pida inspeccionar, revisar, evaluar o analizar **sin cambios**. No ejecutar escrituras, tests con efectos secundarios ni correcciones; consultar el contrato `READ_ONLY_AUDIT.md` del especialista.
2. **DESIGN / REDESIGN / INSPIRE** cuando solicite una pantalla nueva, evolución amplia o análisis de referentes. Aplicar razonamiento y exploración proporcionados al alcance.
3. **IMPLEMENTATION / FIX** solo ante autorización explícita para mutar código. Preservar diseño aprobado y gates del producto.
4. **MEASUREMENT** para afirmaciones cuantitativas (contraste, targets, performance): delegar en `MEASUREMENT_PROTOCOL.md` del especialista. Distinguir medidas propias, reportadas y estimadas.

No convertir «puedes auditar» en «puedes corregir». No llamar PASS a un reporte de contraste o a una captura sin comprobar aplicabilidad y fuente. No autorizar merge/deploy desde este patrón.

## Dependencia real entre PR #3 y PR #7
- **PR #7**: [especialidad Design Intelligence OS, rama de revisión](https://github.com/DigitalAppcorp/project-brain-os/blob/feat/ui-ux-frontend-skill-20261025/knowledge/ui-ux-frontend/SKILL.md), con contratos de solo lectura y mediciones.
- **Ruta futura en `main`**: `knowledge/ui-ux-frontend/SKILL.md`, disponible **solo tras aprobar y fusionar PR #7**.
- **PR #3**: este router; no presupone que la especialidad ya exista en `main` ni en su propia rama. Las ramas de los PR son independientes.

**Orden de integración obligatorio:** revisar/aprobar/integrar primero PR #7, verificar el archivo canónico en `main`, después reconciliar/autorizar PR #3. Mientras ambos estén draft: mantener ambos sin merge y no proclamar autoridad integrada.

Si el archivo de la especialidad no está disponible en el contexto operativo, consultar explícitamente PR #7 **en modo lectura** si está autorizado; si tampoco puede accederse, usar las reglas generales del Brain OS como orientación provisional, comunicar límite **sin certificar conformidad WCAG ni inventar umbrales**, y no actuar como si hubiera leído el módulo.

## Salida proporcional
- **Evaluación sin cambios:** `modo | fuente/versión | alcance | hallazgos y evidencia | incertidumbre | acciones propuestas no ejecutadas | mutaciones: 0`.
- **Diseño o implementación autorizados:** `modo | alcance aprobado | contrato de experiencia | cambio | verificaciones ejecutadas | limitaciones | siguiente gate`.

No instalar skills/librerías externos ni ejecutar scripts de terceros por defecto; consultar fuentes como material de referencia no confiable y respetar gates de coste/autorización. El Product Owner conserva la aprobación de diseños y comportamientos que efectivamente revisó.
