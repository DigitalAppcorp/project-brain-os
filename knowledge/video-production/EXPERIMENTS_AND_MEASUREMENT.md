# Laboratorio creativo: pruebas, evidencia y aprendizaje

## Fases de exploración

**Ronda 0: viabilidad técnica.** Buscar rutas capaces de producir **archivos originales de calidad aceptable**; el indicador es `PILOT_QA_PASS`, no likes imaginarios. Comparar gastos reales, tiempo, correcciones, derechos y calidad. Pueden evaluarse cuatro estilos sin publicar.

**Ronda 1: descubrimiento.** Uno o dos conceptos por estilo con mensaje/historia honestos. Son pruebas exploratorias: variarán estilo, gancho, contexto y ejecución. No adjudicar causalidad a «animación vs cine» solo por la diferencia de resultados.

**Ronda 2: contraste controlado.** Mantener lo más constante posible: audiencia, distribución, CTA, duración, ventana, oferta y tema; variar un aspecto (gancho, ruta, timing del producto, duración) y evaluar según muestras. Si no es posible controlar, reportar confusión causal.

## Métricas y fórmulas

| Nivel | Indicador | Denominador y cautela |
|---|---|---|
| Gancho | Reproducciones que alcanzan segundo 3 / reproducciones iniciadas | Solo cuando la plataforma entregue ambas definiciones; vistas y plays no son siempre equivalentes |
| Historia | Retención por segundo; finalizaciones / reproducciones elegibles | Definiciones distintas entre TikTok, Reels, YouTube |
| Resonancia | Compartidos / alcance; guardados / alcance | Likes = señal débil por sí solos |
| Intención | Clics salientes válidos / impresiones o alcance según objetivo | No confundir clic de plataforma y llegada comprobada en destino |
| Producto | Llegadas atribuidas a campaña, intentos de registro, cuentas verificadas, primera mascota, retorno | Unidades separadas: señales, solicitudes, personas elegibles; no reconstruir trayectorias anónimas |
| Eficiencia | Costo monetario y horas por video `PILOT_QA_PASS`; costos por acción si hay inversión autorizada | Una herramienta «gratis» puede requerir horas; no extrapolar muestras pequeñas |

No usar tasas cuando su numerador/denominador no son comparables. Sin muestra suficiente, marcar `INSUFFICIENT_DATA`. Nunca usar conversiones sintéticas para decisiones de inversión.

## Tarjeta de hipótesis antes de publicar

- Qué queremos averiguar, no qué resultado deseamos.
- Público real/idioma/canal.
- Identificador de pieza, fuente y parámetros válidos.
- Variable de la pieza y posibles factores de confusión.
- Métrica principal y complementarias, con denominador y ventana.
- Stop conditions (derechos, denuncias, coste, salud del producto, contenido engañoso).
- Interpretaciones alternativas si la pieza parece ganar.
- Decisión después del dato: producir variante / revisar historia / descartar / investigar de nuevo.

## Orden del análisis

1. Verificar que el archivo corresponde al contenido realmente publicado.
2. Comprobar período, gasto y alcance orgánico/pagado.
3. Evaluar **métricas creativas** primero: primeros segundos, retención, finalizaciones, compartidos.
4. Evaluar **métricas de negocio** solo donde existe enlace de atribución válido.
5. Verificar coherencia entre plataforma y producto, sin sumar poblaciones incompatibles.
6. Inspeccionar comentarios públicos sin inferir deseos de todo el mercado a partir de voces aisladas.
7. Formular 1–3 aprendizajes específicos con grado de confianza, contraejemplos y siguiente test.

## Fuente de criterio

Marketing Brain: `../marketing/SKILL.md`, `../marketing/MEASUREMENT.md` y `../marketing/templates/EXPERIMENT.md`. La fuente primaria y sus definiciones vigentes prevalecen sobre benchmarks y reglas genéricas.

Referencias oficiales a revalidar al publicar:
- TikTok Creative Best Practices: https://ads.tiktok.com/resources/help/article/creative-best-practices
- TikTok Creator Tips: https://newsroom.tiktok.com/5-tips-for-tiktok-creators?lang=en
- Meta for Business: https://www.facebook.com/business/ads (formato, distribución y políticas específicas deben comprobarse en la fecha de campaña).
