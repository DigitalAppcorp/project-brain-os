# Investigación UX, arquitectura de información y métricas

## Antes del pixel
Definir **persona situacional** (no estereotipo demográfico), tarea, motivación, contexto de uso, riesgo y criterio de éxito. Especificar quién puede quedar excluido: uso con una mano, tamaño de texto aumentado, poca conectividad, baja familiaridad, lectores de pantalla, movilidad reducida.

## Métodos según incertidumbre
- **No sabemos qué problema resolver**: entrevista contextual y observación de tareas reales; síntesis de necesidades, no feature-request literal.
- **No sabemos cómo organizar información**: card sorting y tree testing; comparar términos con modelos mentales.
- **No sabemos por qué falla una pantalla**: test de usabilidad moderado/no moderado por tareas y revisión heurística.
- **No sabemos dónde cae el funnel**: telemetría agregada (exposición, acción, éxito, error, abandono, tiempo); comprobar calidad del tracking.
- **No sabemos qué opción supera a otra**: prototipos comparados y, si hay muestra/potencia suficientes, experimento controlado.
- **No sabemos si usuarios vuelven**: análisis por cohortes, métricas de activación y retención sin confundir frecuencia con valor.

Investigación cualitativa descubre mecanismos y patrones, no estima prevalencia poblacional; medición cuantitativa estima magnitudes con incertidumbre. La revisión heurística no sustituye observar usuarios.

## Formulación de tareas
Usar escenario realista, neutral y evaluable: «Encuentra un lugar apropiado para tu mascota, comprueba cómo llegar y vuelve al mapa». No dirigir al usuario por etiquetas («toca el icono verde»).

Registrar por participante: completó sin ayuda, errores, desvíos, tiempo (si relevante), momentos de confusión, comentarios, medio de acceso y contexto. Distinguir capacidad de uso autónoma frente a «lo completó con pista».

## Diseño de flujo
Por cada tarea documentar:
1. Punto de entrada y expectativa.
2. Información que necesita para decidir.
3. Acción primaria y secundarias; rutas de retorno.
4. Estados de espera y feedback.
5. Alternativas: cancelar, editar, reintentar, deshacer.
6. Dependencias: login, ubicación, permisos, red, elegibilidad.
7. Errores y resolución sin pérdida de datos.
8. Señal de resultado exitoso y forma de verificarlo.

No obligar a recordar información visible en otra pantalla. Mantener consistencia de términos y continuidad entre pasos.

## Investigación a escala MVP
Formar hipótesis explícita, prototipo de bajo coste y 3–5 tareas críticas. Un grupo pequeño de participantes puede revelar fallos cualitativos relevantes; no usarlo como respaldo de porcentajes universales. Incluir perfiles con necesidades de accesibilidad cuando corresponda. Priorizar por severidad observada, recurrencia y coste de corregir.

## Instrumentación mínima
- **Tasa de éxito por tarea**: tareas completadas autónomamente / intentos válidos.
- **Tasa de error**: errores de tarea / intentos comparables, con definición clara.
- **Tiempo y pasos por tarea**: según complejidad, comparando medianas/distribución si la muestra lo permite.
- **Funnel**: usuarios expuestos → intención → ejecución → confirmación real.
- **Retención**: retorno con acción de valor, no solo abrir aplicación.
- **Quejas/reintentos/abandonos**: desglosar por dispositivo, tamaño, red y versión.
Excluir cuentas QA o instrumentación interna cuando se mida adopción real; documentar denominador, ventanas, origen y privacidad.

## Sesgos que evitar
- Pedir a usuarios si «les gusta» sustituye mal a ver si logran una tarea.
- Interpretar clics en anuncios o botones de «próximamente» como uso confirmado.
- Optimizar microconversiones sin medir éxito final ni confianza.
- Extrapolar desde un único viewport, idioma, modelo de celular o administrador.
- Confundir satisfacción post-demo con accesibilidad o robustez.

## Entregable de investigación
Problema, método, muestra/segmento, observaciones, evidencia cruda localizada, limitaciones, hallazgos por severidad, oportunidades, hipótesis y siguiente prueba. Una recomendación sin evidencia debe aparecer como **hipótesis**, no como hecho.