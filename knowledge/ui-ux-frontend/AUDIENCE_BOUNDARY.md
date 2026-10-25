# Frontera de audiencias — evitar filtración de instrucciones a UI

## Problema y límites
Durante vibe coding se mezclan peticiones del Product Owner, decisiones de ingeniería, restricciones de seguridad, requisitos legales, comentarios sobre bugs y mensajes para consumidores. **Una instrucción para construir/corregir no es automáticamente copy público.**

Llamamos provisionalmente `implementation-to-UI leakage` al fallo de convertir contexto interno de implementación en texto/ornamento visible sin justificación para la audiencia final. Es un **nombre operativo, no un diagnóstico científico establecido ni una causa neuronal demostrada**.

## Modelo de audiencias
- **Product Owner/cliente**: comunica intención, alcance, realidad del negocio, prioridades y aprueba.
- **Equipo de producto/IA**: convierte intención en decisiones, lógica, código, pruebas y documentación.
- **Usuario final**: desea entender, decidir, hacer o recuperar una tarea; no conoce tickets, prompts ni webhooks.
- **Otros actores** cuando existan: moderadores, soporte, administradores, personal clínico, reguladores, usuarios con tecnologías asistivas. Algunos sí necesitan detalles técnicos específicos en superficies adecuadas.

## Cuatro clases y regla de enrutamiento
| Clase | Ejemplo | Destino inicial |
| --- | --- | --- |
| Negocio real | `Membresía mensual 2,99` | copy público autorizado / lógica relevante |
| UX y comunicación | `Invitación cálida, no agresiva` | tono, composición, interacción |
| Legal/contractual | `Precio, renovación y consentimiento` | claridad y visibilidad pública necesaria; asesoría aplicable |
| Implementación/interna | `Idempotencia, webhook, orden duplicada, rollback` | backend, QA y documentación, NO copy automático |
Otros datos: secretos/PII no deben circular en copy, prompts persistentes ni logs abiertos.

## «Publicación» del contenido: gate antes de renderizar
Para cada frase, etiqueta, title, help text, toast, botón, error o sección:
1. **Identificar destinatario concreto y su estado de tarea.**
2. **Describir trabajo comunicativo:** orientar, informar, pedir decisión, prevenir error, explicar resultado, permitir recuperación o cumplir obligación.
3. **Probar exactitud** con fuente de verdad y tono del producto; sin inventar beneficios/condiciones.
4. **Verificar relevancia temporal y lugar**: información de «pago en verificación» puede ser necesaria DESPUÉS del pago, no en el pitch inicial.
5. **Eliminar o reformular** lo que sólo informa al constructor sobre el trabajo realizado.
6. **Comprobar accesibilidad/claridad**, especialmente advertencias contractuales.

### Prohibición inteligente, no censura
NO eliminar todos los textos técnicos; la interfaz de administración, diagnóstico, cuentas y soporte puede requerirlos. La decisión depende de **audiencia, contexto, necesidad y nivel de comprensión**.

## Ejemplo genérico — membresía
**Instrucción interna:** «No habilitar derechos hasta pago verificado; manejar abandono y eventos duplicados».
**UI previa a pago:** beneficios reales, precio/cadencia, renovación, consentimiento y acción clara.
**UI mientras se confirma:** «Estamos confirmando tu pago. Puedes consultar el estado aquí». Solo si ese estado ocurre.
**Backend:** idempotencia, estado autoritativo, reconciliación; jamás se resuelve mostrando un texto tranquilizador.
**Anti-patrón:** «No creamos órdenes duplicadas y verificamos webhooks antes de acreditar beneficios» como texto de venta.

## Correcciones conversacionales
Cuando el PO diga `no ofrecemos X`, actualizar primero la lista de hechos válidos y constraints; generar texto público NUEVO a partir de datos vigentes, no convertir «no X» en argumento de venta automáticamente.
Si el usuario necesita saber que X no existe para tomar una decisión segura, mostrarlo en contexto (disponibilidad/preguntas frecuentes), no negar por reflejo.

## Detección automática + revisión humana
Bandera roja si copy contiene jerga de implementación sin audiencia técnica: `webhook, RPC, deploy, optimista, rollback, PR, commit, duplicados de sistema, según tus instrucciones, hemos corregido`. **No es lista de palabras prohibidas**: investigar significado y contexto, no borrar acríticamente.
Otras señales: etiquetas «SECCIÓN 02» sin secuencia real; textos que anuncian cambios al PO; promesas añadidas durante fix técnico; disclaimers inventados para justificar arquitectura.

## Evidencia mínima de aprobación
`Elemento visible | audiencia | trabajo comunicativo | fuente del hecho | etapa/estado | tono aprobado | resultado`. Conservar solo para cambios significativos o copy crítico. Al revisar UI, comparar contra snapshot de mensajes originales y las instrucciones internas recientes.

## Validación
Prueba diferencial: generar pantalla bajo brief limpio, corrección negativa, corrección conversacional y contexto clasificado. Evaluador ciego anota filtración, inexactitud, pérdida de comunicación contractual y discrepancias; ver [EVALUATIONS.md](EVALUATIONS.md). No afirmar que la hipótesis está demostrada solo por la existencia del filtro.
