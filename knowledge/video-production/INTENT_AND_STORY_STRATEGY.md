# Video OS v0.4 — Intención y estrategia de historia

**Obligatorio antes de storyboard, generación, edición, gasto y exportación.** Fuente del cambio: fallo PAZO 2026-10-29; el sketch «perro oye park» no justificaba la presencia de PAZO ni el objetivo comercial. La calidad cinematográfica no rescata una idea sin propósito.

## Contrato de intención: G0

Cada pieza debe tener un registro con estos campos, todos resueltos antes de producir:

- `audience`: persona y situación concreta; insight como `EVIDENCE` o `HYPOTHESIS`, nunca intuición disfrazada de dato.
- `business_goal`: descubrimiento / consideración / activación / retención / comunidad / educación / entretenimiento de marca.
- `audience_A_to_B`: de qué creencia, emoción o comportamiento a cuál queremos llevar al espectador.
- `single_takeaway`: una frase que deba recordar después de ver el video.
- `viewer_value`: recompensa real: humor, emoción, curiosidad, información útil, identificación o utilidad.
- `story_motor`: deseo del personaje, conflicto, acción, reacción, resultado; o progresión informativa equivalente.
- `brand_role`: cómo participa la marca: herramienta, evidencia, contexto, resolución o patrocinador explícito. `NONE` es válido para contenido independiente, pero no debe describirse como video de conversión PAZO.
- `product_proof`: funciones verificadas de la versión publicada, recursos reales con permiso y momentos de interacción necesarios.
- `hook_promise`, `payoff_delivery`: pregunta o promesa inicial y segundo en que se satisface honestamente.
- `next_action`: ver perfil, explorar demo, registrar mascota, regresar, compartir; o ninguna cuando el objetivo lo justifique.
- `primary_metric`: métrica coherente con objetivo, con unidad, ventana, denominador y disponibilidad real. `UNKNOWN` si no existe.
- `distribution`, `assets`, `rights`, `capacity`, `credit_quote`: restricciones comprobadas.

**Pitch obligatorio, máximo tres frases:** «Queremos que [audiencia] pase de [A] a [B]. Mostraremos [historia concreta] para producir [emoción/aprendizaje]. PAZO desempeña [rol real]; comprobaremos [señal]». Si solo se justifica con «viral», «video bonito», «tenemos IA», «hace falta publicar cinco», o «es gracioso», `INTENT_BLOCKED`.

## Arquitecturas narrativas: selección, no plantilla rígida

1. **Comedia:** situación reconocible → deseo → anomalía → reacción → escalada → remate.
2. **Microdrama:** deseo → obstáculo → elección → consecuencia → cambio.
3. **Demostración:** problema real → tarea en interfaz real → resultado observable → siguiente paso.
4. **Explicación:** pregunta → evidencia/contexto mínimo → descubrimiento → aplicación.
5. **Testimonio auténtico:** experiencia consentida → hecho verificable → resultado sustentado. Jamás crear usuarios ficticios.
6. **Pieza emocional/sensorial:** contraste → avance de sentimiento → cierre con significado.

No imponer una duración de hook, corte o CTA como ley universal. El montaje debe añadir información/emoción, no simular movimiento con textos. Un hook no puede prometer un payoff inexistente.

## Veto de marca y causalidad

Antes de autorizar G1:
- **Sin logo:** ¿la historia merece verse? Si no, la publicidad carece de recompensa.
- **Sin PAZO:** ¿la transformación deseada seguiría siendo idéntica? Para adquisición, si sí, la integración de marca es decorativa.
- **Sin rótulos:** ¿suceden acciones comprensibles? En narrativa de actuación, si no, reescribir.
- **Sustitución:** ¿podría cambiarse PAZO por cualquier marca sin alterar idea/valor? Advertir genericidad.
- **Persona ajena:** ¿entiende qué es PAZO sin conocer el proyecto? Si no, falla el mensaje aunque el chiste funcione.
- **Crítica previa:** escribir la razón más fuerte para *no* producir la idea y el coste de oportunidad de la generación.

## Caso de regresión PAZO

`REJECT`: perro oye «park» → mueve cola → recoge correa → end-card PAZO. Puede entretener, pero no demuestra ni explica el valor del producto.

`CANDIDATE DISCOVERY`: un momento real/actuado de mascota conecta orgánicamente con crear su perfil en PAZO, mostrando el perfil verdadero, sin likes, usuarios ni pantallas inventadas. Transformación: «no sabía que las mascotas podían tener su propio espacio» → «entiendo que PAZO permite crearles un perfil».

`CANDIDATE CONSIDERATION`: persona necesita elegir un lugar para pasear; se observa en la interfaz real de Lugares una búsqueda y apertura de lugar; el beneficio es comprensible. No atribuir recomendaciones personalizadas ni capacidades no verificadas.

`CANDIDATE RETENTION`: historia que representa un motivo real de volver, condicionada a que la función y actividad existan; no fingir comunidad poblada.

Esas propuestas son hipótesis narrativas, **no** greenlight para producir, pagar ni publicar.

## Métricas por intención

- Awareness: alcance y reconocimiento comprobable cuando exista estudio; vistas no prueban recuerdo de marca.
- Consideración: clics cualificados hacia demo/landing y rebote, atribución con UTM cuando exista.
- Activación: primeras mascotas / visitantes elegibles atribuidos, excluyendo administradores y QA.
- Retorno: usuarios elegibles que vuelven con ventana definida.
- Entretenimiento: retención, finalización, compartidos y señales cualitativas; no inferir usuarios registrados.

Separar `IDEA`, `EXECUTION` y `DISTRIBUTION`: cambiar múltiples a la vez es prueba exploratoria de portafolio, no experimento causal. No extraer conclusiones con muestras insuficientes. Usar `EXPERIMENTS_AND_MEASUREMENT.md`.

## Tres puertas antes de gastar

- `G0 INTENT`: transformación + valor + rol de marca + KPI coherentes. Sin puente causal, bloqueo.
- `G1 STORY`: beatboard causal, promesa cumplida, animatic/radio-cut según medio, revisión ciega de sentido sin texto. Si no funciona, reescribir.
- `G2 CAPABILITY`: actuación/filmación/pantalla real y derechos disponibles; prueba efectiva de 3–5 s para técnica de riesgo; cotización de créditos y autorización. Si falla, detener, no degradar a stock con rótulos.

Solo después se aplican los gates técnicos/creativos de `EDITORIAL_INTELLIGENCE.md`, `CREATIVE_EVIDENCE_GATE.md` y `QUALITY_AND_RIGHTS.md`. Un MP4 reproducible no constituye un video útil.

**Estados:** `INTENT_BLOCKED`, `SCRIPT_REWRITE`, `PRODUCTION_CANDIDATE`, `TECHNICAL_RENDER_VERIFIED`, `CREATIVE_REVIEW`, `VIDEO_READY_FOR_PUBLICATION` (solo con QA y derechos). Documentar una skill no equivale a entrenar pesos del modelo ni a validar competencia artística.