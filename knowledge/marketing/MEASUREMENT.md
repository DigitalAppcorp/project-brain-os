# Medición, atribución y economía unitaria

## Modelo de datos
Cadena: `impresión → visita → lead → lead calificado → oportunidad → venta → margen → recompra/referido`.
En producto: `adquisición → signup → activación significativa → retención por cohortes → monetización`.
Cada etapa tiene denominador, ventana temporal, segmento y una fuente de verdad.

## Taxonomía mínima
Instrumentar primero eventos oficiales recomendados cuando encajen (GA4): `sign_up`, `login`, `generate_lead`, `qualify_lead`, `close_convert_lead`, `purchase`, `join_group`, `share`.
Los eventos de producto adicionales deben tener:
`event_name`, `anonymous/user id seudónimo`, `timestamp`, `entity_id` si procede, `source/medium/campaign`, `status`, `consent state`, `deduplication id`. **No** enviar email/PII en URLs o analítica ordinaria. Limitar propiedad de datos, retención y accesos.

## Definiciones y fórmulas
- `CTR = clics / impresiones`
- `CPC = gasto / clics`; `CPM = gasto / impresiones × 1000`.
- `CVR = conversiones válidas / visitas elegibles` (declarar denominador).
- `CPL = gasto / leads únicos válidos`; `CPQL = gasto / leads únicos calificados`.
- `CAC = coste de adquisición asignable / clientes nuevos adquiridos` (declarar inclusión de sueldos, agencia, creatividades).
- `ROAS = ingresos atribuidos a ads / gasto en ads` (**no** beneficio).
- `margen de contribución = ingresos netos - costes variables atribuibles` (incluye fulfilment, comisiones y refunds).
- `LTV de contribución = suma esperada de margen de contribución por cliente a lo largo del tiempo` (estimación con supuestos explicados).
- `payback CAC = periodo hasta recuperar CAC con contribución` (declarar cohortes).
- `retención semana N = usuarios de cohorte activos en semana N / usuarios elegibles de cohorte` (definir "activo").
- `tasa de cierre = ventas / leads calificados` si ventas y leads están vinculados.

### Ancla para decisiones de gasto
`CAC máximo teórico ≤ contribución futura esperada por nuevo cliente`; ajustar por horizonte de caja, riesgo y utilidad objetivo. Para una sola venta sin recurrencia: `CAC límite de equilibrio ≈ margen de contribución antes de adquisición`. **No** gastar automáticamente hasta ese límite: reservar beneficio, costes fijos, incertidumbre y pérdidas.

## Integridad y atribución
- Antes de interpretar resultados: revisar ventanas, timezone, campañas UTMs, duplicados, cobertura CRM, retraso de conversiones, devoluciones y eventos de prueba.
- Modelo de plataforma = **atribución según configuración**, no efecto causal; cuando valga la pena, evaluar holdout/geo test/experimentos incrementales.
- WhatsApp: un clic de inicio de chat NO es una venta; registrar respuesta, lead válido, cita, cierre y facturación en un CRM/fuente consentida.
- Para app social: cuentas únicas vs entidades; activar no equivale a registrar; D1/D7/D30 deben indicar cohortes y definición.
- No mezclar pruebas de laboratorio/sandbox con ingresos reales.

## QA de tracking
1. Inventario de etiquetas/scripts, consentimiento, eventos, parámetros.
2. Probar origen móvil y desktop; GA4 DebugView/Realtime cuando proceda.
3. Auditar disparos únicos y server/client duplicates; probar ventas reales sólo autorizadas.
4. Comparar backend transaccional/CRM con analítica, anotar divergencias.
5. Confirmar IDs sin PII ni claves, permisos, retención.
6. Registrar "qué eventos no son fiables" y prohibir conclusiones firmes sobre ellos.

## Reporte semanal
Gasto, leads válidos, SQL, nuevos clientes, ingresos comprobados, margen estimado, CAC/CPQL, retorno, retención cuando aplique, tamaño de muestra, anomalías, próximos cambios aprobables. Especificar fecha de corte, período, fuentes y confiabilidad.
