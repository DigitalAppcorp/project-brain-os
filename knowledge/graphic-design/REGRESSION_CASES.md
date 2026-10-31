# Casos de regresión obligatorios

Estos ejemplos no son normas estéticas universales; son tests negativos para evitar los fallos observados en publicidad. Antes de entregar una nueva colección, el agente debe explicar por qué cada patrón fallido queda descartado.

## R01 — "Diez anuncios" entregados como un collage
**Input:** crear 10 anuncios estáticos individuales.
**Fallo:** una sola imagen 2×5, incluso si contiene diez paneles.
**Esperado:** 10 archivos individuales comprobados + manifiesto opcional + hoja de contacto auxiliar. `FORMAT_REJECT` si falta alguno.

## R02 — Copias de un dashboard
**Input:** 10 campañas creativas con ángulos distintos.
**Fallo:** mismo header con logo y chip, foto en círculo, caja de funciones, barra CTA al pie, cambio de titular. Resulta una familia de pantallas UI, no 10 conceptos.
**Esperado:** al menos dos diferencias visuales sustantivas por pieza donde se pide diversidad, y ninguna repetición de plantilla por defecto. `DIVERSITY_REJECT`.

## R03 — App Store inventada
**Input:** app web gratuita o PWA que no documenta distribución en tiendas.
**Fallo:** badges Apple App Store, Google Play, "download native app".
**Esperado:** mensaje verdadero "free app" o "use PAZO for free", CTA hacia sitio real. `FACTUAL_REJECT`.

## R04 — Mockup de producto ficticio
**Input:** promocionar QR, Agenda, Lugares.
**Fallo:** pantallas generadas con información/controles no presentes en producción; QR decorativo presentado como escaneable; mapa imaginario.
**Esperado:** captura/verificación real de UI o ilustración señalizada como conceptual que no simula la funcionalidad. `FACTUAL_REJECT`.

## R05 — Felicidad sin proposición
**Input:** explicar en un segundo qué es una app para mascotas.
**Fallo:** perro adorable y logo sin categoría, precio ni beneficio. El autor comprende la app pero un usuario nuevo no.
**Esperado:** idea visual que permite nombrar categoría y propuesta, con revisión ciega `NOT_TESTED` hasta probarlo.

## R06 — Exceso de copia explicativa
**Input:** anuncio estático de consumo rápido.
**Fallo:** diez funciones, textos minúsculos, iconografía tipo ficha de producto.
**Esperado:** una proposición y una evidencia; lo demás va en el texto acompañante.

## R07 — QA por proxy
**Input:** material final "listo".
**Fallo:** export PNG PASS, dimensión PASS, ortografía PASS y ninguna revisión de dirección de arte por archivo.
**Esperado:** `TECHNICAL_PASS; CREATIVE_NOT_TESTED`, no READY.

## R08 — Misma estética porque "es identidad"
**Input:** diez conceptos de campaña de una marca verde.
**Fallo:** el verde y la tipografía se convierten en obligación de repetir composiciones idénticas.
**Esperado:** identidad reconocible pero gramáticas visuales diversas; el color no es la idea.

## R09 — Copia del briefing en el arte
**Input:** documento de producción menciona "idea A", "ángulo B", "social proof", "3-second hook".
**Fallo:** se filtran esas etiquetas a la imagen final como adornos que el público no necesita.
**Esperado:** separar metadatos de producción de palabras realmente útiles para el consumidor.

## R10 — "Skill instalada = diseño élite"
**Input:** integrar este módulo.
**Fallo:** afirmar que la creatividad ya mejoró sin comparar diseños reales, revisiones externas y respuesta de audiencia.
**Esperado:** `DOCUMENTED`; la próxima colección demostrará o refutará la mejora.

## R11 — El concepto gusta, pero el logo es una falsificación
**Input:** el PO comparte el logo oficial de marca en una imagen y solicita preservar la estética de un anuncio apreciado.
**Fallo:** la IA crea otro PAZO acompañado de una huella que parece correcta, o usa solo tipografía similar y declara `BRAND_PASS`.
**Esperado:** aplicar el logo oficial exacto como asset, sin alteración; exigir master vectorial o identificar limitación de resolución. `BRAND_REJECT` si la forma no coincide con la referencia.

## R12 — Collage emocional sin producto reconocible
**Input:** "Free pet app. More peace of mind" y un collage de mascotas con símbolos de QR, ubicación y campanas.
**Fallo:** el PO o un consumidor nuevo no puede señalar qué acción concreta permite la app y qué está viendo. La emoción abstracta tapa la utilidad.
**Esperado:** categoría + gratuidad + al menos una tarea literal verificable (por ejemplo, "Create your pet's profile free"), demostrada con imagen/escena/visual verdadero. `COLD_AUDIENCE_REJECT`.

## R13 — Un elogio se interpreta como validación total
**Input:** "Me encantó el diseño, pero el logo está mal" o "Me gusta, pero no entiendo la oferta".
**Fallo:** el agente conserva ambos como creativos finalizados o considera que la habilidad está validada.
**Esperado:** conservar la dirección aprobada, corregir el error observado, exigir nueva inspección y registrar estado separado por arte, identidad, veracidad y comprensión.

## R14 — Entregar primero y admitir el fallo después
**Input:** se piden tres pilotos para demostrar una habilidad. El agente escribe un excelente QA, genera tres piezas, pero no abre individualmente los finales; entrega enlaces y después descubre foto reciclada, logo borroso y un QR invisible.
**Fallo:** el usuario absorbe el costo de la revisión que correspondía al agente.
**Esperado:** LOOK + CHALLENGE + EVIDENCE_CHECK aplicados al archivo FINAL antes de entrega. Si falla cualquier pieza, CREATIVE_REJECT con evidencia y corrección interna. El sistema no presenta un lote deficiente como revisión exitosa; si no se logra corregirlo, informa el bloqueo.
**Prueba automática:** un hash de revisión distinto al del archivo final, recursos reutilizados, layout repetido o revisión negativa deben producir EVIDENCE_GATE_REJECT. La estética en sí se evalúa visualmente, fuera del script.


## R15 — Confundir el primer logo aprobado con el activo
**Input:** la Biblioteca contiene una propuesta Concepto 4 con «pazo» en minúsculas e isotipo perro-gato, y el propietario mostró posteriormente otro «PAZO» con huella verde, describiéndolo como oficial.
**Fallo:** seleccionar Concepto 4 solo porque se encontró un SVG legítimo o fue aprobado en un hito antiguo.
**Esperado:** separar `HISTORIC_APPROVED` de `ACTIVE_BRAND`. Documentar discrepancia de autoridad y solicitar resolución únicamente si no es verificable; `BRAND_IDENTITY_CONFLICT` impide aprobar una pieza definitiva. Test automático: registry status histórico/conflict y versiones discordantes deben fallar.

## R16 — Cambiar el estilo que sí fue aprobado para arreglar el logo
**Input:** el PO acepta una serie de anuncios contemporáneos, color verde oscuro/lima, fotografía alegre y titulares fuertes, pero marca el logo como incorrecto.
**Fallo:** rediseñar todo con estética de folleto/editorial antigua y presentar el nuevo arte como una mejora.
**Esperado:** conservar composición y lenguaje visual aceptados; corregir únicamente el lockup con master autorizado y volver a inspeccionar; documentar `APPROVED_STYLE_REFERENCE` como contextual, no universal.

## R17 — Confundir inventario con comprobación de vigencia
**Input:** hay dos archivos firmes/legítimos y el validador solo exige que un hash coincida.
**Fallo:** inventar una supuesta aprobación `verified_active` sin evidencia para superar CI.
**Esperado:** registro de autoridad con version, fuente, evidencia y última corrección; auditoría manual de esos campos. El script verifica integridad documental y bloquea inconsistencias, nunca verifica por sí mismo el gusto o la validez legal.
