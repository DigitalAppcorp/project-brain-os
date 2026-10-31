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
