# Fuentes verificadas para UI/UX Frontend

**Fecha de investigación**: 2026-10-25. La fecha refleja consulta de la documentación, no revisión futura garantizada. En caso de discrepancia, leer la edición vigente de la fuente oficial. Distinguir requisitos WCAG de recomendaciones de diseño.

## Normas y patrones de accesibilidad (prioridad alta)
1. **W3C — WCAG 2.2, Recommendation, 12 dic 2024**. Objetivo de conformidad y criterios testables: contraste de texto 1.4.3, contraste no textual 1.4.11, zoom 1.4.4, reflow 1.4.10, foco 2.4.7/2.4.11, dragging 2.5.7, target 2.5.8, accessible authentication 3.3.8. https://www.w3.org/TR/WCAG22/
2. **W3C WAI — ARIA Authoring Practices, Dialog Modal**. Semántica, contención de foco, cierre con Escape, devolución de foco. https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
3. **W3C WAI — Developing a Keyboard Interface**. Tab/Shift+Tab y manejo correcto de foco. https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/
4. **W3C WAI — Labeling Controls**. Asociar etiquetas y reconocer controles. https://www.w3.org/WAI/tutorials/forms/labels/
5. **W3C WAI — Form Instructions**. Placeholder no sustituye etiqueta. https://www.w3.org/WAI/tutorials/forms/instructions/
6. **W3C WAI — Images Tutorial**. Texto alternativo según intención: informativo, decorativo o funcional. https://www.w3.org/WAI/tutorials/images/

## Heurísticas y UX investigada
7. **Nielsen Norman Group — 10 Usability Heuristics**. Revisión de 30 ene 2024. Estado del sistema, control, consistencia, prevención/recuperación de errores, reconocimiento vs memoria, minimalismo. Marco heurístico, no norma legal. https://www.nngroup.com/articles/ten-usability-heuristics/
8. **Nielsen Norman Group — Severity Ratings for Usability Problems**. 0–4, frecuencia, impacto, persistencia; S0–S4 del módulo es adaptación contextual, no predicción matemática. https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/
9. **Nielsen Norman Group — UX Research Cheat Sheet**. Escoger métodos según pregunta, test temprano y medición contextual. https://www.nngroup.com/articles/ux-research-cheat-sheet/
10. **Baymard Institute — Ecommerce UX Audit** (10 jul 2026). Revisar fricción mediante flujos y tareas completas, no confiar solo en embudos o preferencias estéticas. La evidencia procede principalmente de comercio electrónico: no generalizar sus cifras a apps de otra categoría. https://baymard.com/blog/ecommerce-ux-audit
11. **Baymard Institute — How to Audit Checkout Flow** (13 may 2026). Analytics detecta dónde ocurre abandono, observación UX explica por qué; aplicable especialmente a pagos. https://baymard.com/blog/audit-checkout-flow-hidden-friction

## Diseño de sistemas, plataformas y formularios
12. **US Web Design System — Design Tokens**. Semántica de escalas y consistencia de diseño. https://designsystem.digital.gov/design-tokens/
13. **US Web Design System — Typography**. Legibilidad, jerarquía, longitud de línea y espacios (recomendaciones contextuales, no mínimos WCAG). https://designsystem.digital.gov/components/typography/
14. **Apple Developer — UI Design Dos and Don'ts**. Área de toque iOS 44×44 pt; recomendación de plataforma distinta del mínimo normativo WCAG web. https://developer.apple.com/design/tips/
15. **GOV.UK Design System — Error Messages**. Mensajes específicos con recuperación, cercanos a campos. https://design-system.service.gov.uk/components/error-message/
16. **GOV.UK Design System — Recover from Validation Errors**. Preservar entradas y validar accesiblemente. Nota: su preferencia por desactivar validación HTML nativa responde a su sistema particular; no es obligación universal para toda app. https://design-system.service.gov.uk/patterns/validation/
17. **MDN — prefers-reduced-motion**. Respeto a preferencias del sistema para motion. https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion

## Ingeniería y verificación
18. **React — Choosing the State Structure**. Evitar estado redundante, contradictorio y duplicado. https://react.dev/learn/choosing-the-state-structure
19. **React — You Might Not Need an Effect**. Effects para sincronización externa; prevención de races en fetching. https://react.dev/learn/you-might-not-need-an-effect
20. **Google web.dev — Web Vitals**. LCP ≤2.5s, INP ≤200ms, CLS ≤0.1, p75; medición en visitas reales. https://web.dev/articles/vitals
21. **Google web.dev — Getting Started Measuring Web Vitals**. Diferenciar RUM y laboratorio; interpretación de p75. https://web.dev/articles/vitals-measurement-getting-started
22. **Playwright — Accessibility Testing**. Automatización con axe-core y advertencia explícita: hay barreras que requieren pruebas manuales. https://playwright.dev/docs/accessibility-testing

## Evaluación de evidencia
- **NORMATIVA**: especificación de conformidad (WCAG). Citar criterio exacto, nivel y excepciones.
- **DOCUMENTAL OFICIAL**: APIs/plataformas y sistemas de diseño. Verificar versión; distinguir guía de obligación.
- **INVESTIGACIÓN**: método, muestra, sector, fecha y restricciones de extrapolación.
- **HIPÓTESIS INTERNA**: diseño propuesto, severidad, metas no normativas. Evaluar en el producto antes de afirmar efectividad.

## Límites
Ninguna fuente certifica por sí sola la conformidad o calidad de un proyecto concreto; se requieren inspección, pruebas y revisión de usuarios. No atribuir directamente a un sitio web resultados de pruebas que no ejecutamos.