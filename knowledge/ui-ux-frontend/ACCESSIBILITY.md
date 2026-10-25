# Accesibilidad — criterios comprobables

**Base**: W3C WCAG 2.2 nivel AA como objetivo del módulo, sujeto a regulación/requisitos del proyecto. WCAG es una norma de resultados; Apple, Material, WAI APG y USWDS incluyen recomendaciones y patrones, no todos requisitos normativos. No confundir «pasó axe» con «conforme a WCAG».

## 1. Matriz esencial
| Aspecto | Criterio / enfoque | Prueba |
|---|---|---|
| Contraste texto habitual | **4.5:1** mínimo, salvo excepciones normativas (1.4.3 AA). | Verificar par de colores en estados y fondos reales. |
| Texto grande | **3:1** si cumple definición normativa de grande (1.4.3). | Medir tamaño/peso y fondo. |
| Componentes no textuales | **3:1** para información visual necesaria e indicadores relevantes, con excepciones (1.4.11 AA). | Revisar icono, foco, contorno, límites y selección. |
| Focus | Visible (2.4.7 AA) y no totalmente oculto (2.4.11 AA). | Navegar con Tab bajo header/footer sticky y modal. |
| Táctil | **24×24 CSS px** para 2.5.8 AA, o excepción admitida. | Comprobar hitbox real y separación, no solo tamaño del glyph. |
| Zoom y reflow | Texto 200%, reflow equivalente a ancho 320 CSS px salvo contenidos excepcionales (1.4.4, 1.4.10). | Ampliar, girar, long text. |
| Movimiento de arrastre | Alternativa de un solo puntero si el arrastre no es esencial (2.5.7 AA). | Completar mismo resultado sin drag. |
| Autenticación | No exigir exclusivamente prueba cognitiva como recordar contraseña/puzzle sin alternativa accesible (3.3.8 AA). | Revisar login y recuperación. |
| Errores | Identificar y sugerir corrección donde aplique (3.3.1 y 3.3.3). | Forzar errores, verificar texto/foco/reintento. |
| Labels | Nombre, función y rol; formularios con etiquetas asociadas (1.3.1, 3.3.2, 4.1.2). | Inspeccionar árbol accesible y lector. |

## 2. HTML y semántica
- Usar button para acción; a con href para navegación; label vinculado al control; headings con jerarquía real; nav, main, form y listas semánticas.
- «Div clicable» más role y tabIndex no reemplaza automáticamente comportamiento de teclado nativo.
- Usar ARIA solo para completar semántica, no compensar HTML incorrecto. Estados aria-expanded, aria-selected, aria-pressed, aria-live solo cuando describen estado real.
- Icono decorativo: ocultarlo a tecnologías asistivas; imagen informativa: alt según función; imagen usada como botón: nombre de acción.
- No usar placeholder en sustitución de label. Marcar campos opcionales/requeridos con texto entendible.

## 3. Teclado y navegación asistiva
- Tab lógico, Shift+Tab inverso, Enter/Space según control, Escape al cerrar diálogo.
- Nunca eliminar outline de foco sin reemplazo eficaz y contrastado; usar focus-visible.
- Evitar trampas de teclado, salvo contención esperada dentro de modal mientras está abierto.
- Modal real: aria-modal solo si el fondo es verdaderamente inerte, foco inicial dentro, Tab cíclico, Escape, cierre visible y retorno del foco al disparador o destino lógico (APG).
- Focus y scroll coherentes al cambiar pantalla, completar tarea, mostrar error o eliminar control.
- Componentes complejos (tabs, combobox, menu, tree, dialog) deben adoptar patrón APG completo o componente accesible maduro, no «ARIA parcial».

## 4. Errores, estados y feedback
- Para errores de formulario, mostrar descripción precisa junto al campo; una lista de errores puede enfocarse al enviar formularios largos.
- Preservar lo escrito tras fallar validación; no resetear sin necesidad.
- Usar aria-describedby, aria-invalid y anuncios en vivo cuando correspondan, sin saturar.
- No bloquear datos por teclado virtual o por mensajes overlay.
- Loading y éxito deben poder percibirse sin movimiento/color/sonido exclusivamente; actualizar atributos y texto accesibles.
- Prevenir acción irreversible con confirmación o deshacer, según contexto; foco inicial menos destructivo si corresponde.

## 5. Vision y motion
- Respetar preferencia prefers-reduced-motion; no basar sentido en animación o parpadeo.
- Verificar legibilidad a zoom, large text, forced-colors/high contrast cuando relevante, y fondos fotográficos.
- Evitar objetivos exclusivamente basados en precisión motora, ubicación GPS, códigos memorísticos o temporizadores inflexibles.

## 6. Batería manual mínima
1. Navegar un flujo crítico sin mouse; foco siempre perceptible.
2. Ejecutarlo con lector de pantalla (al menos uno disponible), comprobando nombres/roles/estados.
3. Probar zoom 200% y 400% / ancho efectivo 320 CSS px, sin pérdida funcional.
4. Probar reducción de movimiento y alto contraste si la plataforma lo soporta.
5. Inyectar error, latencia y pantalla vacía para comprobar feedback.
6. Verificar tamaños reales de targets y contrastes, no mediante aproximación visual.
7. Validar con personas con distintas necesidades de acceso cuando sea viable.

## 7. Herramientas y límites
Automatizar Playwright + axe-core para violaciones detectables. Complementar con Lighthouse, inspección de árbol de accesibilidad y pruebas manuales de teclado/lector. La automatización **no detecta** todos los problemas WCAG ni prueba comprensión humana. Registrar escenarios ejecutados, dispositivo/navegador, fecha, resultado y limitaciones.

## Fuentes
[WCAG 2.2](https://www.w3.org/TR/WCAG22/), [APG modal](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/), [WAI labels](https://www.w3.org/WAI/tutorials/forms/labels/), [Apple targets](https://developer.apple.com/design/tips/), [Playwright](https://playwright.dev/docs/accessibility-testing).