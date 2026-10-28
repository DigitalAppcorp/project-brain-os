# Quality gates — contratos comprobables

## Modos y autoridad (v0.6.0)
- **AUDIT / READ_ONLY_AUDIT**: leer y evaluar sin modificar; contrato en [READ_ONLY_AUDIT.md](READ_ONLY_AUDIT.md). No aplicar automaticamente Implementation Ready ni VISUAL-AND-UX-ACCEPTED; informar capacidad de evaluación y cobertura.
- **IMPLEMENTATION**: solo con autorización explícita adicional. Este modo aplica QA de cambios y el contrato del Project Brain OS raíz. El permiso de auditar **no** autoriza implementar.
- **MEDICIONES**: usar [MEASUREMENT_PROTOCOL.md](MEASUREMENT_PROTOCOL.md) como formato único; evitar reglas numéricas duplicadas o umbrales inventados.
- El patrón `patterns/INTERFACE_QUALITY_GATE.md` integrado en `main` es **router** del Brain OS raíz, no una segunda fuente normativa. Delega en esta especialidad v0.6.0 sin duplicar sus contratos.

## Regla superior
Estos gates **complementan** Gates 0–9 y Scope Closure Reconciliation del Project Brain OS raíz. No autorizan merge ni despliegue ni sustituyen decisiones de producto del PO. La revisión estética del PO aplica al carril definido por el protocolo, no a toda UI nueva. No confundir documento aprobado, código presente, test ejecutado, aceptación visual y producción.

## Estados separados
- **SPECIFIED**: alcance, comportamiento, criterios y estados documentados.
- **IMPLEMENTED**: código presente en rama identificada, sin inferir runtime.
- **AUTOMATED_PASS**: pruebas identificadas, salida reproducible y commit; indicar cobertura.
- **MANUAL_PASS**: escenarios/dispositivos identificados, persona/evidencia; no generalizar cobertura.
- **DESIGN_QA_PASS**: revisión profesional interna de composición y estados, crítica adversarial y correcciones verificadas según protocolo; no se deduce de CI.
- **PO_VISUAL_ACCEPTED**: superficies realmente aceptadas por PO con fuente/alcance; NOT_REQUESTED para UI nueva ordinaria autorizada. El estado histórico VISUAL_ACCEPTED no se infiere de QA interna.
- **RELEASED**: despliegue y comprobación en entorno correspondiente, con autorización si aplica.
- **BLOCKED / NOT_TESTED / INCONCLUSIVE**: distinguir fallos, no ejecución y resultado incierto.
Estos estados pueden coexistir parcialmente; no son una escalera que elimine los anteriores.

## Gate UX-SPEC
Condiciones mínimas: tarea y usuario, limitaciones, flujo principal, casos vacío/espera/error/éxito, permiso y retorno; jerarquía y dirección visual aprobadas cuando proceda; métricas definidas; riesgos y requisitos accesibles identificados.
Resultado: APPROVED / NEEDS_REVISION / BLOCKED + evidencia. No exigir investigación exhaustiva para un cambio cosmético inocuo.

## Gate previo de diseño visual
Antes de cerrar UI aplicar [VISUAL_APPROVAL_PROTOCOL.md](VISUAL_APPROVAL_PROTOCOL.md) y enlazar el registro de decisiones: UI nueva autorizada exige gate profesional autónomo; rediseño dirigido por PO conserva el gate de su intención aceptada. Autorización de implementación vigente siempre separada. Una selección de alternativa o permiso de auditoría no autoriza transferir cambios. No convertir toda pieza nueva en una solicitud de aprobación estética.

## Gate ENGINEERING-READY
- Diff del alcance, estado y contratos backend evaluados; riesgos de regresión.
- Compilación/lint/unit y e2e **realmente ejecutados cuando aplican**, salidas verificables.
- 1 camino feliz + 1 error significativo + reintentos/doble envío y respuesta obsoleta para mutaciones relevantes.
- Estados de usuario y permisos revisados por backend; no marcar éxito antes de verdad autoritativa.
- Responsive, scroll, teclado/foco y accesibilidad automatizada/manual según riesgo.
- Si la herramienta o entorno no permite una prueba, anotarla como NOT_TESTED; decidir si bloquea según riesgo.

## Gate visual y UX (dos decisiones separadas)
- Comparación referencia ↔ dirección seleccionada identificada por versión ↔ ejecución actual; usar evidencia aprobada cuando corresponda al carril, conforme a [VISUAL_APPROVAL_PROTOCOL.md](VISUAL_APPROVAL_PROTOCOL.md).
- Capturas completas realmente inspeccionadas por viewport/idioma/estado pertinente, prueba de scroll/interacción y crítica adversarial con fallos/correcciones observables; la fuente normativa de criterios es el protocolo, no otra checklist aquí.
- DESIGN_QA_PASS es interno; PO_VISUAL_ACCEPTED solo acredita lo que el PO revisó y aceptó. Para UI nueva ordinaria, no exigir su inspección estética como gate. Ninguna decisión estética acredita seguridad, backend ni autoriza release.
- Si se detecta S3/S4 abierto, bloquear el alcance afectado salvo mitigación documentada y autorizada donde sea seguro/legal.

## Auditoría WCAG-EM 2.0 (cuando se evalúe conformidad formal)
W3C Group Note de 23-07-2026, **metodología** y NO criterio WCAG nuevo:
1. Definir alcance del producto, versiones, plataformas, criterios y límites.
2. Explorar producto y tecnologías; identificar tipos de vistas, estados y flujos.
3. Seleccionar muestra representativa de pantallas, patrones, estados, procesos completos y excepciones; justificar sesgo.
4. Evaluar muestra respecto a criterios aplicables, con métodos automáticos y manuales.
5. Reportar hallazgos, cobertura, excepciones, nivel de confianza y conclusiones de alcance **sin certificar lo no evaluado**.
Para auditoría rápida usar subconjunto **etiquetado**, no afirmar conformidad total por una revisión muestral improvisada.
Fuente: https://www.w3.org/TR/wcag-em-2/

## Matriz mínima por riesgo
| Tipo de cambio | Pruebas proporcionadas |
| --- | --- |
| Texto, icono, color | visual en estados afectados + contraste/nombre accesible si cambia |
| Navegación/layout | móvil/desktop cuando aplique + teclado/foco + atrás/scroll |
| Fetch/lista | vacío/loading/error/reintento/permiso + no saltos de layout |
| Mutación | éxito real/error/red lenta/doble tap/obsolescencia/autorización |
| Pagos/seguridad | autorizaciones backend, idempotencia, sandbox y rollback de UI; comprobación autorizada de producción solo cuando proceda |

## Registro de mediciones y cobertura
Si el caso reclama un criterio medible, adjuntar la ficha de [MEASUREMENT_PROTOCOL.md](MEASUREMENT_PROTOCOL.md), distinguiendo resultados `MEASURED / REPORTED / CODE_INSPECTED / ESTIMATED / NOT_TESTED`. No transformar un reporte ajeno en medición propia. Si falta evidencia obligatoria, `INCONCLUSIVE` o `NOT_TESTED`, sin certificar.
En READ_ONLY_AUDIT, la salida contiene hallazgos y recomendaciones, **ningún cambio ejecutado ni aceptación de implementación**.

## Reporte de gate
`Scope | Ref commit/branch | Dispositivos | Pruebas ejecutadas (nombre+salida) | No ejecutadas | S3/S4 abiertos | A11y cobertura | Visual PO | Regresiones | Decisión | Próxima acción`.

### Decisión
- **PASS**: únicamente para criterios probados.
- **CONDITIONAL**: resultado parcial con pruebas pendientes no bloqueantes y responsabilidad/fecha; no llamar «completado».
- **BLOCKED**: incumplimiento importante o incertidumbre crítica.
- **NOT_EVALUATED**: sin evidencia. Nunca convertir ausencia de defectos reportados en PASS.

Nunca declarar «accesible» porque axe arroja cero violaciones. Véase [TEST_RECIPES.md](TEST_RECIPES.md).

## Gates transversales v0.3.0
**AUDIENCE-PASS:** para copy nuevo o modificado, registrar destinatario, propósito, verdad del negocio, estado de tarea y revisión de filtración según [AUDIENCE_BOUNDARY.md](AUDIENCE_BOUNDARY.md) y [UX_CONTENT.md](UX_CONTENT.md). No marcar PASS si solo contiene «textos técnicos eliminados»: el contenido contractual necesario debe permanecer.

**INTENT-PASS:** cuando hay cambios sobre UI existente, identificar invariantes desde [DESIGN_MEMORY.md](DESIGN_MEMORY.md); ejecutar delta y prueba de preservación según [CHANGE_INTEGRITY.md](CHANGE_INTEGRITY.md). Una pantalla puede tener build PASS y fallar fidelidad/tono.

**CONTEXTUAL-DESIGN:** para diseño nuevo amplio o rediseño, justificar por qué jerarquía/composición/patrón corresponden al público y al producto; explorar alternativas **solo si aporta valor**. Una propuesta de «3 estilos» que cambia únicamente colores no demuestra exploración, ni una pantalla diferente demuestra por sí sola originalidad.

**REFERENCE-VALIDITY:** al analizar un producto externo, separar observación de hipótesis; no inferir interacción/velocidad desde capturas. Transferir principios, no identidad visual.

### Informe final de habilidades
Añadir a la ficha de QA: `audiencia del copy | decisiones DIR | delta aprobado | invariantes probados | referencias y fecha | razón de composición | pruebas NO ejecutadas`. El nivel de detalle escala con el riesgo, no con el número de archivos de la habilidad.

## Recuperación y feedback contextual (v0.6)
Para diseño/implementación visual, enlazar aprendizajes pertinentes recuperados y límites; después de feedback, eventos registrados en ubicación autorizada según [ADAPTIVE_LEARNING.md](ADAPTIVE_LEARNING.md). Si no existe historial o no puede leerse, declararlo sin inventarlo. No bloquear una consulta trivial por ausencia de ledger ni elevar pesos a autorización; mantener todos los gates visuales anteriores.
