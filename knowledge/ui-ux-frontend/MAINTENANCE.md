# Mantenimiento y control de cambios

## Versión
**0.2.0 — 2026-10-25**. Ampliación operativa con evaluación adversarial, casos de prueba, protocolos de calidad, WCAG-EM 2.0, métricas con denominadores, biblioteca contextual y criterios de fidelidad visual. Sigue en PR draft y **no implica ejecución real de tests, auditoría de un producto ni instalación automática en agentes externos**.

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
- **2026-10-25 v0.2.0**: corrección S0 ≠ no reproducido; separación severidad/estado/confianza/prueba; incorporación de WCAG-EM 2.0; seis nuevos módulos para calidad visual, gates, métricas, patrones, recetas y evaluación de habilidad. Pendiente de ejecución independiente de la batería E01–E08.
- **2026-10-25 v0.1.0**: creación de habilidad UI/UX Frontend Engineering; referencias a fuentes verificadas, protocolo de criterio independiente, definición de tests y templates.

## Próxima revisión sugerida
**2027-01-25**, o antes si cambia un criterio normativo, una API utilizada, un fallo crítico o una exigencia legal. Esta fecha no configura un recordatorio automático.