# Mantenimiento y control de cambios

## Versión
**0.7.0 propuesta — 2026-10-26**. Extensión optativa de UX motivacional veraz y CSS accesible ([MOTIVATIONAL_UX.md](MOTIVATIONAL_UX.md)). La base v0.6.0 continúa integrada en `main`; esta actualización permanece sin merge. No se declara efecto medido en motivación, retención o conversión.

**0.6.0 — 2026-10-26**. Ampliación operativa con evaluación adversarial, casos de prueba, protocolos de calidad, WCAG-EM 2.0, métricas con denominadores, biblioteca contextual y criterios de fidelidad visual. Está integrada en `main` y **no implica evaluación comparativa del agente, auditoría de un producto ni instalación automática en agentes externos**; existen verificaciones acotadas de motor y preview documentadas.

## Actualización periódica
Revisar la documentación en cada modificación sustantiva y, como práctica interna, cada **90 días**:
- W3C: versiones y errata de WCAG, WAI APG y técnicas accesibles.
- React, navegadores, API PWA y herramientas de prueba según framework real.
- Google web.dev: métricas Core Web Vitals y umbrales.
- Sistemas de diseño y UX research cuando aparezcan nuevos hallazgos relevantes.
- Seguridad y privacidad cuando cambie el contexto legal/productivo.

Una revisión no ocurre automáticamente. Para actualizar: consultar fuente y fecha, explicar cambio, crear rama y PR, actualizar SOURCES.md, versión y changelog; no afirmar que «ya se actualizó» sin commit comprobado.

## Cambios y semver
- **PATCH**: claridad, enlaces, erratas, ejemplos sin cambiar criterios.
- **MINOR**: nuevas listas, técnicas o criterios compatibles.
- **MAJOR**: nueva precedencia o contrato que altere decisiones de producto.

## Prueba de regresión documental
Antes de merge:
1. Validar frontmatter de SKILL.md, enlaces relativos y rutas.
2. Revisar que normas, recomendaciones, hipótesis y preferencias estén etiquetadas.
3. Confirmar que no existan reglas estéticas universalizadas a partir de un producto.
4. Verificar que no contenga secretos, datos personales ni credenciales.
5. Verificar que no autorice producción, merge o gasto sin gates Brain OS.
6. Simular auditoría de una pantalla, un error asíncrono y un desacuerdo estético.
7. Abrir PR y revisión del Product Owner; no alterar el core de Brain OS si solo se actualiza este módulo.

## Política de evaluación del propio módulo
Cada versión nueva debe documentar: batería de escenarios con entrada y respuesta esperada, rúbrica, baseline anterior, observaciones, regresiones y decisión. Revisar [EVALUATIONS.md](EVALUATIONS.md). Si solo se redactó la batería, registrar estado **NOT_EVALUATED**; no declarar mejoría cuantificada. Los ejemplos de código son plantillas y no pruebas ejecutadas.

## Historial
- **2026-10-26 v0.7.0 (propuesta):** filtro contextual de apoyo motivacional, separación de estado real/mensaje/animación CSS, salvaguardas antimanipulación, reduced motion y casos de evaluación E21–E23 (solo especificados).
- **2026-10-25 v0.4.0**: modo READ_ONLY_AUDIT sin mutaciones, protocolo de medición verificable, plantilla corregida, router PR #3 → especialista PR #7 y nuevos fixtures E17–E20. Pruebas documentales verificables; evaluaciones del modelo siguen pendientes.
- **2026-10-25 v0.3.0**: introduce la capa de razonamiento, fronteras de audiencia, memoria de diseño, creatividad contextual, referencias, control de cambios y UX content. Evaluación E01–E16 pendiente.
- **2026-10-25 v0.2.0**: corrección S0 ≠ no reproducido; separación severidad/estado/confianza/prueba; incorporación de WCAG-EM 2.0; seis nuevos módulos para calidad visual, gates, métricas, patrones, recetas y evaluación de habilidad. Pendiente de ejecución independiente de la batería E01–E08.
- **2026-10-25 v0.1.0**: creación de habilidad UI/UX Frontend Engineering; referencias a fuentes verificadas, protocolo de criterio independiente, definición de tests y templates.

## Próxima revisión sugerida
**2027-01-25**, o antes si cambia un criterio normativo, una API utilizada, un fallo crítico o una exigencia legal. Esta fecha no configura un recordatorio automático.

## Versión 0.3.0 — 2026-10-25
- Arquitectura basada en decisiones, no en un estilo visual prefijado.
- Siete módulos nuevos: `DESIGN_REASONING`, `AUDIENCE_BOUNDARY`, `DESIGN_MEMORY`, `CREATIVE_EXPLORATION`, `REFERENCE_ANALYSIS`, `CHANGE_INTEGRITY`, `UX_CONTENT`.
- Ruteo por tarea: proyecto nuevo, ajuste, rediseño, auditoría, referencias, implementación y optimización.
- Control de filtración de instrucciones técnicas a texto público, además de separación de negocio, UX, legal e implementación.
- Contratos de intención de diseño en repositorio de producto y doble prueba de delta + invariantes.
- Evaluaciones E09–E16 y criterios para detectar homogeneización y regresiones.
- **Estado:** documentación lista en rama, sin haber demostrado experimentalmente mejora vs v0.2.0; no instalar globalmente ni declarar pruebas ejecutadas por redactar fixtures.

## Revisión de independencia
La habilidad puede citar referentes de diseño, pero no debe copiar literalmente sus guías como si fueran reglas propias ni crear un estilo forzoso para todos los productos. Comprobar que cada decisión se fundamenta en el encargo y que el PO conserva autoridad estética dentro de accesibilidad/integridad. Las lecciones de productos concretos viven en sus repositorios, no en Project Brain OS.


## Dependencias integradas y autoridad
- [PR #7](https://github.com/DigitalAppcorp/project-brain-os/pull/7) aportó la especialidad; [PR #8](https://github.com/DigitalAppcorp/project-brain-os/pull/8) añadió previews y gates visuales; [PR #9](https://github.com/DigitalAppcorp/project-brain-os/pull/9) añadió aprendizaje contextual; [PR #3](https://github.com/DigitalAppcorp/project-brain-os/pull/3) integró el router. Todos están fusionados en `main`.
- La autoridad normativa especializada permanece en `knowledge/ui-ux-frontend/SKILL.md`; `patterns/INTERFACE_QUALITY_GATE.md` solo enruta.
- El motor y las herramientas no se instalan automáticamente en otros agentes. Las autorizaciones para modificar productos, fusionar o desplegar siguen independientes conforme a Brain OS raíz.

- **2026-10-26 v0.5.0**: protocolo de aprobación visual, previews externas al producto, utilidad estática sin dependencias y guía de Playwright CLI. Ver [PREVIEW_VERIFICATION.md](PREVIEW_VERIFICATION.md) para pruebas realmente ejecutadas. Batería comparativa de agentes no ejecutada; no cambia Brain OS core ni integra PR #3/#7 automáticamente.

- **2026-10-26 v0.6.0**: motor local de feedback contextual (JSONL/Python stdlib), sustitución granular, reversión, recuperación y errores recurrentes; integrado al protocolo de previews v0.5 sin alterar permisos. Registro histórico PAZO permanece en rama documental de ese producto. Ver [LEARNING_VERIFICATION.md](LEARNING_VERIFICATION.md): tests del motor no equivalen a evaluación del agente ni a mejora cuantificada de UX. Feedback no modifica automáticamente la política general.
