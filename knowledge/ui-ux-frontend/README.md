# Brain OS — UI/UX Frontend Engineering

> **v0.6.0 · 2026-10-26 · documentación implementada en rama de revisión · batería comparativa pendiente de ejecución.**

## Propósito
Sistema de decisiones reutilizable para diseñar, construir, criticar y mantener productos digitales **desde cero o existentes**: apps, webs, PWAs, dashboards, componentes, modales, rediseños, UX writing, análisis de referentes y auditorías. No define una apariencia estándar ni se limita a React; selecciona proceso proporcional al contexto.

### Activación
> Activa Project Brain OS y el módulo `knowledge/ui-ux-frontend/SKILL.md`. Selecciona modo según el trabajo, diferencia la audiencia del Product Owner de los usuarios finales, preserva decisiones aprobadas y audita tus propias propuestas con evidencia.

## Orden de lectura (carga progresiva)
**Siempre**
1. [SKILL.md](SKILL.md) — núcleo, autoridad, límites y selección de modo.
2. [DESIGN_REASONING.md](DESIGN_REASONING.md) — razonamiento y entrega proporcionados.

**Preview y decisiones visuales (al diseñar o implementar UI)**
- [VISUAL_APPROVAL_PROTOCOL.md](VISUAL_APPROVAL_PROTOCOL.md) — única política de alternativas, preview final y autorizaciones.
- [PREVIEW_ARCHITECTURE.md](PREVIEW_ARCHITECTURE.md) — aislamiento, servidor sin dependencias, Playwright CLI y comparación.
- [PREVIEW_VERIFICATION.md](PREVIEW_VERIFICATION.md) — evidencia de instalación y smoke local, con límites.

**Aprendizaje contextual (antes de diseñar y después del feedback PO)**
- [ADAPTIVE_LEARNING.md](ADAPTIVE_LEARNING.md) — persistencia, esquema, prioridades auditables, captura y recuperación.
- [LEARNING_VERIFICATION.md](LEARNING_VERIFICATION.md) — pruebas pequeñas realmente ejecutadas, historial F13 y límites.

**Diseño y contenido**
3. [AUDIENCE_BOUNDARY.md](AUDIENCE_BOUNDARY.md) — clasificación de instrucciones vs UI pública.
4. [UX_CONTENT.md](UX_CONTENT.md) — jerarquía de títulos, copy, estados y tono.
5. [CREATIVE_EXPLORATION.md](CREATIVE_EXPLORATION.md) — alternativas pertinentes y anti-fijación.
6. [REFERENCE_ANALYSIS.md](REFERENCE_ANALYSIS.md) — análisis de otros productos sin copia.
7. [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md) + [VISUAL_QUALITY.md](VISUAL_QUALITY.md) — sistemas, composición y fidelidad.
8. [UX_RESEARCH.md](UX_RESEARCH.md) + [UX_METRICS.md](UX_METRICS.md) — investigación y medidas.

**Auditoría especializada**
9. [READ_ONLY_AUDIT.md](READ_ONLY_AUDIT.md) — modo de auditoría estrictamente sin mutaciones, alcance y límites.
10. [MEASUREMENT_PROTOCOL.md](MEASUREMENT_PROTOCOL.md) — registro reproducible de contraste, objetivos, estados y rendimiento.

**Mantenimiento, ingeniería y auditoría**
11. [DESIGN_MEMORY.md](DESIGN_MEMORY.md) + [CHANGE_INTEGRITY.md](CHANGE_INTEGRITY.md) — contratos de experiencia y no-regresión.
12. [FRONTEND_ENGINEERING.md](FRONTEND_ENGINEERING.md) + [PATTERN_LIBRARY.md](PATTERN_LIBRARY.md) — implementación y escenarios de producto.
13. [ACCESSIBILITY.md](ACCESSIBILITY.md) + [AUDIT_QA.md](AUDIT_QA.md) + [QUALITY_GATES.md](QUALITY_GATES.md) + [TEST_RECIPES.md](TEST_RECIPES.md) — pruebas, WCAG y evidencias.
14. [DECISION_PROTOCOL.md](DECISION_PROTOCOL.md) — criterios de desacuerdo y decisiones.
15. [EVALUATIONS.md](EVALUATIONS.md) — batería de evaluación de la habilidad.
16. [SOURCES.md](SOURCES.md) + [MAINTENANCE.md](MAINTENANCE.md) — fuentes y revisión.
17. [templates/](templates/) — fichas de auditoría, contrato y registro de intención.

## Doctrina de diseño (v0.3)
- **No ejecutar el prompt como maqueta del brief:** el usuario final no debe leer explicaciones internas destinadas al creador.
- **No exportar requisitos de seguridad al copy automáticamente:** implementar lógica real, informar consecuencias cuando el usuario realmente las necesite.
- **No crear marcadores decorativos de estructura** (p. ej., «Sección 02») a menos que ayuden a navegar, clasificar o seguir un proceso.
- **No homogeneizar por obedecer otra regla:** un patrón recurrente puede ser el mejor si el contexto lo justifica.
- **No confundir gusto con norma:** separar preferencias legítimas del PO, usabilidad medible y accesibilidad.
- **No perder intención al modificar:** verificar el cambio solicitado y conservar el resto del contrato de experiencia.
- **No prometer resultados no probados:** design spec, código, QA automatizado, prueba manual y producción son estados distintos.
- **AUDIT = solo lectura:** si el encargo es evaluar sin tocar, cero mutaciones del producto. La auditoría no concede permiso para implementar; requiere nuevo GO.
- **Valor medido ≠ reportado:** todo número se acompaña de fuente, método, aplicabilidad y cobertura; no inventar conformidad.
- **Autoridad única:** `patterns/INTERFACE_QUALITY_GATE.md` del PR #3 es el router; este módulo es la única fuente especializada, actualmente en PR #7 hasta integración autorizada.

## Modos sin duplicar habilidades
- **Crear:** comprender negocio/audiencia, definir estructura, explorar opciones cuando convenga, implementar si autorizado.
- **Ajustar:** identificar delta + invariantes, corregir con el cambio mínimo, verificar regresiones.
- **Rediseñar:** auditar sistema existente y desarrollar nueva intención visual con migración segura.
- **Evaluar:** separar observado/hipótesis, severidad/estado del incidente y pruebas.
- **Analizar inspiración:** reconocer decisión, contexto, límites de transferencia y alternativa propia.
- **Implementar:** traducir contratos UX a semántica, estados, rendimiento y evidencia técnica.

El módulo **complementa Project Brain OS raíz**: las autorizaciones, control de producción, Git y Scope Closure Reconciliation siguen vigentes. Aquí solo vive metodología general; decisiones específicas de PAZO u otros productos deben permanecer en sus propios repositorios.

## Estado de calidad
**Documentación publicada en rama de revisión**, sin merge y sin asumir instalación permanente en otros agentes. **Los fixtures de EVALUATIONS.md están especificados pero no equivalen a pruebas ejecutadas**. Comprobar el PR antes de afirmar cobertura o aprobación.