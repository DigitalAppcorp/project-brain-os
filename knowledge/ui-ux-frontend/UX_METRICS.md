# Métricas UX y evidencia causal

## Contrato de medición
Cada objetivo debe declarar:
`Población | Tarea | Evento inicial | Evento de éxito | Denominador | Ventana temporal | Segmentos | Exclusiones | Fuente | Línea base | Umbral/hipótesis | Método | Limitaciones`.
Si algún campo esencial se desconoce, NO inventar cifras. «Sin medición» no significa «0».

## Métricas para tarea
- **Task success rate**: tareas completadas autónomamente / intentos válidos. Separar completadas con ayuda.
- **Abandono**: intentos iniciados sin evento final dentro de ventana razonable; estimar errores de telemetría y tareas abandonadas deliberadamente.
- **Error de tarea**: clase de error / oportunidades o intentos comparables; catalogar definiciones.
- **Tiempo por tarea**: desde disparador observable hasta confirmación; medianas/dispersión y condiciones de red, no promedios engañosos.
- **Retrabajo**: volver a una pantalla, repetir pasos o necesitar soporte, según contexto.
- **Accesibilidad**: cobertura de flujos/criterios/dispositivos evaluados y hallazgos abiertos; no comprimir en una supuesta «puntuación WCAG» universal.
- **Visual quality**: divergencias respecto a referencias aprobadas por prioridad; la estética no se vuelve «objetiva» por asignarle un número.

## Rendimiento
Para web real, comprobar LCP, INP y CLS en p75 y segmentar móvil/desktop cuando los datos lo permitan. Objetivos orientativos según web.dev: LCP ≤2.5s, INP ≤200ms, CLS ≤0.1. Datos de laboratorio no equivalen a RUM ni autorizan afirmar cumplimiento de percentil real.
No perseguir performance a costa de mostrar estados engañosos. Medir primer feedback interactivo y bloqueos del flujo cuando sea pertinente.

## Funnel correcto
Ejemplo para una operación legítima:
`expuesto → inició → validó → envió → confirmó servidor → resultado mostrado`.
No equiparar `click` con transacción exitosa. Guardar condiciones de exclusión: QA, bots, duplicados, permiso, región, errores externos. No recoger PII innecesaria ni registrar secretos/tokens.

## Diseño de experimento
1. Formular hipótesis con mecanismo plausible.
2. Definir métrica principal, guardrails de integridad/accesibilidad y umbral **antes** de la prueba.
3. Medir línea base y variación con mismo periodo/segmentos comparables.
4. Para causalidad fuerte, aleatorización y muestra/potencia cuando sea viable; si no, etiquetar observacional.
5. Registrar resultados con incertidumbre y limitaciones; no extrapolar estudio de e-commerce a todas las apps.
6. Decidir mantener/revertir/iterar/seguir midiendo y actualizar evidencia.

## Revisión de datos
- Asegurar identificadores consistentes, eventos idempotentes y zonas horarias explícitas.
- Telemetría de éxito real emitida tras confirmación autoritativa cuando aplique.
- No perseguir más clics si empeora confianza, errores, retención o cancelación.
- Segmentos pequeños: no presentar diferencias accidentales como hallazgos concluyentes.

## Mini-ficha
`Cambio:` ___
`Problema observado:` ___
`Hipótesis:` ___
`Métrica principal / denominador:` ___
`Línea base (o desconocida):` ___
`Exclusiones:` ___
`Evidencia (URL/fecha/método):` ___
`Resultado:` medido / sin medición / inconcluso
`Decisión y gate:` ___

Fuentes complementarias: [UX_RESEARCH.md](UX_RESEARCH.md), https://web.dev/articles/vitals y https://www.nngroup.com/articles/ux-research-cheat-sheet/.
