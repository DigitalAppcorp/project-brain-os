# Ingeniería frontend con responsabilidad UX

## Regla de entrada
Leer contrato del flujo, componentes y datos existentes; evaluar pantalla, backend, RLS/permiso, dependencias y navegación antes de cambiar. Hacer diff mínimo seguro. React/TypeScript es un ejemplo de aplicación, no un stack obligatorio para todos los productos.

## 1. Arquitectura
- Separar dominio/datos, estados de flujo y representación. La vista describe estados; no es la fuente de verdad de permisos o pagos.
- Usar componentes por responsabilidad; separar primitives de composiciones y dominios.
- Mantener API de componentes tipada: props semánticas, eventos explícitos, accesibilidad, variantes y defaults controlados.
- Dar identidad estable a listas; componentes controlados para inputs; no duplicar estado derivable.
- Preferir HTML/CSS nativos antes que reconstruir todo con JS; librerías nuevas requieren evaluación de bundle, mantenimiento y accesibilidad.
- CSS y tokens por sistema; no introducir hacks globales ni z-index infinito para un caso local.
- Asegurar estados significativos visibles para loading, empty, error, success, permisos y desconexión.

## 2. Estado y consistencia
### Modelo de estados recomendado
Una mutación debe expresar estados mutuamente consistentes, p. ej.:
**idle → pending → succeeded / failed → retry**, más cancelación si aplica.
No mostrar simultáneamente «no existe» y «activo» cuando la verdad aún se está consultando; diferenciar **desconocido** de **falso**.

### React
- Evitar estado redundante, contradictorio y duplicado; derivar valores durante render (React: Choosing the State Structure).
- No crear Effects para cálculos derivados ni eventos de usuario (React: You Might Not Need an Effect).
- En cargas asíncronas: cancelar/ignorar respuestas obsoletas, prevenir carreras y soportar errores.
- Elegir estrategia de caching/invalidation según aplicación; preservar datos que siguen siendo válidos y evitar flicker por remount.
- Optimistic UI solo con política explícita de rollback, reconciliación con servidor, feedback de conflicto y manejo de doble tap.
- Los contadores, likes, guardados o follows deben rehidratarse de la verdad autoritativa, no quedar eternamente en estado optimista local.
- Evitar interacciones durante transición incompatible (por ejemplo, iniciar una compra duplicada mientras se espera confirmación).

## 3. Acciones críticas y seguridad
- Idempotencia para operaciones con reintentos, pagos, invitaciones y otras mutaciones sensibles.
- UI no decide autorización: verificar en backend, proteger contra duplicados y estados incompatibles.
- Nunca colocar secretos en frontend o confiar en ocultar botones como control de acceso.
- Mostrar «éxito» solo tras confirmación semántica necesaria; preservar identificación y contexto del error.
- Evitar pérdida de datos por navegación, refresh o error inesperado. Definir reanudación cuando la tarea lo requiera.
- Confirmar/deshacer acciones destructivas según severidad y reversibilidad.
- No diseñar engaños para retener usuario ni dificultar cancelación.

## 4. Performance como experiencia
### Objetivos Core Web Vitals en datos reales
- **LCP ≤ 2.5 s**, **INP ≤ 200 ms**, **CLS ≤ 0.1** en el **percentil 75** de visitas, segmentado móvil/escritorio según guía web.dev. Son objetivos de calidad web, no una promesa ni una medición de este producto.
- Diferenciar laboratorio/CI de RUM real; perfiles lentos y equipos modestos son parte de UX.
- Evitar assets pesados innecesarios; dimensionar imágenes para prevenir CLS, usar formatos y resolución apropiados, lazy-load fuera del viewport.
- Carga diferida de mapas, editores, gráficos, carruseles y paneles complejos cuando no sean críticos.
- Evitar trabajo de render caro durante scroll, onChange y drag; medir antes de microoptimizar.
- Reservar espacio para datos/imágenes asíncronos; skeletons deben representar estructura real y no ser artificialmente interminables.
- Evitar animaciones que confundan latencia con progreso confirmado; feedback inmediato y honesto.

## 5. Diseño de fallos
Matriz obligatoria para flujo significativo:
- 0 resultados / sin contenido / primera visita.
- Cargando normal / lento prolongado / timeout.
- Sin red / red intermitente / regreso al foreground.
- Permiso denegado (ubicación, cámara, notificaciones).
- Sesión expirada / sin autorización.
- Solicitud duplicada / confirmación retrasada / respuesta tardía.
- Datos obsoletos / error del servidor / recuperación sin repetir formulario.
- Navegación de vuelta, refresh, reentrada o instalación PWA.
- Tamaño, idioma, rotación, zoom, teclado virtual, scroll con barra fija.

Para cada fallo decidir **qué ve**, **qué puede hacer** y **qué datos se conservan**.

## 6. Pruebas técnicas y funcionales
- Unit tests de estado puro y validaciones.
- Integration tests de componentes con navegación, eventos y respuestas simuladas.
- E2E (p. ej. Playwright) del camino principal y recuperación de errores, no solo click del botón.
- A11y con axe + teclado + lector manual donde aplique.
- Visual regression por viewport y tema con umbrales y revisión humana; screenshot diffs no prueban UX.
- Condiciones de concurrencia, doble click, request abortado y sesión/permiso.
- Comprobar red real y navegador real para capacidades PWA como instalación, GPS, push, mapas y return URLs.

## 7. Criterios de entrega
Un PR no está listo solo con CI verde. Debe demostrar:
1. Especificación de flujo y estados coherentes.
2. Ausencia de regresiones conocidas.
3. Evidencias de tests reproducibles.
4. Verificación visual y de interacción en dispositivos pertinentes.
5. Preservación de contratos de backend y accesibilidad.
6. Limitaciones o pruebas pendientes explícitas.

Documentar «no validado» cuando no se tiene entorno de prueba.
## Recetas operativas y restricciones
Ver [TEST_RECIPES.md](TEST_RECIPES.md) para ejemplos adaptables de e2e, axe, condiciones de carrera, pruebas manuales y registros de evidencia. Ver [PATTERN_LIBRARY.md](PATTERN_LIBRARY.md) para escenarios de mapas, pagos, paneles, feeds y PWA. No considerar la existencia de recetas como prueba ejecutada. Su alcance y riesgo determinan el gate en [QUALITY_GATES.md](QUALITY_GATES.md).
