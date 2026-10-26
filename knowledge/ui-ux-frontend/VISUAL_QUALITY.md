# Calidad visual — dirección de arte, fidelidad y crítica

## Propósito
El diseño de élite combina identidad propia, claridad del recorrido y ejecución visual consistente. Una captura atractiva NO demuestra utilidad; un flujo accesible pero visualmente pobre NO satisface automáticamente un brief de dirección de arte. Auditar por separado y reunir ambos resultados.

## Contrato de dirección de arte antes de diseñar
Registrar: (1) audiencia, tarea y tono emocional deseado; (2) atributos de marca y antiatributos; (3) referencias visuales **con motivo específico**, no imitación global; (4) restricciones de plataforma; (5) tipografía, color y sistema de composición; (6) nivel de densidad, imágenes/ilustración/iconografía; (7) interacción y motion; (8) accesibilidad; (9) evidencia de aceptación.

### Referencias comparables
Cada referencia debe declarar «qué adoptamos», «qué NO adoptamos» y «riesgo al trasladarlo». Apple puede inspirar refinamiento, no legitimar automáticamente transparencia, blur o navegación oculta. Stripe puede inspirar formularios, no definir la densidad de una aplicación infantil. Ningún referente dicta una estética universal.

## Auditoría visual de ocho dimensiones
1. **Jerarquía**: en 3–5 segundos se identifica propósito, acción primaria, estado y contenido principal; probar comprensión real si la afirmación importa.
2. **Composición**: retícula, alineaciones ópticas, agrupación por proximidad, anchos, densidad, uso intencional del espacio negativo.
3. **Tipografía**: familias/pesos restringidos, escalas, interlineado, longitud de línea, truncamiento razonable, expansión de traducciones.
4. **Color y superficies**: semántica, contraste real, fondos dinámicos, modo oscuro/alto contraste; degradados y vidrio no ocultan lectura.
5. **Iconografía e imágenes**: misma familia visual, metáforas comprendidas, proporciones consistentes, licencia/atribución y fotografías pertinentes.
6. **Estados del componente**: default/hover/focus/pressed/selected/disabled/loading/error y feedback sin depender solo del color.
7. **Continuidad**: sistema compartido entre pantallas, transición de contexto, posición de acciones, control de scroll y navegación.
8. **Motion y acabado**: causalidad visible, easing/duración coherentes, reduced motion, jitter/flicker, blur costoso, microdesajustes e inconsistencias.

## Revisión de fidelidad referencia → producto
- Reunir referencia aprobada, restricciones y captura/ejecución actual al **mismo viewport y estado**, con fecha.
- Comparar estructura primero: barra, retícula, bloques, jerarquía, tamaño de superficies.
- Después tipografía, color, iconos, espaciados, radios, sombras, estados y animación.
- Marcar cada divergencia: ERROR respecto al alcance aprobado / DECISIÓN nueva / DIFERENCIA de plataforma o dato.
- Explicar por qué existe; no rellenar huecos interpretando libremente un screenshot.
- Proponer solución mínima con evidencia antes de reescribir todo el layout.
- Captura vs ejecución: no afirmar comportamiento de scroll, foco ni animación a partir de imagen fija.

## Revisión crítica en tres pasadas
- **Director de arte**: marca y composición; lista máxima de 3 cambios de mayor impacto.
- **Diseñador de interacción**: acciones, estados, legibilidad e inclusión; puede rechazar un efecto.
- **Ingeniero frontend**: factibilidad, responsive, compatibilidad, rendimiento y costo de mantenimiento.
Registrar conflictos explícitos. La estética no puede dispensar fallos críticos; la ingeniería no puede convertir un rediseño aprobado en una versión visual distinta sin explicar divergencias.

## Errores recurrentes y tratamiento
- «Más premium = más blur»: medir legibilidad sobre fondos cambiantes; ofrecer superficie opaca adaptable.
- «Menos bordes = siempre mejor»: conservar distinción y focus-visible mediante forma/espacio/contraste.
- «Más animación = más fluido»: observar tiempos de respuesta y reduced-motion; quitar movimiento decorativo excesivo.
- «Un screenshot pixel-perfect certifica terminado»: añadir responsive, estados, teclado, scrolling, datos y pruebas en dispositivo.
- «La referencia manda en todos los detalles»: separar intención de decisiones incidentales; identificar incompatibilidades.

## Evidencia y salida
Entregar: objetivo → referencia/estado aprobado → diferencias observables → tres problemas priorizados → propuesta y trade-offs → criterios de comparación → estados probados/no probados. No inventar «pixel-perfect» ni porcentajes de fidelidad sin criterio reproducible. Para medición usar [UX_METRICS.md](UX_METRICS.md), para aceptación [QUALITY_GATES.md](QUALITY_GATES.md).

## Revisión visual situada v0.3.0
Antes de llamar «mala composición» a un título alineado a la izquierda, examinar **función textual**, jerarquía, espacio, longitud, relación con CTA y preferencias legítimas del producto. No usar centro/izquierda como dogma. Antes de agregar eyebrow o pastilla verificar su función real; para texto de interfaz usar [UX_CONTENT.md](UX_CONTENT.md). Inspiración externa: [REFERENCE_ANALYSIS.md](REFERENCE_ANALYSIS.md); creatividad pertinente: [CREATIVE_EXPLORATION.md](CREATIVE_EXPLORATION.md). En iteraciones técnicas, comparar con baseline aprobado mediante [CHANGE_INTEGRITY.md](CHANGE_INTEGRITY.md).
