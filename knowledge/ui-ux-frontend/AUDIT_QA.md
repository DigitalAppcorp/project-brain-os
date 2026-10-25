# Auditoría UI/UX, severidad y Definition of Done

## Auditoría de siete capas
1. **Valor/tarea**: propósito, usuarios, recorrido, éxito, fricción y abandono.
2. **Arquitectura de información**: etiquetas, navegación, orden, encontrabilidad y reconocimiento.
3. **Interacción**: affordances, acciones, feedback, control/deshacer, incertidumbre, estados límite.
4. **Visual**: jerarquía, tipografía, color, espacio, consistencia, densidad, claridad en scroll.
5. **Inclusión**: semántica, teclado, lector, touch, contraste, zoom y motion.
6. **Ingeniería**: estado, carreras, datos autoritativos, error, permisos, seguridad, performance.
7. **Calidad real**: tests, dispositivos, telemetría, validación con usuarios, aceptación de PO.

## Severidad de hallazgos
Escala adaptada de NN/g; **no** es una norma ni promedio matemático automático:
- **S4 — Bloqueante/catastrófico**: tarea esencial imposible, pérdida de datos, daño potencial significativo, acción financiera incorrecta, barrera accesible crítica. Bloquear release afectado.
- **S3 — Alto**: fallo recurrente, tarea principal gravemente confusa o inaccesible, error sin recuperación. Corregir antes del release afectado salvo excepción documentada sin riesgo.
- **S2 — Medio**: fricción medible, inconsistencias y fallos de tareas secundarias con alternativa viable. Priorizar según impacto.
- **S1 — Bajo**: problemas de pulido/estética sin bloqueo. Corregir según beneficio y alcance.
- **S0 — No reproducido/no defecto**: documentar evidencia o desacuerdo.

Evaluar **frecuencia + impacto + persistencia**, riesgo de accesibilidad/integridad, alcance y coste; no degradar automáticamente un problema de cumplimiento por ocurrir en pocos usuarios. Anotar **confianza** (alta/mediana/baja) separada de severidad.

## Orden de prioridad
P0 corregir bloqueo y corrupción. P1 proteger tareas y accesibilidad. P2 corregir fricción frecuente. P3 pulido. No empezar una nueva capa visual cuando el flujo anterior tiene un defecto S3–S4 activo.

## Auditoría basada en evidencias
Por hallazgo documentar:
- ID, área/flujo, escenario y precondiciones.
- Comportamiento esperado vs observado y evidencia (captura, traza, DOM, ticket o test).
- Norma/heurística/estudio/hipótesis aplicable.
- Severidad, confianza y frecuencia conocida/desconocida.
- Causa probable (separar del síntoma).
- Solución mínima y opción alternativa, con trade-offs.
- Prueba de aceptación objetiva.
- Responsable/gate/estado final.

No afirmar «el contraste cumple» si no se midió; «no pude reproducir» no equivale a PASS; «las pruebas sintéticas pasan» no implica éxito en producción.

## Check de lanzamiento del flujo crítico
- [ ] Objetivo, usuario y escenario definidos.
- [ ] Estado inicial/normal/vacío/espera/error/éxito y cancelación especificados.
- [ ] La tarea principal se completa sin instrucciones externas.
- [ ] Back, refresh, doble tap y estado obsoleto no corrompen UI ni datos.
- [ ] Acción principal distinguible; controles tienen etiquetas y feedback.
- [ ] Componentes responsivos, sin recortes críticos ni overlays obstructivos.
- [ ] A11y WCAG relevante revisada con herramientas + teclado + manual.
- [ ] Rendimiento evaluado con datos disponibles; umbrales explícitos o pendiente.
- [ ] No regresión de rutas, roles, estado ni contenido previamente aprobado.
- [ ] Test e2e del escenario de éxito y al menos un error significativo.
- [ ] Revisión visual del Product Owner cuando aplica.
- [ ] Estado de implementación, staging, producción y aprobaciones separados.

## Tres Gates de esta especialidad
**UX-Spec**: intención, escenarios, diseño de estados, criterios de a11y y métricas; puede avanzar con hipótesis explícitas para MVP.

**Implementation Ready**: cambios en rama, código integrado, build/tests, bugs bloqueantes resueltos, verificación accesible técnica; «pendiente visual» sigue pendiente, no es completado.

**UX Accepted**: revisión visual/interactiva con evidencias o aceptación de PO para superficies aprobadas; la aceptación visual no sustituye pruebas de backend/permisos.

La fase solo termina conforme al **Scope Closure Reconciliation** del Brain OS raíz; si falta una prueba visual o un entregable acordado, indicarlo.

## Guía de revisión de capturas
Una captura permite observar layout, jerarquía, saturación, tipografía aparente, contraste aproximado y defectos de superposición. **No** permite certificar interacción, focus, responsive, persistencia, lector ni métricas. Formular preguntas o pruebas concretas sobre lo invisible, sin atribuir causas técnicas sin trazas.

## Guía ante retroalimentación crítica
Si usuario dice «no se ve como pedí», comparar explícitamente **referencia ↔ intención aprobada ↔ pantalla entregada**, localizar divergencias, corregir sistema/composición antes de retoques cosméticos y registrar nuevas pruebas. No defender un diseño por ser moderno ni inventar preferencias nuevas.