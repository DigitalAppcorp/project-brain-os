# Graphic Design OS — ejecución y rechazo obligatorio (v0.3)

## Incidente que corrige
PAZO: tres pilotos se entregaron y solo después se reconoció CREATIVE_FAIL 3/3. Dos reutilizaron fotografías de anuncios anteriores; un supuesto QR no mostraba el mecanismo; el logo provenía de una referencia pequeña ampliada. La habilidad enumeraba reglas, pero **no exigía ejecutarlas antes de entregar**. El fallo es de la transición producción→revisión→entrega.

## Máquina de estados (obligatoria para anuncios)
1. BRIEF: categoría, función concreta, gratuidad, audiencia nueva, canal, pruebas del producto, formato, coste y derechos.
2. CONCEPT: dos o tres ideas visuales diferentes que respondan a objetivos concretos. La foto bonita no es una idea sin causalidad.
3. ASSET_PREFLIGHT: revisar imágenes rechazadas/anteriormente usadas y sus IDs; encontrar logo maestro autorizado. Si solo existe una captura borrosa, no declarar BRAND_PASS.
4. PRODUCE: una imagen por creatividad. Si el generador responde con collage cuando se pidieron archivos independientes, REJECT y reintentar sin declarar entrega.
5. LOOK: abrir **cada archivo FINAL**, a escala completa y de pantalla móvil, no solo un contact sheet ni el prompt. Comprobar que se vea la acción anunciada, logos exactos, texto natural, fotografía novedosa, recortes, jerarquía y ausencia de UI inventada.
6. CHALLENGE: escribir por cada imagen el **argumento más fuerte para rechazarla**, con evidencia observable. Si hay fallo crítico, CREATIVE_REJECT; la salida se corrige antes de mostrarla como candidata. No delegar el QA al PO.
7. EVIDENCE_CHECK: ejecutar scripts/validate_creatives.py contra manifest de los finales. Si falla, EVIDENCE_GATE_REJECT. Si pasa, confirma documentación técnica; NO certifica estética, fidelidad del logo ni respuestas humanas.
8. REVIEW_CANDIDATE: solo imágenes completas inspeccionadas, sin vetos. Mostrar como candidatas, sin afirmar validación de público si no hubo prueba externa.
9. PUBLICATION_READY: sumar evidencia externa real de comprensión con personas que no conocen la app, derechos de imagen, aprobación del PO y políticas del canal. Publicar/gastar exige autorización independiente.

## Manifest por colección
JSON con schema_version=1, requested_count (número exacto), prior_inventory_checked=true y prior_asset_ids (identificadores de las fuentes usadas en lotes rechazados; si no existen, registrar esa revisión honestamente).

Cada elemento creatives[] debe incluir:
- id, image (ruta relativa al directorio root) y sha256 del archivo FINAL.
- single_visual_idea (acción visual concreta), primary_medium (photography, expressive_typography, illustration, conceptual_collage, product_documentation o mixed_media), composition_signature, visual_rhetoric (diferenciación no cosmética).
- source_asset_ids (identificadores reales de las fotografías/ilustraciones originales); el verificador bloquea repetición dentro del lote y contra el inventario anterior.
- category_in_art=true, free_claim_in_art=true, specific_action_in_art=true **solo tras inspeccionar la imagen**, y fictitious_interface=false, unverified_claims=false **solo tras comprobar hechos**.
- brand: master_asset, master_sha256, exact_asset_composited=true y visual_match_checked=true. El logo se compone desde el original autorizado; no se pide a un generador que lo imite.
- visual_review: inspected_sha256 igual al archivo final, result=PASS/REVISE/REJECT, visible_evidence con observaciones concretas, strongest_rejection_reason con objeción sustancial.
- Para publish: blind_comprehension={status:TESTED, observed_answers:[...]} con respuestas reales, rights_verified=true y owner_approved=true.

Comando para un piloto completo:

    python knowledge/graphic-design/scripts/validate_creatives.py /ruta/manifest.json --root /ruta/creativos --target review

Para un lote publicable:

    python knowledge/graphic-design/scripts/validate_creatives.py /ruta/manifest.json --root /ruta/creativos --target publish

## Limitaciones, fraude y prevención
**El script no ve contenido semántico de las imágenes.** No puede comprobar que una palabra esté realmente impresa en el arte, que una cara no sea idéntica tras recomposición, que el logo se haya compuesto exactamente, ni verificar licencias o testimonios humanos. Los flags documentan la inspección responsable; inventarlos es un incumplimiento. Todos los PASS manuales deben corresponder a la imagen final inspeccionada. Un resultado EVIDENCE_GATE_COMPLETE no equivale a CREATIVE_PASS.

Si el arte no muestra ninguna acción del producto, una pieza falla aunque diga Free Pet App, aunque tenga buen color y aunque tenga un informe de 100 puntos. La validación de calidad artística sigue siendo un examen de imagen verdadera, no un score administrativo.

## Puerta para integrar en main
1. Pruebas de regresión técnicas (21) en GitHub CI.
2. Tres nuevas ejecuciones que usen activos distintos y logo maestro verificable, contrastadas con el lote fallido.
3. Inspección visual individual y prueba de comprensión externa documentada si se anuncia como apta para campaña.
4. Decisión explícita de integración del PO.

Mientras los tres nuevos pilotos no lo demuestren: DOCUMENTED_AND_GATED, NOT_ARTISTICALLY_VALIDATED. No crear otra serie de diez.


## v0.4 — Identidad antes de composición

**Nuevo paso obligatorio dentro de ASSET_PREFLIGHT:** cargar y validar [BRAND_ASSET_AUTHORITY.md](BRAND_ASSET_AUTHORITY.md). Cuando exista contradicción entre identidad histórica y la referencia que el propietario llamó oficial, bloquear `BRAND_PASS`, sin inferir que el logo original histórico es el vigente.

Migración del manifesto: `schema_version: 2` y `brand_registry` adicional con `brand_id`, `active_version`, `status=verified_active`, `authoritative_asset_id`, `master_asset`, `master_sha256`, `approval_authority`, `approval_evidence`, `usage_variant`, `conflict_resolution=not_applicable|resolved_by_owner`, `verified_against_latest_owner_feedback=true`. Cada objeto creative.brand incorpora `brand_id`, `active_version` y `usage_variant` idénticos al registro. Un arte con otro lockup queda rechazado aunque su hash sea consistente con algún archivo antiguo.

No falsificar `status`, `approval_evidence` ni la resolución del propietario para superar un gate automático. Estos campos son **declaraciones revisables**, no verificación criptográfica de autoridad.

**Preservación del arte aprobado:** cuando el único fallo del anuncio sea la marca, mantener fotografía, mensaje, composición y tono aprobados; hacer composición del logo maestro auténtico como capa independiente y comparar las imágenes antes/después. No convertir un defecto puntual de branding en un rediseño editorial sin encargo.
