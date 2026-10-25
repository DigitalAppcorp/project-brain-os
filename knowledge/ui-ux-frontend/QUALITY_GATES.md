# Quality gates — contratos comprobables

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

## Gate ENGINEERING-READY
- Diff del alcance, estado y contratos backend evaluados; riesgos de regresión.
- Compilación/lint/unit y e2e **realmente ejecutados cuando aplican**, salidas verificables.
- 1 camino feliz + 1 error significativo + reintentos/doble envío y respuesta obsoleta para mutaciones relevantes.
- Estados de usuario y permisos revisados por backend; no marcar éxito antes de verdad autoritativa.
- Responsive, scroll, teclado/foco y accesibilidad automatizada/manual según riesgo.
- Si la herramienta o entorno no permite una prueba, anotarla como NOT_TESTED; decidir si bloquea según riesgo.

## Gate VISUAL-AND-UX-ACCEPTED
- Comparación referencia ↔ estado aprobado ↔ ejecución actual.
- Captura por viewport/tema/estado relevante; prueba manual del scroll/interacción en flujo significativo.
- PO acepta solo lo que revisó; aceptación estética ≠ seguridad ni funcionamiento backend.
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

## Reporte de gate
`Scope | Ref commit/branch | Dispositivos | Pruebas ejecutadas (nombre+salida) | No ejecutadas | S3/S4 abiertos | A11y cobertura | Visual PO | Regresiones | Decisión | Próxima acción`.

### Decisión
- **PASS**: únicamente para criterios probados.
- **CONDITIONAL**: resultado parcial con pruebas pendientes no bloqueantes y responsabilidad/fecha; no llamar «completado».
- **BLOCKED**: incumplimiento importante o incertidumbre crítica.
- **NOT_EVALUATED**: sin evidencia. Nunca convertir ausencia de defectos reportados en PASS.

Nunca declarar «accesible» porque axe arroja cero violaciones. Véase [TEST_RECIPES.md](TEST_RECIPES.md).
