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

## Actualizaciones de plataformas verificadas (2026-11-01)

### Google Ads API v26.1 — 2026-10-28
[Release notes oficiales](https://developers.google.com/google-ads/api/docs/release-notes): nueva configuración de priorización de redes y topes porcentuales del presupuesto para redes secundarias, con comprobación de elegibilidad y valores por cuenta/campaña. **Antes:** este playbook no contemplaba esos controles. **Ahora:** cuando se gestione Google Ads mediante API, revisar elegibilidad y asignación de presupuesto por canal antes de recomendar cambios. Versión menor **sin breaking changes**; no migrar ni modificar presupuestos por el mero anuncio.

### Meta — anuncio oficial 2026-10-06 (omisión del baseline)
[Meta Advertising Week](https://about.fb.com/ltam/news/2026/10/advertising-week-new-york-2026-nuevas-capacidades-de-ia-para-guiar-campanas-y-llegar-a-los-clientes/): Customer Lifecycle Strategy está disponible para anunciantes y recomienda exclusiones de clientes existentes en campañas marcadas como adquisición; Advantage+ creative permite generar videos desde recursos estáticos. Ads Creative Studio está en despliegue; capacidades agénticas de cambio de campañas y tareas programadas están en pruebas. **Antes:** el playbook mencionaba Advantage+ sin separar estado de cada función. **Ahora:** confirmar controles visibles y permisos por cuenta, mantener creativos de marca aprobados y revisión humana antes de cualquier publicación, presupuesto o activación de automatizaciones. No confundir recomendación del proveedor con resultado comercial medido.

### TikTok — documentación actualizada octubre 2026 (sin día confirmado)
[Smart+ unificado](https://ads.tiktok.com/resources/help/article/how-to-create-a-campaign-in-the-upgraded-smart-experience): nuevo flujo con opciones manuales, parcialmente automáticas y totalmente automáticas para Sales, Lead Generation, App Promotion y Traffic, sujeto a disponibilidad de cuenta. [Recommended Creatives](https://ads.tiktok.com/resources/help/article/about-recommended-creatives-in-tiktok-ads-manager): sugerencias desde URL y biblioteca, generación IA y opción de autorizar adiciones/refrescos durante entrega. **Antes:** solo se documentaban pautas de creatividad 2025. **Ahora:** antes de lanzar, verificar qué automatización se activa, el permiso de refresco y los derechos de uso; no habilitar actualización automática sin aprobación del Product Owner.

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
