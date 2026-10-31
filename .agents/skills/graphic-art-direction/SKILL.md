---
name: graphic-art-direction
description: Graphic Design & Art Direction OS para publicidad estática, identidad, posters, campañas y diseño editorial; activar al crear o auditar piezas gráficas. No sustituye UI/UX en pantallas funcionales.
---

# Adaptador de descubrimiento — Graphic Design & Art Direction OS

Antes de diseñar anuncios o piezas gráficas, lee [módulo canónico](../../../knowledge/graphic-design/SKILL.md), [flujo](../../../knowledge/graphic-design/ART_DIRECTION_WORKFLOW.md), [copy+arte](../../../knowledge/graphic-design/COPY_ART_INTEGRATION.md), [quality gate](../../../knowledge/graphic-design/QUALITY_GATE.md) y [casos de regresión](../../../knowledge/graphic-design/REGRESSION_CASES.md). Activa también `expert-evidence-review` y Marketing Brain según el encargo.

**Autoridad primaria:** dirección de arte para piezas gráficas. UI/UX solo asesora legibilidad y fidelidad de producto cuando corresponde. No convertir ads en dashboards. Un documento aprobado no equivale a pieza visual aprobada ni a rendimiento medido. No gastar presupuesto, publicar ni prometer resultados sin autorización/evidencia.

## Gate no eludible para entregas
**Obligatorio** abrir [EXECUTION_PROTOCOL](../../../knowledge/graphic-design/EXECUTION_PROTOCOL.md), inspeccionar las imágenes finales individualmente y ejecutar [evidence gate](../../../knowledge/graphic-design/scripts/validate_creatives.py) antes de declarar READY_FOR_PO_REVIEW. Un creative FAIL bloquea la entrega como material listo. Un script PASS no valida la calidad estética.


## Identidad verificada y aprendizaje v0.4
Leer [BRAND_ASSET_AUTHORITY](../../../knowledge/graphic-design/BRAND_ASSET_AUTHORITY.md) antes del render final. No usar logos auténticos históricos como vigentes sin prueba; bloquea ante conflicto entre versiones aprobadas. Preservar composición visual aprobada cuando solo hay que corregir identidad. Manifest schema_version=2.
