# Integridad de cambios — proteger el contrato de experiencia

## Riesgo principal
Una corrección técnica puede introducir silenciosamente texto interno, composición nueva, alteración de tono, navegación distinta o pérdidas de accesibilidad. Que el fix pase tests unitarios NO garantiza preservar la experiencia aprobada.

## Contrato antes de editar
1. Recuperar rama, producto, pantalla, especificación, estados y decisiones vigentes en [DESIGN_MEMORY.md](DESIGN_MEMORY.md).
2. Declarar **cambio solicitado**, **superficie autorizada**, **invariantes** que deben sobrevivir y **dependencias**.
3. Clasificar la petición: visual, contenido, backend, seguridad, interacción, integración o mixta.
4. Determinar si el cambio exige nueva información pública; filtrarla con [AUDIENCE_BOUNDARY.md](AUDIENCE_BOUNDARY.md).
5. Seleccionar modificación mínima segura. No alterar decisiones visuales aprobadas por preferencia del implementador.

## Matriz de delta
| Plano | Qué puede cambiar | Qué se preserva por defecto |
| --- | --- | --- |
| Backend/integración | RPC, llamadas, autorización, idempotencia y errores | tono, copy público, diseño, navegación salvo necesidad real |
| Copy | frase indicada, corrección de hechos, etiqueta | estructura, estado funcional, política de pago |
| UI visual | layout/token/componente solicitado | acciones, contratos de datos, navegación, mensajes legales |
| Interacción | comportamiento solicitado y feedback necesario | estilo, contenido verificado, seguridad del backend |
| Rediseño integral aprobado | partes definidas del sistema | funciones, datos, roles y alcance no expresamente reemplazados |

**No interpretar «arregla el pago» como «explica los webhooks al usuario», ni «optimiza» como autorización para rediseñar todo.**

## Auditoría de diff
- **Semántica:** ¿se añadieron mensajes que reflejan el prompt o instrucciones al programador?
- **Diseño:** ¿cambió jerarquía, disposición, espacios, nombre de CTA, tamaño, contraste o motion?
- **Comportamiento:** ¿regresaron estados de error, foco, teclado, scroll, modal, permiso, navegación o rehidratación?
- **Integridad:** ¿el servidor confirma el estado? ¿cobros/roles/contadores tienen verdad autoritativa?
- **Alcance:** ¿cambios fuera del objetivo? Señalarlos, revertirlos o justificar necesidad antes de aceptar.

## Prueba de preservación (dual)
**Prueba A — objetivo nuevo:** ejecutar el caso que motivó el cambio; PASS solo con evidencia real.
**Prueba B — invariantes anteriores:** contrastar capturas/ejecución y estados contra baseline aprobado; anotar explícitamente divergencias. Si el alcance exige un cambio visual nuevo, presentarlo para aprobación y actualizar DIR.

Usar snapshots visuales bajo mismo contenido, viewport y condición; agregar tests de texto público y navegación crítica sin depender solo de snapshots. Seguir [TEST_RECIPES.md](TEST_RECIPES.md).

## Estados de revisión
`UNCHANGED_VERIFIED`, `CHANGED_APPROVED`, `CHANGED_UNAPPROVED`, `UNKNOWN_NOT_TESTED`.
No convertir «no observé regresiones» en verificación si no se ejecutó la prueba.

## Regla ante regresiones
S3/S4: detener nuevo alcance, estabilizar, reconstruir la causa con evidencia y corregir en rama. No defender la solución anterior por orgullo; registrar la lección generalizable sin trasladar secretos/detalles privados al OS.

## Contrato final de cambios
`Objetivo | archivos/estados tocados | invariantes probados | nuevo copy público y razón | decisiones afectadas | pruebas PASS/FAIL/NOT_TESTED | discrepancias | autorización | siguiente gate`.

## Comparación con preview aprobada
Antes de transferir al producto comprobar decisiones y versión en [VISUAL_APPROVAL_PROTOCOL.md](VISUAL_APPROVAL_PROTOCOL.md). Aplicar la comparación de [PREVIEW_ARCHITECTURE.md](PREVIEW_ARCHITECTURE.md) con contenido, estado y viewport equivalentes; enlazar baseline, captura implementada y diff de código. Registrar diferencias como intencionales autorizadas, deriva o no comprobadas. Si hay deriva significativa, restaurar la referencia o presentar el delta al PO; no actualizar el baseline para ocultarla.
