# Fuentes verificadas para UI/UX Frontend

**Fecha de investigación**: 2026-10-25. La fecha refleja consulta de la documentación, no revisión futura garantizada. En caso de discrepancia, leer la edición vigente de la fuente oficial. Distinguir requisitos WCAG de recomendaciones de diseño.

## Normas y patrones de accesibilidad (prioridad alta)
1. **W3C — WCAG 2.2, Recommendation original 5 oct 2023, actualización 12 dic 2024**. Objetivo de conformidad y criterios testables: contraste de texto 1.4.3, contraste no textual 1.4.11, zoom 1.4.4, reflow 1.4.10, foco 2.4.7/2.4.11, dragging 2.5.7, target 2.5.8, accessible authentication 3.3.8. https://www.w3.org/TR/WCAG22/
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

## Metodología formal y pruebas críticas añadidas en v0.2.0
23. **W3C — WCAG Evaluation Methodology (WCAG-EM) 2.0**, Group Note de 23 jul 2026. Cinco fases: alcance, exploración, muestreo representativo, evaluación e informe; aplicable a aplicaciones digitales; no reemplaza WCAG 2.2 ni añade requisitos. https://www.w3.org/TR/wcag-em-2/
24. **W3C WAI — WCAG-EM overview**. Explica alcance y diferencias de WCAG-EM 1 vs 2 y procedimiento. https://www.w3.org/WAI/test-evaluate/conformance/wcag-em/
25. **W3C — WCAG 2.2 publication history**. Diferencia publicación original y republicación de erratas. https://www.w3.org/standards/history/WCAG22/

## Evaluación de evidencia
- **NORMATIVA**: especificación de conformidad (WCAG). Citar criterio exacto, nivel y excepciones.
- **DOCUMENTAL OFICIAL**: APIs/plataformas y sistemas de diseño. Verificar versión; distinguir guía de obligación.
- **INVESTIGACIÓN**: método, muestra, sector, fecha y restricciones de extrapolación.
- **HIPÓTESIS INTERNA**: diseño propuesto, severidad, metas no normativas. Evaluar en el producto antes de afirmar efectividad.

## Límites
Ninguna fuente certifica por sí sola la conformidad o calidad de un proyecto concreto; se requieren inspección, pruebas y revisión de usuarios. No atribuir directamente a un sitio web resultados de pruebas que no ejecutamos.

## Fuentes integradas para la arquitectura v0.3.0
26. **NIST — Human Centered Design**. Describe cuatro actividades: contexto, requisitos, soluciones y evaluación; aplicable a ciclo iterativo. https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design
27. **GOV.UK — Understand content design**. El contenido se fundamenta en lo que una persona necesita saber o hacer y en su ubicación/formato apropiados; no respalda ocultar información obligatoria. https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/understand-content-design/
28. **GOV.UK — Government Design Principles**. Empezar por necesidades, hacer menos, trabajar con datos e iterar. https://www.gov.uk/guidance/government-design-principles
29. **Anthropic — Frontend Design SKILL.md (fuente pública)**. Documenta patrones visuales genéricos y propone planificación, evaluación del brief, composición deliberada y copy desde perspectiva del usuario. **Es guía del fabricante, no prueba causal de por qué todos los modelos fallan.** https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md

### Hipótesis no confirmadas (evitar afirmaciones causales)
- `Implementation-to-UI leakage` es etiqueta **operativa propuesta**, no nombre académico confirmado por estas referencias.
- Que el modelo maximice el reconocimiento del prompt del PO sobre necesidades finales es una **hipótesis**; no afirmar optimización deliberada sin estudio controlado.
- La homogeneización puede correlacionar con plantillas y datos de entrenamiento, pero ninguna de estas fuentes atribuye el patrón a una causa neural única de GPT o Claude.

## Movimiento, microfeedback y apoyo motivacional (ampliación 2026-10-26)

30. **W3C WCAG 2.2, 2.2.2 Pause, Stop, Hide (Level A)**. Para información que se mueve o actualiza automáticamente y cumple las condiciones aplicables, ofrecer mecanismo de pausa/parada/ocultación (con excepciones). https://www.w3.org/TR/WCAG22/#pause-stop-hide
31. **W3C WCAG 2.2, 2.3.1 Three Flashes or Below Threshold (Level A)**. Limitar destellos conforme a criterios. https://www.w3.org/TR/WCAG22/#three-flashes-or-below-threshold
32. **W3C WAI, Understanding 2.3.3 Animation from Interactions (Level AAA)**. Proteger contra efectos de movimiento no esencial disparados por interacción; NO confundir AAA con AA. https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions
33. **MDN, CSS prefers-reduced-motion**. Media query para respetar preferencia de reducir movimiento. https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion

**Límite de evidencia:** estas fuentes describen accesibilidad y comportamiento de movimiento, no demuestran que CSS aumente motivación o conversión. `MOTIVATIONAL_UX.md` define un criterio operativo de diseño contextual, no un método clínico, una norma ni un efecto causal medido.
