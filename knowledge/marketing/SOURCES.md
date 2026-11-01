# Fuentes primarias y registro de conocimiento

Última revisión de enlaces/documentos: **2026-11-01** (baseline anterior: 2026-10-23). No significa que cada página haya sido actualizada por el proveedor ese día. Priorizar página oficial > documentación técnica > guía de producto > estudio independiente > opinión. Cada decisión de campaña debe verificar vigencia en el momento de uso.

| Área | Fuente oficial | Para qué utilizarla | Riesgo de cambio |
| --- | --- | --- | --- |
| SEO y AI Search | [Google AI features](https://developers.google.com/search/docs/appearance/ai-features) | SEO válido para AI Overviews / AI Mode; no requisitos especiales de optimización | medio |
| Contenido SEO | [Google Helpful Content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | Originalidad, calidad, personas primero | medio |
| Técnica SEO | [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) | Rastreo, estructura e indexación | medio |
| Generación de leads | [Google Ads local lead generation](https://business.google.com/us/resources/articles/lead-generation/) | Journey, búsqueda local, calidad de lead, LSA | alto |
| Leads y CRM | [Google Ads lead generation](https://business.google.com/us/accelerate/resources/articles/generate-leads/) | Conversiones que llegan a venta, canales y automación | alto |
| Conversiones offline | [Enhanced conversions / Data Manager API](https://support.google.com/google-ads/answer/14274408) | Integraciones: migración 2026, ajustes de implementación | **muy alto** |
| GA4 | [Set up events](https://developers.google.com/analytics/devguides/collection/ga4/events) | Taxonomía, DebugView, key events | medio |
| GA4 referencia | [Recommended Events](https://developers.google.com/analytics/devguides/collection/ga4/reference/events) | sign_up, generate_lead, close_convert_lead, purchase | medio |
| Meta Ads | [Meta Advantage+](https://www.facebook.com/business/ads/meta-advantage-plus) | Automatización y objetivos (verificar opciones regionales) | alto |
| Meta API | [Meta Conversions API](https://developers.facebook.com/docs/marketing-api/conversions-api/) | Envío de eventos; volver a verificar permisos y deduplicación | **muy alto** |
| TikTok creatividad | [TikTok Creative Best Practices](https://ads.tiktok.com/resources/help/article/creative-best-practices?lang=es) | Video nativo, hooks, pruebas; documento con actualización 2025 | alto |
| FTC publicidad | [FTC Advertising and Marketing](https://www.ftc.gov/business-guidance/advertising-marketing) | Veracidad de claims y obligaciones | medio |
| FTC reseñas | [FTC Reviews and Testimonials Rule](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers) | Reseñas falsas, compensaciones y testimonios | medio |
| FTC endorsements | [FTC Endorsements](https://www.ftc.gov/business-guidance/advertising-marketing/endorsements-influencers-reviews) | Influencers y relaciones materiales | medio |
| California privacidad | [CPPA Regulations](https://cppa.ca.gov/regulations/) | CCPA/CPRA, vigencia y reformas | **alto** |
| Google Ads API / presupuestos | [Release notes v26.1](https://developers.google.com/google-ads/api/docs/release-notes) | 2026-10-28: priorización de canales y límites de presupuesto por red, sujetos a elegibilidad; versión menor sin breaking changes | alto |
| Google Search / UGC | [Prevent user-generated spam](https://developers.google.com/search/docs/monitor-debug/prevent-abuse) | 2026-10-26: indexación selectiva de páginas compartidas, moderación y vigilancia de abuso en Search Console | alto |
| AI Search / control de entrenamiento | [Google: shared AI training control](https://developers.google.com/search/blog/2026/10/ai-training-control) | 2026-10-30: propuesta de señal compartida en robots.txt, soporte previsto para 2027; no vigente todavía | medio |
| Meta Ads / automatización | [Meta Advertising Week 2026](https://about.fb.com/ltam/news/2026/10/advertising-week-new-york-2026-nuevas-capacidades-de-ia-para-guiar-campanas-y-llegar-a-los-clientes/) | 2026-10-06: Customer Lifecycle Strategy general, video IA desde estáticos; otras funciones en despliegue o prueba | alto |
| TikTok Ads / Smart+ | [Upgraded Smart+](https://ads.tiktok.com/resources/help/article/how-to-create-a-campaign-in-the-upgraded-smart-experience) | Documento actualizado octubre 2026 (día no especificado): flujo manual/automatizado unificado, disponibilidad por cuenta | alto |
| TikTok Ads / creatividades | [Recommended Creatives](https://ads.tiktok.com/resources/help/article/about-recommended-creatives-in-tiktok-ads-manager) | Documento actualizado octubre 2026 (día no especificado): sugerencias y generación IA, con autorización para refresco durante entrega | medio |
| California / privacidad | [CalPrivacy: SB 923](https://privacy.ca.gov/2026/09/california-expands-privacy-protections-by-strengthening-deletion-rights/) | Ley firmada 2026-09-27, vigente desde 2027-01-01; derecho de supresión ampliado y vía online para solicitudes, si aplica CCPA | muy alto |

## Hallazgos verificados a la fecha de registro
1. Google recomienda contenido útil, original y para personas; reglas SEO fundamentales siguen aplicando a superficies con IA.
2. GA4 modela eventos, incluidos `generate_lead`, `close_convert_lead`, `sign_up`; definición y configuración requieren comprobación.
3. Ayuda de Google Ads indica cambios 2026 para subidas offline/enhanced lead conversions hacia Data Manager API: revisar antes de integrar.
4. TikTok recomienda experimentación creativa continua y formatos adaptados al canal; sus recomendaciones son puntos de partida, no garantías.
5. FTC prohíbe publicidad engañosa y regula reseñas/testimonios falsos; California tiene reglas de privacidad con cambios efectivos en 2026.
6. Meta Advantage+ y CAPI son capacidades del proveedor; el diseño detallado se verifica al implementar, no se da por confirmado desde enlaces del catálogo.


## Revisión de novedades materiales — 2026-11-01

Comparación contra el baseline de 2026-10-23. Las fuentes de Meta (2026-10-06) y California (2026-09-27) son **omisiones relevantes del baseline**, no anuncios nuevos posteriores a ese día. Las novedades posteriores verificadas son Google Search (2026-10-26 y 2026-10-30) y Google Ads API v26.1 (2026-10-28). Los documentos de TikTok solo muestran el mes de actualización (octubre 2026): **no se infiere día ni lanzamiento universal**.

- Google Ads API v26.1: la priorización y los topes de presupuesto entre redes pueden modificar decisiones de media buying en cuentas elegibles. No se deben activar automáticamente. [Notas oficiales](https://developers.google.com/google-ads/api/docs/release-notes).
- Google Search: para plataformas con contenido generado por usuarios, decidir explícitamente qué páginas deben indexarse, aplicar controles de abuso y monitorizar Search Console. [Actualización oficial](https://developers.google.com/search/updates).
- Control de entrenamiento IA: propuesta de interoperabilidad para 2027, no instrucción para modificar robots.txt ahora. Distinguir entrenamiento de IA, búsqueda e inclusión en respuestas de Gemini. [Anuncio oficial](https://developers.google.com/search/blog/2026/10/ai-training-control).
- Meta: Customer Lifecycle Strategy permite recomendaciones de exclusión de clientes existentes para campañas de adquisición; la generación de video desde imágenes está disponible en Advantage+ creative. Las capacidades agénticas descritas siguen en prueba y requieren aprobación humana. [Anuncio oficial](https://about.fb.com/ltam/news/2026/10/advertising-week-new-york-2026-nuevas-capacidades-de-ia-para-guiar-campanas-y-llegar-a-los-clientes/).
- TikTok: Smart+ y creatividades recomendadas pueden cambiar el flujo de creación y la autorización de actualizaciones automáticas; verificar controles concretos de cada cuenta antes de publicar. [Smart+](https://ads.tiktok.com/resources/help/article/how-to-create-a-campaign-in-the-upgraded-smart-experience), [creatividades](https://ads.tiktok.com/resources/help/article/about-recommended-creatives-in-tiktok-ads-manager).
- California: SB 923 amplía derechos de supresión y exige vía online para solicitudes en negocios cubiertos, con entrada en vigor 2027-01-01. Determinar aplicabilidad por separado; **no** asumir que todas las empresas pequeñas están cubiertas. [CalPrivacy](https://privacy.ca.gov/2026/09/california-expands-privacy-protections-by-strengthening-deletion-rights/).

En GA4, Meta Conversions API y reglas FTC sobre publicidad/testimonios no se identificó un cambio material **nuevo y verificable** respecto al contenido de este módulo durante esta revisión; esto no equivale a una certificación exhaustiva de que no exista ningún cambio.

## Etiquetas para notas futuras
`official_verified` / `internal_measured` / `external_study` / `hypothesis` / `outdated` / `unverified`.
Para cada nota: `claim | fuente URL | fecha de evidencia | fecha de consulta | alcance | limitaciones | acción`.
Nunca reemplazar un dato con un número genérico sin indicar población y fecha.

## Revisión próxima
Primera revisión ordinaria: noviembre 2026. La existencia de esta fecha **no** crea por sí sola ejecución programada, commit ni actualización.
