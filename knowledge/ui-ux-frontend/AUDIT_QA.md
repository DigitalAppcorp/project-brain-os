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
- **S0 — No es un defecto de usabilidad**: conclusión sustentada de evaluación/desacuerdo con que exista el problema, según inspiración de NN/g. **NO** significa «no reproducido». S0 no invalida reporte de anomalía técnica aún pendiente.

Evaluar **frecuencia + impacto + persistencia**, riesgo de accesibilidad/integridad, alcance y coste; no degradar automáticamente un problema de cumplimiento por ocurrir en pocos usuarios.

**Cuatro dimensiones separadas y obligatorias:**
1. **Severidad**: S0–S4 o **SIN_DETERMINAR** (si no hay evidencia suficiente).
2. **Estado del incidente**: REPORTED, NEEDS_REPRO, REPRODUCED, INVESTIGATING, FIXED_PENDING_VERIFICATION, VERIFIED_FIXED, REJECTED_WITH_EVIDENCE. «No reproducido» = NEEDS_REPRO/INVESTIGATING, nunca S0 automático.
3. **Confianza**: alta / media / baja + fuente de evidencia.
4. **Estado de prueba**: PASS / FAIL / NOT_TESTED / INCONCLUSIVE, ligado a commit, dispositivo y caso de prueba.

Cuando el riesgo es alto y falla la reproducción, conservar incidente abierto, capturar logs y determinar bloqueo según riesgo, no cerrar por ausencia de reproducción.

## Orden de prioridad
P0 corregir bloqueo y corrupción. P1 proteger tareas y accesibilidad. P2 corregir fricción frecuente. P3 pulido. No empezar una nueva capa visual cuando el flujo anterior tiene un defecto S3–S4 activo.

## Auditoría basada en evidencias
Por hallazgo documentar:
- ID, área/flujo, escenario y precondiciones.
- Comportamiento esperado vs observado y evidencia (captura, traza, DOM, ticket o test).
- Norma/heurística/estudio/hipótesis aplicable.
- Severidad (o SIN_DETERMINAR), estado del incidente, confianza, frecuencia conocida/desconocida y estado de prueba.
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

## Quality gates ejecutables
La autoridad técnica sobre criterios de aceptación, pruebas de riesgo, seguimiento de escenarios y evaluación WCAG-EM 2.0 se encuentra en [QUALITY_GATES.md](QUALITY_GATES.md). Para pruebas modelo, utilizar [TEST_RECIPES.md](TEST_RECIPES.md). Ningún gate autoriza modificar main o producción automáticamente.

## Tres Gates de esta especialidad
**UX-Spec**: intención, escenarios, diseño de estados, criterios de a11y y métricas; puede avanzar con hipótesis explícitas para MVP.

**Implementation Ready**: cambios en rama, pruebas ejecutadas y vinculadas a commit según el riesgo, fallos bloqueantes resueltos, accesibilidad técnica verificada; si no existen pruebas, marcar NOT_TESTED en vez de inferir PASS. «Pendiente visual» sigue pendiente.

**UX Accepted**: revisión visual/interactiva con evidencias o aceptación de PO para superficies aprobadas; la aceptación visual no sustituye pruebas de backend/permisos.

La fase solo termina conforme al **Scope Closure Reconciliation** del Brain OS raíz; si falta una prueba visual o un entregable acordado, indicarlo.

## Guía de revisión de capturas
Una captura permite observar layout, jerarquía, saturación, tipografía aparente, contraste aproximado y defectos de superposición. **No** permite certificar interacción, focus, responsive, persistencia, lector ni métricas. Formular preguntas o pruebas concretas sobre lo invisible, sin atribuir causas técnicas sin trazas.

## Guía ante retroalimentación crítica
Si usuario dice «no se ve como pedí», comparar explícitamente **referencia ↔ intención aprobada ↔ pantalla entregada**, localizar divergencias, corregir sistema/composición antes de retoques cosméticos y registrar nuevas pruebas. No defender un diseño por ser moderno ni inventar preferencias nuevas.
## Auditoría de contexto y deriva v0.3.0
En páginas generadas desde briefs y en cambios sobre productos existentes, aplicar revisión de cinco fallos:
1. **PROMPT-LEAK**: contenidos que describen instrucciones, tickets, mejoras de ingeniería o decisiones al PO sin razón para usuario.
2. **STRUCTURE-LEAK**: numeraciones, «capítulos» o indicadores de sección sin navegación, clasificación o secuencia real.
3. **TONE-DRIFT**: nuevos mensajes rompen voz/objetivo original, aun siendo verdaderos.
4. **SCOPE-DRIFT**: modificación funcional altera layout, copy, iconos o comportamiento no solicitados.
5. **TEMPLATE-FIXATION**: patrón formal impuesto a sector, audiencia y tamaño de módulo sin justificación.
Etiquetas de observación interna, **no diagnósticos clínicos ni categorías académicas confirmadas**. Documentar evidencia, severidad y alternativa; no prohibir patrones por el mero hecho de parecer comunes.

Complementos: [AUDIENCE_BOUNDARY.md](AUDIENCE_BOUNDARY.md), [CHANGE_INTEGRITY.md](CHANGE_INTEGRITY.md), [CREATIVE_EXPLORATION.md](CREATIVE_EXPLORATION.md) y [REFERENCE_ANALYSIS.md](REFERENCE_ANALYSIS.md).
