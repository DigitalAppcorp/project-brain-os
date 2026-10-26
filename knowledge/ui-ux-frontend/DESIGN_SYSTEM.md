# Sistema visual y diseño de interacción

## 1. Diseño visual al servicio de la comprensión
La primera evaluación es «¿entiende y completa su tarea?», luego «¿tiene calidad estética e identidad?». Un efecto premium que dificulta legibilidad, predictibilidad, control o velocidad es un defecto, no un logro.

### Jerarquía y composición
- Determinar **una acción primaria por contexto**, no varias compitiendo. Las secundarias deben distinguirse por prioridad, no ocultarse arbitrariamente.
- Definir bloques por significado y proximidad; alinear a retícula consistente; controlar ritmo vertical y densidad.
- Evitar interfaces planas sin contraste semántico: superficies similares necesitan separaciones mediante espacio, tipografía, sombreado, fondo o delimitación.
- Los títulos deben describir contenido, no servir únicamente de adorno. Navegación identificable y estado activo inequívoco.
- No sacrificar legibilidad por espacio negativo excesivo ni introducir relleno que aleje tareas críticas.

### Tipografía y contenido
- Base habitual recomendada para lectura: alrededor de **16 CSS px** o equivalente, adaptable y nunca congelada contra zoom. No es mínimo universal normativo.
- Construir escala tipográfica semántica (título, sección, cuerpo, etiqueta, ayuda, dato); preferir tamaños y alturas de línea legibles, con medidas de texto contenidas.
- Contraste de texto y controles: ver [ACCESSIBILITY.md](ACCESSIBILITY.md).
- Copy de acción con verbos y resultado específico; no depender de textos ambiguos («Listo», «Continuar») si el contexto no los aclara.
- Etiquetas visibles para entradas; placeholders opcionales únicamente como ejemplo y nunca como único rótulo.
- Internacionalización desde componentes: cadenas traducibles, espacio para expansión de texto, formatos locales y textos bidireccionales cuando aplique.

### Tokens y componentes
- Diseñar tokens de **color semántico, superficies, tipografía, escala espacial, radio, sombras, elevación, densidad, z-index, breakpoints y motion**.
- Valores locales excepcionales solo con razón documentada. No crear 10 radios o 14 grises por pantalla.
- Los tokens **no** eximen de probar contraste real cuando el fondo es foto, mapa o translúcido.
- Cada componente reusable define API, variantes, disabled/loading/active/error, foco, teclado, estado vacío, responsive y guía de contenido.
- Asegurar estados interactivos visibles sin depender solo de color: hover cuando exista, pressed, focus-visible, selected, loading y disabled.

## 2. Responsive real (no «cabe en mi teléfono»)
- Diseñar **mobile-first**, pero con layout adaptable por contenido, no por un modelo específico.
- Probar al menos **320, 360/375, 390/430, 768, 1024 y 1440 CSS px**, ajustando a dispositivos/mercado reales. Estos son puntos de prueba internos, no breakpoints normativos.
- Considerar reflow a 320 CSS px (WCAG 1.4.10 y excepciones), zoom 200–400%, orientación, teclado virtual, scroll y larga traducción.
- Verificar safe areas, notch, barras del navegador y componentes sticky/fixed: no tapar CTA, último elemento, indicador de foco ni contenido.
- Preferir distribución fluida y container queries cuando aportan; evitar posición absoluta para layout general.
- Para barras inferiores, reservar espacio efectivo de scroll y no asumir viewport height estático. Usar unidades dinámicas/safe-area cuando corresponda.

## 3. Objetivos táctiles y gestos
- WCAG 2.2 AA 2.5.8: target 24×24 CSS px con excepciones especificadas; **preferir mayor** en móvil por usabilidad.
- Apple recomienda **44×44 pt** en iOS, regla de plataforma, no una conversión directa ni obligación WCAG; usar cerca de 44–48 CSS px como objetivo ergonómico web contextual.
- Dar espacio entre acciones peligrosas y frecuentes; ampliar zona interactiva sin cambiar tamaño visual del icono.
- Todo gesto exclusivo (swipe, drag, long press) que opere función debe tener alternativa accesible si la norma lo requiere.
- La tarjeta completa solo debe ser clickable si tiene una acción única, semántica y coherente; controles internos no pueden disparar navegación accidental.

## 4. Motion y superficies
- Animación solo cuando explica causalidad, transición o estado; no para ocultar latencia.
- Respetar prefers-reduced-motion; eliminar/atenuar desplazamientos, parallax y bucles no esenciales.
- Emplear transform/opacity con prudencia; evitar trabajo de layout en scroll y consumo excesivo de blur/filtros.
- Glassmorphism, transparencias y gradientes deben verificarse sobre **el peor contenido dinámico**, no una captura ideal.
- Gradiente de recorte/scroll puede mejorar estética, pero jamás ocultar sin indicio una opción esencial o eliminar lectura/foco de elemento.
- Los efectos «3D» y sombras nunca sustituyen forma, nombre y accesibilidad de un control.

## 5. Navegación, mapas y dashboards
### Navegación
- Mantener consistencia de ubicación y vocabulario; mostrar dónde está el usuario y ruta de retorno.
- No esconder acciones fundamentales en menús desbordantes a menos que sean realmente secundarias.
- Preservar historial y scroll cuando es parte del modelo de tarea; evitar resets de pantalla sin intención.

### Mapas
- Mapas complementan listas; ofrecer lista/búsqueda/alternativa textual cuando el mapa no carga o no es operable.
- Separar «centrar mapa», «abrir detalle», «cómo llegar», «check-in» y «guardar»; no reutilizar el mismo tap con resultados ambiguos.
- No confiar en pines diminutos, hover o localización siempre concedida; manejar zoom, selección, permiso denegado, posiciones inexactas y cobertura.
- Medir peso de mapas, carga diferida, fallback y política de fotografías/atribución.

### Administración
- Priorizar estado global, alertas accionables, tareas frecuentes y lectura de tendencias.
- Agrupar métricas con definición temporal, denominador, fecha de actualización y estado vacío.
- Evitar tablas imposibles en móvil: permitir resumen, drill-down, scroll controlado y filtros persistentes.
- No comunicar salud del sistema con un color único; ofrecer texto y detalle de fallo.

## 6. No extrapolar estilos
No transportar paletas, ausencia de contornos, navegación, 3D o estética de una aplicación a otra sin decisión explícita. Un sistema visual generalizable define reglas; el producto define sus tokens y personalidad.
## Calidad visual auditable
Aplicar [VISUAL_QUALITY.md](VISUAL_QUALITY.md) para dirección de arte, divergencia respecto al brief, comparación referencia ↔ ejecución y revisión interdisciplinaria. Los criterios de identidad son específicos del producto, y cada aceptación debe identificar viewport, estado y comportamiento realmente observados. Criterios de entrega en [QUALITY_GATES.md](QUALITY_GATES.md).
