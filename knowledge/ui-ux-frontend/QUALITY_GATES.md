# Quality gates — contratos comprobables

## Modos y autoridad (v0.4.0)
- **AUDIT / READ_ONLY_AUDIT**: leer y evaluar sin modificar; contrato en [READ_ONLY_AUDIT.md](READ_ONLY_AUDIT.md). No aplicar automaticamente Implementation Ready ni VISUAL-AND-UX-ACCEPTED; informar capacidad de evaluación y cobertura.
- **IMPLEMENTATION**: solo con autorización explícita adicional. Este modo aplica QA de cambios y el contrato del Project Brain OS raíz. El permiso de auditar **no** autoriza implementar.
- **MEDICIONES**: usar [MEASUREMENT_PROTOCOL.md](MEASUREMENT_PROTOCOL.md) como formato único; evitar reglas numéricas duplicadas o umbrales inventados.
- El patrón básico `patterns/INTERFACE_QUALITY_GATE.md` es **router** del Brain OS raíz, no una segunda fuente normativa. Referencia cruzada por PR #3 a este módulo v0.4.0 (PR #7); ningún PR está en `main` hasta merge aprobado.

## Regla superior
Estos gates **complementan** Gates 0–9 y Scope Closure Reconciliation del Project Brain OS raíz. No autorizan merge ni despliegue y no sustituyen la aprobación del Product Owner. No confundir documento aprobado, código presente, test ejecutado, aceptación visual y producción.

## Estados separados
- **SPECIFIED**: alcance, comportamiento, criterios y estados documentados.
- **IMPLEMENTED**: código presente en rama identificada, sin inferir runtime.
- **AUTOMATED_PASS**: pruebas identificadas, salida reproducible y commit; indicar cobertura.
- **MANUAL_PASS**: escenarios/dispositivos identificados, persona/evidencia; no generalizar cobertura.
- **VISUAL_ACCEPTED**: superficies realmente revisadas por PO conforme al alcance.
- **RELEASED**: despliegue y comprobación en entorno correspondiente, con autorización si aplica.
- **BLOCKED / NOT_TESTED / INCONCLUSIVE**: distinguir fallos, no ejecución y resultado incierto.
Estos estados pueden coexistir parcialmente; no son una escalera que elimine los anteriores.

## Gate UX-SPEC
Condiciones mínimas: tarea y usuario, limitaciones, flujo principal, casos vacío/espera/error/éxito, permiso y retorno; jerarquía y dirección visual aprobadas cuando proceda; métricas definidas; riesgos y requisitos accesibles identificados.
Resultado: APPROVED / NEEDS_REVISION / BLOCKED + evidencia. No exigir investigación exhaustiva para un cambio cosmético inocuo.

## Gate previo de diseño visual
Antes de IMPLEMENTATION para UI aplicar [VISUAL_APPROVAL_PROTOCOL.md](VISUAL_APPROVAL_PROTOCOL.md) y enlazar el registro de decisiones. UX-SPEC referencia ese resultado: propuesta presentada, preview final aprobada cuando sea significativa y autorización de implementación vigente. Una selección de alternativa sola mantiene bloqueada la transferencia al producto. El modo proporcional del protocolo evita pedir aprobaciones técnicas ordinarias o repetir las ya vigentes.

## Gate ENGINEERING-READY
- Diff del alcance, estado y contratos backend evaluados; riesgos de regresión.
- Compilación/lint/unit y e2e **realmente ejecutados cuando aplican**, salidas verificables.
- 1 camino feliz + 1 error significativo + reintentos/doble envío y respuesta obsoleta para mutaciones relevantes.
- Estados de usuario y permisos revisados por backend; no marcar éxito antes de verdad autoritativa.
- Responsive, scroll, teclado/foco y accesibilidad automatizada/manual según riesgo.
- Si la herramienta o entorno no permite una prueba, anotarla como NOT_TESTED; decidir si bloquea según riesgo.

## Gate VISUAL-AND-UX-ACCEPTED
- Comparación referencia ↔ preview aprobada identificada por versión ↔ ejecución actual; procedimiento en [PREVIEW_ARCHITECTURE.md](PREVIEW_ARCHITECTURE.md).
- Captura por viewport/tema/estado relevante; prueba manual del scroll/interacción en flujo significativo.
- PO acepta solo lo que revisó; registrar aceptación de implementación separada de aprobación de preview conforme a [VISUAL_APPROVAL_PROTOCOL.md](VISUAL_APPROVAL_PROTOCOL.md). Aceptación estética ≠ seguridad ni funcionamiento backend.
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
