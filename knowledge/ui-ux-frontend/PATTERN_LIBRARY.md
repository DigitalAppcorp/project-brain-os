# Biblioteca de patrones UX/frontend — contexto antes que dogmas

Cada patrón es una **solución candidata**, no una orden de aplicarlo a todo producto. Antes de reutilizar: definir tarea, usuario, plataforma, fuente de verdad, estados, accesibilidad, fallos y aceptación; descartar si no encaja. Referencias a [TEST_RECIPES.md](TEST_RECIPES.md) y [QUALITY_GATES.md](QUALITY_GATES.md).

## 1. Formulario transaccional
**Problema**: datos incompletos o mal formateados. **Diseño**: etiqueta persistente, instrucciones, validación contextual, errores específicos, conservar entradas, resumen si muchos errores. **Ingeniería**: esquema compartido cuando sea viable, backend valida, no duplicar envíos, manejar timeout y reintento idempotente. **A11y**: label, aria-invalid/describedby, foco al resumen si aplica. **Pruebas**: campos vacíos, error de red, tab, zoom, reentrada, idioma largo. **Anti-patrón**: placeholder como única etiqueta o limpiar todo tras error.

## 2. Búsqueda + lista + mapa
**Problema**: localizar un lugar y acceder a detalles/ruta. **Diseño**: búsqueda visible, lista textual alternativa, selección sincronizada entre lista y mapa; «centrar», «ver detalle», «cómo llegar» y «check-in» distinguibles. **Ingeniería**: estado único de selección, respuesta de geocoding obsoleta ignorada, mapa con fallback, sin acceso obligatorio a GPS. **A11y**: lista navegable con teclado, nombre real de pines, targets y no depender de gesto. **Pruebas**: mapa en blanco, permiso denegado, sin resultados, pin superpuesto, conexión lenta y navegador externo. **Anti-patrón**: pin como único acceso a función crítica.

## 3. Panel administrativo
**Problema**: monitorear sistema y actuar. **Diseño**: KPIs fechados y definidos, errores prioritarios, filtros compartidos, tabla responsive accesible o drill-down en móvil. **Ingeniería**: permisos autoritativos en backend, paginación real, estado parcial y actualización visible. **A11y**: encabezados de tabla, orden explícito, avisos no solo color. **Pruebas**: 0 datos, muchas filas, sort/filter sin pérdida, roles, zoom. **Anti-patrón**: gráficos sin denominador ni periodo.

## 4. Membresía y pagos
**Problema**: usuario necesita comprar, cancelar o recuperar transacción. **Diseño**: precio/cadencia explícitos, estado «verificando» distinto de «sin membresía», prevención de doble compra y política clara de cancelación. **Ingeniería**: backend y proveedor son fuente de verdad; idempotencia, reconciliación; no acreditar derechos por clic, no bloquear cancelación por UX. **Pruebas**: abandono en proveedor, rechazo, respuesta tardía, webhook retrasado, vuelta a PWA, sesión expirada y reintento. **Anti-patrón**: botón «pagar» durante consulta desconocida o éxito optimista no confirmado.

## 5. Feed social / interacciones
**Problema**: like, guardar, seguir, paginar sin saltos. **Diseño**: feedback rápido, recuperación si falla y estado estable en navegación. **Ingeniería**: decidir rollback o reconciliación de UI optimista; dedupe/idempotencia; cursor paginado estable, claves de lista consistentes y prevención de race; contador autoritativo. **Pruebas**: doble tap, red offline, cambio entre pantallas, scroll infinito, conflicto de dos dispositivos. **Anti-patrón**: contadores hardcodeados o estado que revierte sin explicación.

## 6. PWA instalación y offline
**Problema**: instalar y reabrir con continuidad. **Diseño**: aviso discreto solo cuando instalable/deseado, no forzar ni prometer soporte idéntico en iOS/Android; fallback contextual. **Ingeniería**: detectar soporte real de la plataforma y evento disponible, respetar instalación existente, gestionar actualización de service worker y caché sin exponer datos ajenos. **Pruebas**: distintos navegadores, instalada/no instalada, offline, refresh, versión nueva y teclado virtual. **Anti-patrón**: mostrar botón de instalación que no hace nada.

## 7. Diálogo / confirmación destructiva
**Problema**: impedir pérdida irreversible. **Diseño**: verbo concreto y consecuencia, cancelar evidente, deshacer cuando sea posible. **Ingeniería**: backend verifica autorización; gestionar resultado tardío y reintentos. **A11y**: patrón de diálogo WAI APG, foco inicial prudente, Escape y retorno del foco. **Pruebas**: abrir/cerrar, teclado, segundo diálogo, error tras confirmar, scroll. **Anti-patrón**: modal ornamental sin foco controlado.

## Adaptación e innovación
Si dos patrones compiten, elegir el de menor esfuerzo cognitivo y técnica segura, preservando identidad y decisiones aprobadas. Innovar donde aporta valor **demostrable**; no romper convenciones por originalidad. Un patrón se convierte en «aprobado para este producto» solo tras su gate específico.
