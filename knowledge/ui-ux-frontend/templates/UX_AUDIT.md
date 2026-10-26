# Plantilla — Auditoría UI/UX

**Modo:** READ_ONLY_AUDIT / IMPLEMENTATION_REVIEW
**Mutaciones autorizadas:** NO en READ_ONLY_AUDIT
**Producto / pantalla / versión / rama y SHA:**  
**Fecha / evaluador / dispositivos:**  
**Objetivo del usuario / tarea crítica:**  
**Fuentes de evidencia disponibles:** captura / código / runtime / test / usuario / telemetría  
**No observado / límites:**

**Recordatorio**: NEEDS_REPRO no implica S0; separar severidad, estado de incidente, confianza y PASS/FAIL/NOT_TESTED/INCONCLUSIVE. Registrar SHA, entorno y evidencia.

## Hallazgos — resumen
| ID | Pantalla/estado | Evidencia | Criterio | Severidad | Incidente | Confianza | Resultado |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UX-01 | | CODE_INSPECTED / REPORTED / MEASURED / ESTIMATED / NOT_TESTED | | S0–S4 / SIN_DETERMINAR | REPORTED / NEEDS_REPRO / REPRODUCED / etc. | alta / media / baja | PASS / FAIL / NOT_TESTED / INCONCLUSIVE |

## Ficha detallada por hallazgo (obligatoria para incumplimientos)
**ID / pantalla / selector / estado:**  
**Tarea, precondiciones y usuario final:**  
**Esperado / observado:**  
**Origen de evidencia:** MEASURED / REPORTED / CODE_INSPECTED / ESTIMATED / NOT_TESTED  
**Criterio aplicable:** documento + número + nivel + excepción revisada  
**Valor / unidad / umbral:**  
**Método, herramienta, versión y pasos:**  
**Enlace a traza/captura/DOM o líneas fuente:**  
**Repositorio / rama / SHA / entorno / URL / fecha:**  
**Dispositivo / navegador / viewport / zoom:**  
**Severidad / estado del incidente / confianza / resultado de prueba:**  
**Causa probable (hipótesis si procede):**  
**Solución propuesta (NO IMPLEMENTADA en auditoría):**  
**Prueba concreta de aceptación y cobertura no evaluada:**

Para cuantitativos y reglas, usar [MEASUREMENT_PROTOCOL.md](../MEASUREMENT_PROTOCOL.md) y [ACCESSIBILITY.md](../ACCESSIBILITY.md). Para auditoría sin cambios: [READ_ONLY_AUDIT.md](../READ_ONLY_AUDIT.md).

## Verificación por capas
- [ ] Valor y flujo principal
- [ ] Navegación y arquitectura de información
- [ ] Interacción/feedback/recuperación
- [ ] Jerarquía visual y tokens
- [ ] Mobile, safe-area, responsive, zoom y teclado virtual
- [ ] Teclado, lector de pantalla, labels, foco y contraste
- [ ] Estado asincrónico, error, vacío, datos y permisos
- [ ] Rendimiento y red real
- [ ] Regresión y pruebas
- [ ] Aceptación del Product Owner

## Recomendación final
**Acción prioritaria:**  
**Opciones consideradas y trade-offs:**  
**Qué evidencia falta:**  
**Gate**: UX-Spec / Implementation Ready / UX Accepted / BLOQUEADO  
**Próxima prueba concreta:**
**Mutaciones realizadas sobre el producto auditado:** 0 en READ_ONLY_AUDIT
**Permiso para implementar desde esta auditoría:** NO, requiere GO separado

_Nota: screenshot, test automatizado y aprobación estética son evidencias distintas._