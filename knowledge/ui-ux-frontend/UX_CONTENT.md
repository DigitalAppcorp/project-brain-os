# UX writing — contenido que sirve al usuario, no al prompt

## Regla esencial
Las palabras son una parte de la interfaz. Antes de escribir una frase preguntar quién la leerá, qué sabe, qué necesita hacer y qué ocurrirá después. La especificación interna puede ser larga; el contenido público debe ser **útil, verdadero, claro y situado**.

## Jerarquía textual
- **Título de pantalla:** ubica a la persona en su tarea o estado; no es índice de documentación.
- **Título de módulo:** diferencia contenido relevante; no duplicar la etiqueta encima del título salvo valor real de agrupación/navegación.
- **Eyebrow, chip, numeración:** solo con utilidad semántica: categoría, secuencia real, filtro o estado, no como «adorno IA».
- **Descripción:** aporta información nueva para comprender, decidir o actuar; si repite título o explica implementación, recortar.
- **Acción:** verbo + resultado que ocurrirá; pagos deben reflejar coste, consentimiento y redirección cuando sea relevante.
- **Error/espera/éxito:** situación, consecuencia, recuperación o siguiente paso; no revelar RPC/webhook por defecto.
- **Texto contractual:** exactitud, visibilidad y claridad; el tono amable nunca sustituye información obligatoria.

## Proceso de generación
1. Extraer hechos confirmados y restricciones comerciales del repositorio/PO; marcar desconocidos.
2. Clasificar mensajes recibidos por destinatario con [AUDIENCE_BOUNDARY.md](AUDIENCE_BOUNDARY.md).
3. Elaborar inventario de mensajes `elemento → propósito → estado del flujo → hecho necesario`.
4. Redactar desde el vocabulario del público objetivo, sin jergas no necesarias.
5. Ejecutar revisión `relevancia + redundancia + coherencia tonal + exactitud + accesibilidad + localización`.
6. En cambios posteriores verificar no-regresión del tono y copy mediante [CHANGE_INTEGRITY.md](CHANGE_INTEGRITY.md).

## Antipatrón: corrección convertida en contenido
`PO: "No ofrecemos implantes"` → actualizar catálogo permitido; evitar publicar `"no hacemos implantes"` en hero salvo una necesidad real del paciente. El copy nuevo debe derivar del catálogo vigente, no copiar frase del chat.

## Antipatrón: seguridad interna anunciada
`Ingeniería: "evitar suscripción duplicada y acreditar tras webhook verificado"` → estado y lógica de sistema; no convertir automáticamente en explicación publicitaria. Si el usuario espera confirmación, mostrar `"Estamos confirmando tu pago"` cuando ocurra y explicar forma de comprobar estado.

## Control de voz
Registrar para cada producto: registro/tutear-usted, personalidad, verbos preferidos, nivel de cercanía, prohibiciones legítimas, legalese necesario y ejemplos aprobados. Aplicar al contexto concreto; una misma app puede tener tono cálido en invitación y directo/formal en consentimiento.

## Internacionalización y lectura
Comprobar expansión, traducciones, idiomas RTL si aplican, nombres accesibles y textos de botones completos. Evitar truncar condiciones esenciales; permitir lectura con zoom y lector. No presumir alfabetización técnica del usuario.

## Publicación
No confundir borrador con contenido validado. Servicios, beneficios, precios, fechas, opiniones o promesas sin fuente permanecen pendientes de confirmación. No «mejorar» copy añadiendo afirmaciones comerciales no verificadas.
