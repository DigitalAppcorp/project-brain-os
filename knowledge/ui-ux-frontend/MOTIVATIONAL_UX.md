# UX motivacional y microinteracciones CSS — apoyo contextual, no manipulación

## Propósito y alcance

**UX motivacional** es una denominación operativa para aplicar apoyo, orientación, progreso honesto y refuerzo positivo en momentos pertinentes. No constituye una norma CSS ni una metodología psicológica validada por sí misma. CSS es la **capa de presentación**; la verdad del estado y los eventos proceden de la lógica de producto y sus fuentes autoritativas.

Este módulo complementa [DESIGN_REASONING.md](DESIGN_REASONING.md), [CREATIVE_EXPLORATION.md](CREATIVE_EXPLORATION.md), [UX_CONTENT.md](UX_CONTENT.md), [VISUAL_APPROVAL_PROTOCOL.md](VISUAL_APPROVAL_PROTOCOL.md) y [ADAPTIVE_LEARNING.md](ADAPTIVE_LEARNING.md). Solo se activa cuando ayuda a completar una tarea real. No impone celebraciones, gamificación ni efectos a todas las pantallas.

## Contrato de decisión: cinco preguntas antes de proponer una intervención

1. **Momento:** ¿la persona está empezando, avanzando, completando, esperando o intentando recuperarse de un error?
2. **Objetivo:** ¿el apoyo mejora comprensión, agencia, esfuerzo percibido, continuidad voluntaria o confianza? ¿Qué alternativa más simple bastaría?
3. **Señal verídica:** ¿cuál es la fuente real de éxito/progreso? ¿Es confirmada por backend, local, provisional o desconocida?
4. **Intervención mínima:** escoger una confirmación textual, indicador progresivo legítimo, microinteracción discreta o ninguna. No agregar pasos, pantallas, insignias ni distracciones sin razón.
5. **Riesgos y verificación:** contemplar accesibilidad, interrupción del flujo, preferencia de movimiento reducido, rendimiento, privacidad y posibles incentivos coercitivos.

**Matriz contextual** (opciones, no requisitos automáticos):

| Momento | Técnica posible | Condición de verdad | Evitar |
| --- | --- | --- | --- |
| Inicio de una tarea | mensaje breve orientador, próximo paso claro | instrucción válida para el flujo actual | promesas ficticias o entusiasmo artificial |
| Progreso | barra o pasos con estado persistido, microfeedback al completar subpaso | denominador y avance reales; si se desconocen, no mostrar % | avance falso, progreso que retrocede sin explicación |
| Éxito confirmado | confirmación clara + acento CSS breve/opcional | operación confirmada por fuente autoritativa | celebrar un request pendiente o confundir clic con éxito |
| Espera | indicador de actividad y explicación honesta, opción de salida si aplica | operación realmente pendiente; sin ETA inventado | spinner infinito que esconde errores |
| Error / recuperación | explicación útil, continuidad sin pérdida, reintento cuando procede | estado de error verificable | confeti, culpabilizar, premiar el fallo, ocultar pérdida de datos |
| Recompensa voluntaria | reconocimiento proporcional, opt-in cuando corresponde | logro realmente alcanzado y autorizado | streaks coercitivos, culpa, escasez ficticia, presión para pagar |

**No forzar técnicas motivacionales** en paneles densos, flujos médicos/legales/financieros delicados, moderación, formularios críticos o tareas donde la sobriedad y la certeza sean mejores. Si se proponen, justificar por qué añaden valor.

## Distinción de capas

- **Estado y permisos:** lógica JS/React y backend. Mostrar éxito *después* de la confirmación correspondiente. Una animación CSS no valida una operación.
- **Mensaje:** texto con contenido informativo y tono apropiado al producto. No insertar consignas de diseño, instrucciones al PO ni afirmaciones inventadas en la UI.
- **Forma:** CSS y tokens reales del producto (colores, tipografía, espaciamiento, easing); no inventar una paleta «motivacional» universal ni alterar marca para intensificar estímulos.
- **Accesibilidad:** información esencial visible en texto/semántica, no solo color, vibración, sonido o movimiento. Usar anuncios accesibles en el DOM cuando sean necesarios (por ejemplo `role="status"` para éxito no urgente), sin depender de contenido generado solo por `::before` o `::after`.
- **Privacidad y bienestar:** no perfilar estados emocionales o medir «motivación» individual sin autorización específica. No usar reconocimiento manipulativo para impulsar pagos o consentimiento.

## Receta CSS mínima — ilustrativa, no implementación de un producto

Un componente de resultado confirmado puede renderizar `<p class="ux-success" role="status">Guardado correctamente.</p>` **solo después** de recibir la confirmación verdadera; en errores presentar un mensaje recuperable en lugar de ese estado.

```css
/* Estado final legible aunque las animaciones estén desactivadas. */
.ux-success {
  opacity: 1;
  transform: none;
  color: var(--color-success-text);
  background: var(--color-success-surface);
  border-radius: var(--radius-md);
}

/* Solo decorativo y transitorio, nunca una señal exclusiva de éxito. */
@media (prefers-reduced-motion: no-preference) {
  .ux-success[data-just-confirmed="true"] {
    animation: ux-success-appear 180ms ease-out both;
  }
  @keyframes ux-success-appear {
    from { opacity: 0; transform: translateY(4px); }
    to { opacity: 1; transform: translateY(0); }
  }
}
```

Los tokens del ejemplo son **placeholders**: recuperar los existentes del producto, no crear nuevos sin motivo. La duración 180 ms y el desplazamiento de 4 px son parámetros de ejemplo, no normas ni resultados de investigación. La preferencia `reduce` conserva la información y elimina el movimiento ornamental. La transición se dispara una sola vez al montar el estado validado, no con cada rerender ni en bucles.

Para progreso real, preferir `<progress max="..." value="...">` o semántica equivalente verificable; un `width: 80%` estilizado no acredita un avance real. Para estados de espera, **no** utilizar el mismo estilo de éxito. No aplicar `aria-live` indiscriminado sobre contenedores que se actualizan continuamente.

## Gate de preview / QA proporcional

- Revisar si la intervención responde a un objetivo de usuario y conserva la acción principal.
- Capturar **antes/después** y estados relevantes: pendiente, éxito confirmado, fallo/reintento, sin animación y movimiento reducido. Solo donde apliquen al alcance.
- Inspeccionar contraste, foco, teclado, zoom/reflow, rendimiento y pulsaciones repetidas. CSS no debe bloquear la interacción, superponer CTA, provocar saltos de layout ni alterar hitboxes.
- Cumplir WCAG 2.2 aplicable: 2.2.2 (A) para movimiento automático prolongado; 2.3.1 (A) para destellos; considerar 2.3.3 (AAA) como buena práctica complementaria, **sin presentarla como requisito de AA**. Respetar `prefers-reduced-motion`.
- Comparar la preview aprobada con el runtime después de autorización, conforme a [PREVIEW_ARCHITECTURE.md](PREVIEW_ARCHITECTURE.md). Una captura fija no demuestra temporización, respuesta a errores ni reduced motion.
- Registrar feedback de aciertos y rechazos por componente/momento en [ADAPTIVE_LEARNING.md](ADAPTIVE_LEARNING.md). La aprobación de una animación en una pantalla no la convierte en patrón obligatorio para todas.

## Ejemplos de decisiones

- «Al terminar el perfil» → confirmación breve **si la persistencia fue verificada**, opcional acento de aparición, sin recompensa ficticia.
- «Me faltan dos pasos» → mostrar 2/4 únicamente cuando ese progreso tenga un contrato real y estable.
- «El pago fue rechazado» → recuperación clara sin felicitación, contador ficticio, presión o falso éxito.
- «El PO rechazó la animación pero aprobó el mensaje» → preservar texto aceptado, penalizar solo movimiento en ese contexto; no penalizar la pantalla completa.

## Fuentes y grado de evidencia

- **W3C WCAG 2.2**: criterios 2.2.2 Pause, Stop, Hide (A), 2.3.1 Three Flashes or Below Threshold (A), 2.3.3 Animation from Interactions (AAA). https://www.w3.org/TR/WCAG22/
- **W3C WAI, Understanding 2.3.3**: movimiento no esencial desencadenado por interacción y capacidad de desactivarlo. https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions
- **MDN, prefers-reduced-motion**: preferencia de sistema y media query. https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion

Estas fuentes respaldan **salvaguardas de movimiento y accesibilidad**; no demuestran que una microanimación concreta aumente motivación, retención o conversión. Cualquier mejora causal debe evaluarse con usuarios o indicadores definidos sin atribuir efectos no medidos.
