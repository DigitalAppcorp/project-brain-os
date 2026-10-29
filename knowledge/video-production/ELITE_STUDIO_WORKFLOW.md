# Video OS v0.4 — Sistema operativo de productora: ejecución editorial de principio a fin

**Principio rector:** ninguna técnica, herramienta, presupuesto ni cantidad de entregables antecede a la intención. Se lee tras INTENT_AND_STORY_STRATEGY.md y antes de EDITORIAL_INTELLIGENCE.md.

## Organigrama funcional (una IA puede coordinar, no puede auto-certificar)

| Departamento | Autoridad y entregable | Veto |
|---|---|---|
| Estrategia / investigación | Audiencia, necesidad, objetivo y KPI, fuentes y segmentación | Marca decorativa, métrica de vanidad |
| Dirección creativa | 3 ideas significativamente distintas, logline, razón para existir, selección crítica | Idea genérica o desconectada |
| Guion / story editing | Causa→acción→reacción→consecuencia, beatboard, payoff | Historia sin cambio |
| Arte / casting / dirección | Personaje, mundo, estilo, model sheets, casting, expresiones, encuadres | Inconsistencia de identidad y acting falso |
| Producción | Derechos, disponibilidad de actores/escenarios/UI, desglose de coste, plan de rodaje/generación | Promesa no ejecutable o gasto no autorizado |
| Picture editing | Selects, assembly, rough cut, ritmo, cortes motivados, A/B cuando informativo | Plantilla sin narrativa |
| Sonido | Diálogo, música licenciada, sonido directo, SFX causal, silencio, mezcla | Voces ilegibles y ruido que sustituye actuación |
| Color y acabado | Iluminación, look, estabilización, legibilidad, export y QA | Aspecto infantil/no deseado, artefactos, safe area |
| QA independiente | Revisión completa de **video reproducible**, con/sin audio, derechos y producto | Derecho a REJECT con pruebas y timecodes |
| Analítica | Instrumentación, publicación con permiso, lectura de resultados y aprendizaje | Atribución inventada o muestra insuficiente |

## Pipeline con entregables obligatorios

**P0. Intake y auditoría:** recuperar Brain OS/Design OS/Marketing OS y el producto, historial de feedback, presupuesto, audiencia real. Si faltan datos, UNKNOWN.

**P1. Intent brief / G0:** objetivo primario, público, A→B, valor, brand bridge, KPI y riesgo, según INTENT_AND_STORY_STRATEGY.md. Sin propósito se cancela la idea, NO se pasa a render.

**P2. Ideación:** crear al menos tres tratamientos distintos en mecanismo (comedia situacional, demo funcional, historia emocional...), no tres textos sobre el mismo clip. Para cada uno: one-liner, ventaja, riesgo, razón para NO hacerlo. Elegir por claridad, singularidad, pertinencia, viabilidad y costo; puntuaciones no sustituyen juicio.

**P3. Guion y previs:** guion literario (qué ocurre) y guion técnico (cómo se ve/oye), beat sheet, storyboard o animatic, shotlist con función narrativa, mapa de audio, continuidad, punto de la marca y CTA. Hacer mesa de lectura/visión ciega. Una escena debe explicarse en acciones sin rótulos.

**P4. Factibilidad / G2:** rights ledger, asset map, cámara/micrófonos/animación/UI reales, permisos, modelo y precio estimado. No gastar créditos de terceros sin preflight y autorización adecuada. Realizar 3–5 segundos de la acción más difícil de la pieza. Si no se puede actuar, cambiar tratamiento previa justificación, sin fingir la técnica.

**P5. Producción de material:** rodar/generar con coherencia de personajes, set, luz, voz, mirada, dirección espacial, ropa y producto. Registrar versión, prompt, frame, seed/config si existe, asset IDs, licencias. Animación: poses clave → anticipación → acción → reacción → asentamiento; los ojos y el peso narran. No confundir escena 3D en viewport con video terminado.

**P6. Edición:** seleccionar tomas por significado, assembly, rough cut. Antes del polish comprobar promesa, claridad causal y payoff; recortar o regrabar en vez de cubrir fallos con música, stock, subtítulos o transiciones. Marcar cada empalme: emoción / revelación / reacción / avance / ironía / sonido / orientación. La pausa puede ser más valiosa que un jump cut.

**P7. Sonido y acabado:** diálogo inteligible, ambiente, música y SFX autorizados, pausas con intención; color y consistencia de personaje; texto legible solo cuando suma, subtítulos verificados, formato y safe areas del canal concreto, comprobación de visual sin sonido.

**P8. Screening / gates:** ver pieza completa a velocidad real, tamaño móvil, audio on/off. QA por timecode: 0–inicio, primer cambio, peor transición, payoff, final. Audio escuchado, frame consistency, product truth y derechos. Si el QA no puede reproducir o ver el archivo, marcar NOT_EVALUATED; nunca asumir PASS a partir de ffprobe. Revisor formula argumento más fuerte para rechazarla y prueba de espectador no iniciado cuando exista.

**P9. Handoff y release:** proyecto editable, archivo exacto, evidencias, fuentes, derechos, versión, costo, logs de QA, veredicto. Solo usuario autoriza publicación y/o gasto. Archivo verificable ≠ publicación aprobada.

**P10. Analítica y aprendizaje:** hipótesis, tracking disponible, períodos comparables, creatividades y segmentos, curva por timecodes, CTR, visita→registro→primera mascota cuando exista, exclusión de QA/admin. Diferenciar correcciones del contenido de distribución; datos escasos = INCONCLUSIVE.

## Reglas de rechazo rápido (hard-stop)

- `INTENT_BLOCKED`: video sin A→B, sin valor o con marca pegada.
- `CAPABILITY_NOT_DEMONSTRATED`: se prometió acting/3D/product demo sin filmación o flujo real demostrable.
- `STORY_FAIL`: el espectador no entiende deseo, conflicto o payoff / tutorial no logra resultado.
- `ART_DIRECTION_FAIL`: look no alcanza brief, uncanny, errores de patas/cuerpos, continuidad rota.
- `AUDIO_FAIL`: pista no escuchada, voz ininteligible o música sin licencia.
- `BRAND_TRUTH_FAIL`: UI inventada, usuarios ficticios, testimonio/resultado no sustentado.
- `DIVERSITY_FAIL`: cinco variantes comparten plantilla visible pese a claims de estilos diferentes.
- `DELIVERY_FAIL`: enlace inexistente, MP4 no verificado, assets faltantes.
- `AUDIENCE_UNKNOWN`: nunca declarar éxito sin datos de publicación.

**Regla de prestigio:** si el propio director no recomienda publicar un entregable solicitado para publicación, NO debe entregarlo como tarea cumplida. Documentar rechazo interno y producir alternativa solo si existe una ruta razonable, autorizada y viable; no multiplicar pruebas mediocres.

## Cómo se valida una productora, no solo una habilidad

Rúbrica editorial de EDITORIAL_INTELLIGENCE.md es revisión subjetiva, no señal de mercado. Auditoría independiente y derechos son obligatorios. Para el primer lote, validar cada gramática audiovisual por separado y comparar diferencias visibles antes de escalar. `SKILL_DOCUMENTED` no demuestra actuación de personajes, narrativa ni que un anuncio funcione; `SKILL_BEHAVIOR_VALIDATED` requiere casos de prueba; `PILOT_QA_PASS` requiere visionado y escucha reales, producto y derechos.

**Salida mínima por video:** brief de intención + guion/beatboard + shotlist/motivos de cortes + mapa de audio + asset/rights ledger + coste + prueba de acting + enlaces reales a final editable/MP4 + QA timecoded + hipótesis/métrica + permiso de publicación.