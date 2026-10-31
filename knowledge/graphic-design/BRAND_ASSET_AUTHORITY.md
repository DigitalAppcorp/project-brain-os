# Brand Asset Authority — v0.4 (evitar logotipos históricos como vigentes)

## Incidente observado en PAZO
La investigación de Biblioteca y repositorio recuperó:
- **Concepto D / 4** de octubre de 2026: isotipo perro-gato, lettering «pazo» en minúscula; documentación histórica y trazados vectoriales en el splash del producto.
- **Referencia posterior presentada por el Product Owner como logo oficial:** «PAZO» con huella verde, visible en material suministrado durante la revisión de anuncios.
Ambas representaciones NO son el mismo lockup. La existencia de un vector de alta calidad o de un archivo creado primero NO demuestra vigencia. La aprobación de una propuesta histórica NO aprueba automáticamente su reutilización cuando hay otra referencia más reciente que el PO llama oficial.

**Resultado en PAZO: BRAND_IDENTITY_CONFLICT — bloquea certificación y publicación, NO bloquea explorar conceptos sin marca.** No resolver por estética, fecha de creación aislada, preferencia del agente o suposiciones sobre qué figura en splash. Obtener resolución mediante una declaración explícita del propietario o un documento de marca vigente suficientemente autorizado. No reabrir una decisión ya explícitamente confirmada.

## Contrato de registro de marca
Antes de declarar un diseño BRAND_PASS o publicable, exigir registro activo:
- `brand_id` y `active_version` inequívocos.
- `status=verified_active`; no `legacy`, `draft`, `conflict` ni `unknown`.
- `authoritative_asset_id`: referencia exacta a archivo oficial de origen, no a una aproximación generada.
- `master_asset` y `master_sha256`: asset materializado y fingerprint de sus bytes.
- `approval_authority`: quien aprobó la versión activa; `approval_evidence`: documento, contexto o decisión precisa verificable; `approval_date` cuando se conozca.
- `conflict_resolution`: `not_applicable` o `resolved_by_owner`; si hay fuentes en conflicto sin resolución, `unresolved` y el gate debe rechazar.
- `usage_variant`: variante autorizada (horizontal, blanco, oscuro, etc.) y su contexto de color. No recolorear ni reconstruir tipografía sin autorización.
- `verified_against_latest_owner_feedback`: declaración explícita de comprobación de que la identidad no contradice una corrección posterior del PO.

### Jerarquía de evidencia
1. Decisión explícita del PO sobre el logotipo **vigente** para el trabajo que se está haciendo.
2. Registro oficial de identidad con versión, validez y variantes aprobado.
3. Implementación actual verificable y activos originales del producto.
4. Propuestas históricas aprobadas para su contexto, sin prueba de vigencia.
5. Ejemplos de anuncios generativos, capturas pequeñas o reconstrucciones aproximadas: **no son autoridad de marca**.

Si los niveles 1–3 discrepan, no elegir automáticamente; documentar conflicto y, cuando sea verdaderamente indispensable, solicitar solo la resolución de identidad faltante. El criterio de precedencia busca respetar la intención del propietario, no afirmar que un gráfico que se dijo oficial es original.

## Métodos correctos de composición
Separar dos capas:
1. **Imagen principal / escena**: fotografía o ilustración, sin texto ni logos generados cuando se requiera exactitud absoluta.
2. **Brand lockup**: colocar logo original verificado como una capa independiente, con SVG/raster original apto para la resolución. Exportar y revisar el render final. No pedir a un generador que dibuje el logo y no aceptar un texto PAZO similar.

Para una marca antigua y una nueva coexistentes (splash vs campaña), registrar `scope` de aprobación: `brand_global`, `campaign_only`, `product_legacy` o `unknown`. **No inferir que el splash actual autoriza reutilización comercial de la identidad anterior**, ni que el creativo con paw sustituye automáticamente todos los activos del producto.

## Conservación del aprendizaje creativo
Feedback del PO: la última ronda de anuncios con verde oscuro intenso, lima, titulares de alto impacto y fotografía alegre «ya me gusta más», con reserva por logo incorrecto. **Se aprueba condicionalmente el lenguaje visual; no se aprueba el logo ni la eficacia publicitaria.**
- Congelar las decisiones visuales aceptadas como `APPROVED_STYLE_REFERENCE` para la siguiente iteración **solo en este proyecto/contexto**.
- Hacer un `LOGO_ONLY_CORRECTION` sobre el último arte cuando sea técnicamente posible. No reemplazar fotografía/jerarquía/copy sin necesidad.
- Mantener opciones visuales diferentes para probar hipótesis distintas; coherencia de color NO equivale a clonación obligatoria.
- No convertir el estilo aprobado para PAZO en preferencia estética universal del Graphic Design OS.

## Gating
Para manifest schema_version=2, validador exige un `brand_registry` con estado y procedencia activos, y `brand` de cada creatividad ligado al mismo asset/version. Si solo se encuentran archivos históricos, el estado es `BRAND_IDENTITY_CONFLICT` o `BRAND_UNVERIFIED`, no `PASS`.

**Limitación:** hashes y flags de manifest no verifican por sí solos que la autoridad, las fechas o el recorte dentro de una imagen sean correctos. Se requiere comprobación visual y correspondencia documental; no fabricar `approval_evidence`.
