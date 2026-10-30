# Expert Evidence Protocol (EEP) — criterio de calidad transversal

**Versión del protocolo:** 1.0 · 2026-10-29 · **Estado:** contrato de trabajo DOCUMENTADO, eficacia todavía sin validar en operaciones reales.

**Autoridad:** complemento de `SKILL.md` (Project Brain OS) y de cada especialidad. Nunca sustituye autorizaciones, privacidad, seguridad, evidencias, producto aprobado ni el modo READ_ONLY_AUDIT. Su función es evitar respuestas convincentes pero equivocadas y entregas técnicas que no cumplen el objetivo humano.

## Propósito

Ante cualquier tarea, elevar el juicio del agente desde «puedo producir algo» hacia «¿es esto lo correcto, de calidad verificable, para este contexto?». La expresión «estándar del 1 %» sirve como **pregunta comparativa de oficio**, NO como acreditación, ranking real, entrenamiento del modelo ni garantía de resultados de élite. La mejor solución puede ser **NO HACER**, simplificar o postergar.

## Las cuatro preguntas obligatorias (adaptar profundidad)

1. **Referente experto:** ¿qué decisiones y pruebas esperaría de un especialista de alto nivel en esta tarea concreta? Definir errores y alternativas. No confundir el nombre de un famoso con un método, ni imponerse una estética/técnica por autoridad.
2. **Fuentes originales:** ¿qué material de primera mano necesitamos? Preferir código y runtime reales, documentación oficial y vigente, entrevistas y observaciones consentidas, métricas con denominadores, originales audiovisuales y brief aprobado. Recuperar datos disponibles antes de solicitar otros. Documentar procedencia, fecha, alcance y limitaciones. Nunca inventar inspección, observaciones ni credenciales.
3. **Método de trabajo:** ¿cuál es el proceso profesional adecuado y económico? Contrato de objetivo → opciones pertinentes → elección criticada → desglose ejecutable → implementación → revisión; respetar los gates del especialista. No agregar burocracia a tareas triviales.
4. **Prueba externa:** ¿qué evidencia falsaría nuestra propia conclusión? Medir contra criterios definidos **antes** del trabajo, y en el entorno relevante. Usar pruebas reproducibles y, cuando sea factible, evaluación por otro revisor/persona usuaria. **Una segunda pasada de la misma IA no equivale a una auditoría independiente**. Si no hay prueba externa, dejar `NOT_TESTED`, no inventar `PASS`.

## Ciclo EEP

`ENTENDER → INSPECCIONAR FUENTES → CRITERIO EXPERTO → DISEÑAR OPCIONES → DESAFIAR → EJECUTAR (si autorizado) → VERIFICAR → APRENDER`

### E0: encuadre y evidencia

- Describir resultado final (qué cambiará y **para quién**), criterio de aceptación observable, restricciones, autorización existente y costo/tiempo.
- Etiquetar afirmaciones: `OBSERVED` (inspección directa), `SOURCED` (fuente con fecha), `INFERRED`, `HYPOTHESIS`, `UNKNOWN` y `NOT_TESTED`. Una fuente de terceros no es una observación directa.
- Identificar el material original necesario y sus límites. Si el usuario entregó un recurso, utilizarlo de verdad o reconocer la imposibilidad; no reemplazarlo silenciosamente por una aproximación.

### E1: profesional, no ceremonial

- Recuperar principios y restricciones de la disciplina y del proyecto actual, separando buenas prácticas transferibles de preferencias particulares.
- Considerar cuando valga la pena al menos una alternativa real, incluida **mantener lo existente**, y la objeción más fuerte a la solución elegida.
- La pregunta crítica es: **¿qué podría demostrar que estamos equivocados?** Definir señal y umbral cuando haya datos suficientes; si no, indicar el límite de validez.
- No proponer más complejidad, controles, pantallas, personajes, servicios ni métricas sin necesidad causal.

### E2: ejecución y producto terminado

- Producir el entregable correcto para la solicitud, no una simulación de él: runtime para un bug, prototipo editable para diseño editable, secuencia audiovisual con actuación/sonido para video, resultados reales para una campaña.
- Preservar dependencias y alcance; integrar el método propio de Marketing, UI/UX, Video, Ingeniería o el dominio invocado.
- Mantener separadas `DOCUMENTED`, `CODED`, `TECHNICAL_PASS`, `CREATIVE_PASS`, `USER_ACCEPTED`, `HOSTED_VERIFIED` y `OUTCOME_MEASURED`. Ninguna transición es automática.
- Exigir permisos vigentes antes de despliegue, gasto, cuentas externas, datos personales, producción o acciones irreversibles; documentación o análisis nunca autoriza mutaciones.

### E3: revisión contradicente y evidencia

- Contrastar el resultado con el **objetivo inicial**, la fuente original y los riesgos. Buscar activamente un motivo concreto para rechazarlo; registrar defectos, severidad, evidencia y arreglo.
- Diferenciar la **autocrítica** (segunda pasada interna), revisión técnica externa, evaluación humana y comportamiento real de audiencia/usuarios. No presentar una como otra.
- Decisión: `PASS_VERIFIED` (evidencia suficiente para el gate exacto), `REVISE`, `REJECT`, `BLOCKED`, `NOT_TESTED`. El estado requiere método y alcance; no permitir «calidad élite: PASS» por decreto.
- Ante una contradicción de datos reales, corregir o retirar la hipótesis previa. Registrar aprendizaje aplicable y su límite; nunca declarar que cambiar un documento alteró los pesos del modelo.

## Profundidad proporcional

| Nivel | Cuándo | Exigencia mínima |
| --- | --- | --- |
| **LIGHT** | Consulta simple, texto menor, modificación reversible y localizada | Objetivo, hecho/fuente pertinente, respuesta, una verificación puntual. Sin formularios ni informes artificiales. |
| **STANDARD** | Funcionalidad nueva, nueva pantalla, anuncio creativo, propuesta de marketing, presupuesto no comprometido | E0–E3: fuente, alternativa, principal objeción, artefacto y revisión observable. |
| **CRITICAL** | Pagos, seguridad, privacidad, producción con datos reales, inversión publicitaria, cambios irreversibles, decisiones de gran coste | Auditoría de fuentes originales, pruebas específicas, fallo/rollback, revisión especializada y autorización explícita. No publicar con pruebas incompletas. |

El modo no modifica otras aprobaciones ya establecidas. En un trabajo de alto impacto, el coste de **no verificar** es parte del análisis.

## Interpretación por especialidad

| Especialidad | Material original imprescindible | Prueba de éxito / veto específico |
| --- | --- | --- |
| **Brain OS / producto** | Definición de valor, decisiones/versiones actuales, roadmap, backend/usuarios reales según corresponda | Producto entrega el ciclo de valor; gates, regresiones, fuente de verdad y permisos coherentes. No cerrar scope por CI únicamente. |
| **PAZO / desarrollo** | `AGENTS.md` vigente, código/HEAD, runtime, Supabase, pruebas y métricas separadas por QA/admin, según tarea | No atribuir visita del administrador a usuario real; prueba de ruta completa; ninguna afirmación de conversión/cobro sin evidencia verificable. |
| **Marketing** | Ads reales, presupuesto y gasto, plataformas, analytics/CRM con periodo y denominador, oferta verdadera | Conversión y resultado de negocio según objetivo; separar CTR de registros y de clientes; reconocer campaña fallida. No vender «aprendizaje» como retorno económico. |
| **UI/UX** | Pantalla original real y estados, tarea de usuario, métricas/research, diseño existente y decisión aprobada | Vista y flujo reales accesibles, estados async, legibilidad, contraste, mobile, accesibilidad; revisión visual contextual. No confundir CSS correcto con UX aceptada ni hacer UI «para el creador del prompt». |
| **Video** | Guion literario/técnico, referencia audiovisual, actores/personajes, escenario, diálogo, música/efectos, producto real, licencias | Intención y causalidad, actuación, montaje, audio, derechos y visionado completo. Un MP4 renderizado, un personaje modelado o música de fondo no demuestran narrativa. |

El contrato se extiende a otros trabajos por analogía con su oficio real (documentos, finanzas, restaurantes, nuevas apps), **sin copiar preferencias específicas de PAZO**.

## Contrato compacto de salida para trabajo no trivial

`Objetivo / Hechos y fuente / Hipótesis o faltantes / Método y decisión / Principal objeción / Evidencia de verificación / Estado y siguiente acción`.

No publicar esta ficha como interfaz final, copy de anuncio, título visual o texto para usuarios del producto. Se usa **internamente** para decidir y revisar. La explicación al Product Owner debe ser concisa y enfocada en resultados.

## Límites importantes

- La «experticia» evocada, citas de autores, prompts largos y etiquetas grandilocuentes **no garantizan capacidad ni calidad**.
- Un test estático solo valida estructura/reglas, no el efecto sobre usuarios ni el nivel artístico.
- La retrospectiva no debe reescribir métricas ni etiquetar una hipótesis como evidencia.
- No ejecutar tareas no autorizadas por el solo hecho de que una revisión recomiende mejorarlas.
- Evitar rituales costosos: si EEP aumenta tiempo sin mejorar decisiones o calidad medida, **simplificar o retirar** el proceso.

## Evaluación de la mejora

Comparar tareas futuras similares **con y sin protocolo** cuando sea viable: fallas de aceptación, retrabajo, pruebas omitidas, tiempo/coste y resultados de usuarios o negocio. Documentar contraejemplos; un éxito aislado o el merge del protocolo no constituyen validación de su eficacia.

**Casos de regresión:** [EXPERT_EVIDENCE_FIXTURES.md](EXPERT_EVIDENCE_FIXTURES.md).
