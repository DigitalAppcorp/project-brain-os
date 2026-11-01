# Mantenimiento del brazo marketero

Creado: **2026-10-23**. Estado: `v0.1.0 / baseline`. Owner de decisiones: Product Owner; editor responsable: AI Project Brain con herramientas disponibles.

## Cadencia propuesta
- **Mensual:** revisar *si hay cambios materiales* en Google Ads/conversiones, Meta Ads y CAPI, GA4, SEO/AI Search, TikTok Creative, FTC y California CPPA. Si no cambió nada relevante, registrar `NO_MATERIAL_CHANGE`; no editar documentos solo para subir fecha.
- **Por evento:** revisar inmediatamente antes de campaña en vivo, cambio de API/instrumentación, lanzamiento de producto, nueva legislación/política aplicable, anomalía comercial, nueva evidencia experimental o cambio significativo de fuente.
- **Trimestral:** revisar frameworks de contenido, economía unitaria, retención, playbooks y ejemplos para detectar obsolescencia.

## Procedimiento exacto
1. Auditar `main`, PRs y rama activa del repositorio.
2. Abrir fuentes oficiales y comprobar fecha real/versiones; guardar URL y alcance. Comparar recomendaciones con texto actual, no titular.
3. Clasificar `MATERIAL` / `NO_MATERIAL_CHANGE` / `UNVERIFIED`.
4. Si material: redactar **qué cambió, quién se afecta, evidencia, acción, riesgo y fecha**.
5. Trabajar en rama Git de conocimiento con cambio mínimo; tocar solo documentos relevantes, con PR de revisión. No merge automático ni cambiar campañas/producción.
6. Añadir entrada de revisión a este archivo, y al CHANGELOG raíz solo si representa aprendizaje generalizable.
7. La implementación en un negocio requiere inspección de su repo/datos y autorización separada.
8. Evitar duplicar trabajos si hay PR abierto; verificar SHA/estado antes de editar.

## Registro de revisiones
| Fecha | Tipo | Resultado | Fuente/artefacto |
| --- | --- | --- | --- |
| 2026-10-23 | Baseline | Primer módulo transversal; material verificado en fuentes oficiales, ejemplos y checklists, sin campañas ni datos de negocios | `SOURCES.md`, todos los documentos del módulo |
| 2026-11-01 | MATERIAL (revisión oficial) | Google Ads v26.1, Google Search UGC, propuesta AI training 2027, Meta lifecycle/creativos, TikTok Smart+ y creatividades, California SB 923; sin cambios materiales verificables nuevos en GA4/CAPI/FTC | `SOURCES.md`, `PAID_MEDIA.md`, `SEO_ORGANIC.md`, `COMPLIANCE.md`; fuentes detalladas abajo |

## Acta de revisión oficial — 2026-11-01

**Comparación:** `SOURCES.md` y `MAINTENANCE.md` de main, baseline 2026-10-23, más `PAID_MEDIA.md`, `SEO_ORGANIC.md` y `COMPLIANCE.md`. Se inspeccionaron todos los PRs abiertos del repositorio antes de crear esta rama: ninguno trata el módulo de marketing; no se duplicó trabajo. La revisión solo actualiza documentación.

| Evidencia primaria / fecha | Anterior → nuevo | Alcance y decisión recomendada | Riesgo / estado |
| --- | --- | --- | --- |
| [Google Ads API v26.1](https://developers.google.com/google-ads/api/docs/release-notes), 2026-10-28 | Sin control descrito → priorización de redes y límites por canal en presupuestos elegibles | Auditar elegibilidad/configuración en integraciones Google Ads API; no aplicar cambios automáticos | MATERIAL; depende de tipo de campaña/cuenta; sin breaking changes |
| [Google Search Central UGC](https://developers.google.com/search/updates), 2026-10-26 | SEO genérico → guía específica para URLs compartidas, `noindex` y vigilancia antispam | Plataformas con contenido generado por usuarios: revisar intención de indexación y Search Console | MATERIAL; no aplicar bloqueos indiscriminados |
| [Google AI training control](https://developers.google.com/search/blog/2026/10/ai-training-control), 2026-10-30 | Google-Extended sin propuesta compartida → token común propuesto en robots.txt | Documentar decisión editorial; reevaluar en 2027 antes de usar señal nueva | MATERIAL para planificación; **no disponible todavía** |
| [Meta Advertising Week](https://about.fb.com/ltam/news/2026/10/advertising-week-new-york-2026-nuevas-capacidades-de-ia-para-guiar-campanas-y-llegar-a-los-clientes/), 2026-10-06 | Advantage+ genérico → lifecycle acquisition y video desde imagen; funciones IA con estados distintos | Verificar exclusiones, permisos, revisión de creativos y disponibilidad por cuenta | MATERIAL; omisión del baseline, no anuncio posterior al 23/10 |
| [TikTok Smart+](https://ads.tiktok.com/resources/help/article/how-to-create-a-campaign-in-the-upgraded-smart-experience) y [Recommended Creatives](https://ads.tiktok.com/resources/help/article/about-recommended-creatives-in-tiktok-ads-manager), actualizadas octubre 2026 | Guía creativa 2025 → flujo Smart+ unificado y autorización de refresco de anuncios | Verificar cuenta, automatización elegida y consentimiento de cambios antes de publicar | MATERIAL; día exacto y despliegue universal no verificados |
| [CalPrivacy SB 923](https://privacy.ca.gov/2026/09/california-expands-privacy-protections-by-strengthening-deletion-rights/), 2026-09-27, vigencia 2027-01-01 | Checklist CCPA 2026 genérico → supresión ampliada y método online de solicitudes para entidades cubiertas | Revisar aplicabilidad legal y flujos antes de 2027, sin afirmar cobertura de empresas pequeñas | MATERIAL; omisión del baseline, requiere asesoría jurídica si aplica |

**Sin cambio material verificable en esta revisión:** GA4 (eventos/Measurement Protocol), Meta Conversions API (integración/deduplicación) y FTC (publicidad y reseñas). Las fuentes oficiales existentes se mantienen; no se infiere que no existan cambios fuera de lo consultado. Google Ads [migración de conversiones offline a Data Manager API](https://support.google.com/google-ads/answer/14274408) ya figuraba en el baseline y no se vuelve a registrar como novedad.

**Qué NO se verificó:** configuración de cuentas Meta/Google/TikTok, elegibilidad individual de funciones, métricas de campañas, repositorios de negocios, estado de indexación, aplicación jurídica de SB 923 a una empresa concreta, disponibilidad futura del token de IA o auditoría exhaustiva de todos los changelogs. **Acción y límite:** revisión por Product Owner del PR; sin merge, sin modificaciones de campañas, datos personales ni producción.

## Cambios que disparan revisión urgente
- políticas de anuncios/discriminación/consentimiento o nueva obligación legal;
- deprecación API, definición de evento, pérdida de tracking o cumplimiento de datos;
- alteración de campañas automáticas que afecte costes o acceso;
- nuevos hallazgos de retención o de incremento comercial verificables.

## Estándar de calidad del update
Toda actualización debe indicar: fuente primaria; fecha; lo anterior vs lo nuevo; impacto; decisión recomendada; qué NO se verificó; riesgos; ruta Git/PR; si requiere revisión del Product Owner.
