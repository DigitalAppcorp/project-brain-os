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

## Cambios que disparan revisión urgente
- políticas de anuncios/discriminación/consentimiento o nueva obligación legal;
- deprecación API, definición de evento, pérdida de tracking o cumplimiento de datos;
- alteración de campañas automáticas que afecte costes o acceso;
- nuevos hallazgos de retención o de incremento comercial verificables.

## Estándar de calidad del update
Toda actualización debe indicar: fuente primaria; fecha; lo anterior vs lo nuevo; impacto; decisión recomendada; qué NO se verificó; riesgos; ruta Git/PR; si requiere revisión del Product Owner.
