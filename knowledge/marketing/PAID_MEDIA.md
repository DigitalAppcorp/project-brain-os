# Media buying — Meta, Google, TikTok y otros canales

## Principio
La plataforma optimiza hacia el **evento que recibe**: si aprende con clics o formularios de baja calidad, no necesariamente conseguirá compradores. Priorizar conversiones fiables, oferta, mensaje y señales downstream de CRM.

## Preflight antes de un dólar
1. Responsable y aprobación escrita del gasto, fechas y límite máximo.
2. Oferta válida, landing funcional/móvil, teléfono/WhatsApp, capacidad de respuesta.
3. Unidad económica: margen por venta, cierre estimado, CAC máximo tolerable y caja.
4. Eventos probados y deduplicados; enlaces UTM; plan de privacidad y consentimiento.
5. Cuenta/anunciante elegible; políticas de categoría especial; geografía e idioma; exclusiones correctas.
6. Registro de línea base, versiones y criterio de pausa.
7. No usar tarjetas, presupuesto ni campañas LIVE sin autorización expresa.

## Google Search
- Priorizar consultas con intención transaccional/comercial y geografía real; separar investigación y navegación cuando procede.
- Revisar términos de búsqueda, negativas, anuncios relevantes, landing y extensión de activos.
- Probar medición `generate_lead → qualify_lead → close_convert_lead` si CRM/GA4 lo permiten y está consentido.
- Smart bidding/Performance Max requieren señales y control de calidad: no se asume que automatización compensa tracking defectuoso.
- Para importación offline/enhanced conversions, comprobar **cambios de API**: documentación oficial reporta migración hacia Data Manager API desde 2026; no escribir integraciones basadas en tutoriales antiguos.
- Local Services Ads: comprobar categoría/ciudad/requisitos y modelo de cobro antes de recomendar.

## Meta (Facebook/Instagram)
- Diseñar oferta y conversión destino: formulario, web, conversación, compra o app, según posibilidad de **atribución y cierre**.
- Variar ángulos y creatividades antes de añadir segmentaciones innecesarias; estudiar la entrega real, no asumir que audiencias amplias siempre ganan.
- Pixel/Conversions API solo con gobernanza de consentimiento y **deduplicación event_id** si se usa doble envío (verificar implementación de proveedor).
- Evaluar calidad del lead con CRM, velocidad de respuesta y cierres, no únicamente `cost per lead`.
- Verificar opciones actuales de Advantage+, categorías especiales y limitaciones antes del lanzamiento.

## TikTok / video
- Creativos diseñados para el formato, gancho inicial, demostración y CTA; probar ángulos diferenciados.
- En 2025 TikTok recomendó formato vertical 9:16, música/diseño nativo, pruebas creativas continuas. Confirmar requisitos técnicos/políticas vigentes.
- No inferir compras de views, follows o guardados.

## Diseño de prueba
- Una hipótesis principal por prueba; controlar cambios de objetivo, público, oferta y creatividades para interpretar resultados.
- Antes: periodo, presupuesto máximo, definición de conversión, integridad de datos, umbral económico y guardrails.
- Durante: monitorizar disapproval, gasto, tracking, carga comercial y señales de fraude.
- Después: usar CRM, costes e ingresos verificados; registrar tamaño de muestra y limitaciones de atribución.
- Escalar solo con evidencia suficiente, capacidad y rentabilidad; pausas no requieren "rescatar" inversión hundida.

## Presupuestos pequeños
Evitar dividir poco gasto entre demasiados ad sets. La opción de **no comprar medios** (SEO local, referidos, outreach cálido, alianzas) es válida si no existe oferta contrastada o medición mínima.
No existe CPC, CPL, CPM, CTR o ROAS universalmente "bueno"; comparar con margen, ciclo y objetivo local, no con números inventados.

## Checklist de publicación
Owner aprobado / target verificado / copy legal / URL final / conversiones validadas / privacy / UTMs / frecuencia de revisión / kill-switch / rollback.
