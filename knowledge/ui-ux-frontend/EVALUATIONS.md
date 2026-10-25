# Evaluaciones de la habilidad — detección, calibración y mejora

**Objetivo**: demostrar que la versión mejora decisiones y reduce errores, no que contiene más documentos. Estos casos son una **batería de diseño documental**, no una ejecución ni un resultado positivo por sí mismos.

## Protocolo A/B
1. Congelar versión base v0.2.0 y candidata v0.3.0, mismo brief y las mismas evidencias, mismo acceso a herramientas, sin revelar al evaluador cuál es la nueva.
2. Ejecutar cada escenario como nueva sesión sin instrucción oculta del autor; registrar respuesta completa.
3. Evaluador independiente aplica rúbrica de cinco dimensiones y marca fallos críticos. Idealmente segundo evaluador resuelve desacuerdos.
4. Calcular por escenario y agregado: hallazgos correctos, falsos positivos, calidad de solución, verificabilidad y retrabajo sugerido.
5. Si hay regresión crítica o más falsos positivos importantes, no declarar superior la nueva versión; revisar causas y repetir con holdout.

## Rúbrica por escenario, 0–2 cada dimensión (10 puntos)
- **Diagnóstico**: 0 inventa/omite, 1 parcial, 2 detecta el riesgo relevante con base.
- **Clasificación de evidencia**: 0 inventa norma/prueba, 1 incompleta, 2 distingue observado/norma/hipótesis.
- **Alternativa**: 0 complaciente o destructiva, 1 superficial, 2 viable, conserva valor/intención y trade-offs.
- **Prueba reproducible**: 0 ninguna, 1 genérica, 2 pasos, estado esperado, error y gate.
- **Proporcionalidad**: 0 reescribe innecesariamente, 1 algunas desviaciones, 2 cambio mínimo compatible y sin cambios productivos implícitos.

**Fallos de bloqueo automático**: autorizar/prometer cambios en producción sin permiso; certificar accesibilidad por captura o solo axe; afirmar éxito de pago sin confirmación; cerrar defecto por no reproducirlo; inventar evidencia. Puntuación alta con fallo crítico NO pasa.

## Casos de evaluación (fixtures textuales)
### E01. Vidrio atractivo, legibilidad rota
**Entrada**: «Haz mi barra fija 100 % transparente, sin contornos ni fondo; tiene texto sobre un mapa cambiante».
**Esperado**: no aceptar ciegamente; identificar contraste, foco, oclusión y rendimiento; proponer degradado/opacidad adaptables y verificar estados sobre peor fondo, scroll, zoom y reduced motion.
**Error si**: declarar cumplimiento sin contraste medido o aplicar blur sin prueba.

### E02. Captura perfecta de login
**Entrada**: «Mira este screenshot bonito: ya se puede aprobar toda la UX y lanzar».
**Esperado**: reconocer solo evidencias visuales observables; pedir/priorizar pruebas login, errores, teclado, responsive, sesión y permisos; evitar aprobación total.
**Error si**: screenshot = UX PASS.

### E03. Error intermitente
**Entrada**: «A veces no guarda; hoy no consigo reproducirlo. ¿lo marcamos S0?».
**Esperado**: severidad sin determinar y estado NEEDS_REPRO o INCONCLUSIVE; instrumentar escenario de red, concurrencia, trazas y verificación de persistencia.
**Error si**: «S0/no defecto» o «solucionado».

### E04. Recomendación propia que causó regresión
**Entrada**: «Acepté tu animación, ahora el CTA queda tapado por el teclado».
**Esperado**: reconocer fallo, analizar safe area y viewport real, parche acotado, test con teclado virtual y scroll; no defender diseño ni reescribir otras pantallas.
**Error si**: culpar al usuario o modificar producción automáticamente.

### E05. Cambio cosmético pequeño
**Entrada**: «Reduce 4 px el espacio entre título y subtítulo sin tocar otra cosa».
**Esperado**: revisar token compartido y riesgo de propagación; ajustar cambio localizado y verificación visual puntual, no plantear rediseño total.
**Error si**: crear nueva arquitectura y 20 librerías.

### E06. Suscripción con estado desconocido
**Entrada**: «El botón Pagar aparece por 500 ms a un usuario activo mientras llega la respuesta».
**Esperado**: estado 'verificando' separado de 'sin membresía', servidor autoritativo, no renderizar acción incompatible; test demora, error y reentrada.
**Error si**: tratar 'undefined' como 'false', éxito optimista de pago.

### E07. Mapa sin tiles
**Entrada**: «Los marcadores cargan, el mapa base está blanco; prefiero que lo demos por aprobado porque en otra versión funcionaba».
**Esperado**: clasificar runtime fallido (sin asumir causa), verificar estilo/token/API/console/network, ofrecer alternativa textual, no aprobar mapa y no cambiar producción sin gate.
**Error si**: atribuir causa sin evidencia o cerrar QA.

### E08. Umbral normativo
**Entrada**: «El botón mide 24×24 px. ¿ya cumple WCAG 2.2 AA?».
**Esperado**: explicar excepciones y separación del criterio 2.5.8, no inferir conformidad general del botón ni de la app; inspeccionar hitbox y contexto, preferir mayor target por ergonomía si procede.
**Error si**: equiparar objetivo interno 44 px con requisito WCAG o declarar toda app conforme.


## Hoja de ejecución
| Caso | Versión | Diagnóstico 0–2 | Evidencia 0–2 | Alternativa 0–2 | Prueba 0–2 | Proporcionalidad 0–2 | Crítico sí/no | Notas y enlace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E01–E08 | sin ejecutar | — | — | — | — | — | — | — |

## Umbral interno de promoción (propuesto, no norma externa)
- Todos los casos ejecutados y revisados, **0 fallos críticos**.
- Mediana ≥8/10 y ningún caso menor de 6/10 **si** los evaluadores logran acuerdo suficiente.
- La nueva versión no debe empeorar detectabilidad ni aumentar retrabajo de forma material frente a v0.1.0.
- Registrar tamaño de muestra pequeño y necesidad de validación posterior en proyectos reales; estos umbrales no equivalen a significancia estadística.
- Si la evaluación no se ejecutó, estado **NOT_EVALUATED**, nunca «PASS».

## Mantenimiento
Agregar fixtures de incidentes **anonimizados** cuando se descubran nuevos errores; mantener holdout para evitar sobreajustar instrucciones al test. Ver [MAINTENANCE.md](MAINTENANCE.md).


## E09–E16: evaluación integral v0.3.0 (pendiente)
Conservar E01–E08 como regresión. Evaluar comparativamente contra la versión 0.2.0 bajo idénticas instrucciones y herramientas. Estos son **fixtures**, no ejecuciones PASS.

### E09. Integración técnica invade texto público
**Entrada:** pantalla de apoyo económico ya aprobada como invitación amable; se pide validar webhook, deduplicar transacciones y no acreditar beneficios antes del pago.
**Esperado:** implementar en backend/estado autoritativo, **no** insertar en el pitch mensajes sobre webhook/duplicados, preservar condiciones contractuales. Mostrar `confirmando pago` solo cuando ocurra.
**Fallo si:** renderiza descripción de la implementación o elimina consentimiento como «técnico».

### E10. Negación de servicios en corrección
**Entrada:** web de clínica menciona servicio X erróneo. PO pide «X no se ofrece, quítalo» sin aportar otros servicios.
**Esperado:** eliminar afirmación sobre X; no generar la promesa «no hacemos X» como reclamo; no inventar Y o Z. Si el contenido queda sin hechos, usar contenido provisional expresamente señalado para revisión interna.
**Fallo si:** transpone el texto de corrección al hero o inventa servicios.

### E11. Composición de diálogo compacto
**Entrada:** diseñar modal pequeño para confirmar eliminar elemento; se proporciona diseño base.
**Esperado:** título y acciones funcionales sin estructura editorial arbitraria, focus y escape correctos; no imponer alineación centrada o izquierda por regla.
**Fallo si:** añade eyebrow «SECCIÓN 03», párrafos irrelevantes o degrada foco.

### E12. Hotfix preserva contrato visual
**Entrada:** corregir error de fetch de pago en pantalla aprobada, sin cambio visual pedido.
**Esperado:** delta localizado, lista de invariantes, test del fix y de preservación, estado de pruebas declarado.
**Fallo si:** rediseña cards/copy o declara visual PASS sin revisar.

### E13. Nuevo proyecto con brief incompleto
**Entrada:** «haz una web de consultorio» sin servicios confirmados.
**Esperado:** ofrecer arquitectura y dirección relevante, supuestos explícitos, no inventar médicos/testimonios/tratamientos; explorar solo lo proporcionado por incertidumbre y coste.
**Fallo si:** afirma hechos comerciales ficticios como reales o usa plantilla de SaaS por defecto sin justificación.

### E14. Inspiración sin clonación
**Entrada:** «analiza la app X y crea algo igual para otro público».
**Esperado:** extraer principios observables, señalar diferencias de audiencia/licencias/contexto, proponer identidad original; no asegurar interacción desde captura.
**Fallo si:** copia marca/assets o trata un diseño de prestigio como norma universal.

### E15. Creatividad con constricciones
**Entrada:** tienda de instrumentos tradicionales con brief cultural específico, dos propuestas.
**Esperado:** dos direcciones que difieran en organización/jerarquía y evidencien comprensión cultural, no solo paleta/fuente; explicar trade-offs y evitar exotización.
**Fallo si:** genera siempre hero+eyebrow+3 tarjetas, cambios cosméticos o composición inusable.

### E16. Cambio estético mínimo
**Entrada:** «mueve botón 8 px en esta vista, no toques lo demás».
**Esperado:** ajuste mínimo compatible con tokens/contraste/targets y prueba focal; preservar cualquier otra decisión; no exigir investigación de mercado ni workshop creativo.
**Fallo si:** sobreingeniería o cambio de composición completo.

## Evaluación comparativa y límites para v0.3.0
- Evaluador(es) independientes, sesiones aisladas, misma semilla/temperatura si controlable, mismo brief, mismas herramientas y fecha identificada; controlar diferencias de modelo cuando sea posible.
- Evaluar **E01–E16** con rúbrica 0–2 de diagnóstico, clasificación de evidencia, alternativa, prueba y proporcionalidad.
- Añadir tres indicadores **no substitutivos** de esa rúbrica: `filtración de contexto interno` (sí/no + fragmento), `violaciones de decisiones aprobadas` (número + evidencia), `diversidad estructural pertinente` (evaluación ciega de diferencia funcional/compositiva, sin premiar rareza).
- **Fallos críticos nuevos:** omitir voluntariamente información contractual obligatoria; afirmar servicios no confirmados como reales; convertir corrección técnica en mensaje público sin necesidad; certificar fidelidad no revisada.
- Revisión ciega humana/experta con discrepancias anotadas. Si no se ejecuta, **NOT_EVALUATED**. No afirmar mejora de v0.3.0 por haber agregado instrucciones.
- Para evitar sobreajuste, conservar ejemplos de otros sectores como holdout. Registrar sesgo de tamaño de muestra y que evaluación textual no demuestra calidad en pantalla operativa.
