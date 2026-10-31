# Graphic Design OS — localización sin rediseño

## Regla general
La lengua de revisión del propietario y la lengua de publicación son variables distintas, sin cambiar los principios de la habilidad. PAZO: **presentar primero los anuncios en español** para la revisión del Product Owner; si posteriormente pide inglés, **adaptar los mismos artes al inglés**, no cambiar de estilo, fotos, logos ni hipótesis.

## Flujo
1. Registrar `creative_id`, `art_master` y `review_locale=es`, más `publication_locale` cuando se autorice.
2. Componer fondos/fotografías sin texto ni logo inventado. Logotipo original autorizado como capa separada.
3. Redactar titulares, subcopy, CTAs y disclaimers en español natural. Revisar puntuación, tildes y legibilidad a escala de feed.
4. Cuando pidan inglés, conservar la idea visual, el encuadre y los assets. Adaptar jerarquía/longitud tipográfica sin traducir literalmente expresiones poco naturales. Mantener la misma oferta, gratuita o de pago, y las mismas restricciones funcionales.
5. Revisar cada arte final: **todos los textos visibles** deben estar en el idioma solicitado, incluso etiquetas, cartas, supuestos botones, fondo y textos que se escondieron bajo retoques. Rechazar *ghost text* o halos procedentes de la versión previa. No generar interfaces ficticias para localizar un pantallazo real; usar capturas oficiales del producto en el idioma correspondiente.
6. Registro de versiones `AD-01/es/v1`, `AD-01/en/v1`; comparar equivalencia de claims y layout. Una traducción no es un experimento creativo nuevo.

## Regresiones
- L01: entregar EN cuando el PO pidió ES -> FAIL.
- L02: “ahora en inglés” provoca creatividad totalmente nueva -> FAIL.
- L03: CTA permanece en otra lengua -> FAIL.
- L04: texto previo fantasma bajo parches -> FAIL.
- L05: traducción inventa beneficios adicionales -> FACTUAL_REJECT.
- L06: logo cambia entre idiomas -> BRAND_REJECT.

No afirmar que un script valida idioma/arte con exactitud; exige inspección visual del archivo final.

## Estado y ámbito
Es instrucción reutilizable, no reentrenamiento de pesos. No almacenar creativos ni fotografías PAZO en el repositorio de Brain OS.
