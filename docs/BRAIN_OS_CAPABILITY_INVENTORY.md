# Brain OS — inventario de capacidades reutilizables (31-oct-2026)

Este inventario distingue **contenido guardado en main**, **descubrimiento dentro del checkout** y **instalación local**. No certifica que un agente usó correctamente una habilidad o mejoró resultados/tokens.

| Capacidad | Fuente canónica (main) | Entrada al agente |
| --- | --- | --- |
| Orquestación de producto, arquitectura, seguridad, CI, releases | `SKILL.md`, `patterns/GIT_WORKFLOW.md`, `patterns/BACKEND_SAFETY.md` | `project-brain-os` |
| Ahorro de tokens, local-first, tests agrupados y reducción de retrabajo | `SKILL.md` §16 y `patterns/LOCAL_FIRST_EFFICIENCY.md` | `token-efficiency` |
| Continuidad entre chats, decisiones y agentes | `patterns/VERIFIABLE_HANDOFF.md`, `SKILL.md` §19.9–20 | `verifiable-handoff` |
| Buscar y evaluar skills de terceros antes de proponer su instalación | `.agents/skills/find-skills/SKILL.md` | `find-skills` (requiere autorización para instalar) |
| Qué haría un profesional, fuentes originales, método y prueba externa | `patterns/EXPERT_EVIDENCE_PROTOCOL.md`, `patterns/EXPERT_EVIDENCE_FIXTURES.md` | `expert-evidence-review` |
| Marketing, adquisición, Meta/SEO/CRO, medición y privacidad | `knowledge/marketing/SKILL.md` y referencias | `marketing-brain` |
| UI/UX, Design OS, frontend, accesibilidad y Design QA | `knowledge/ui-ux-frontend/SKILL.md` y referencias | `design-intelligence` |
| UX motivacional y microinteracciones CSS (opcionales) | `knowledge/ui-ux-frontend/MOTIVATIONAL_UX.md` | Submódulo de `design-intelligence` |
| Composición/alineación contextual de cajas de texto | `knowledge/ui-ux-frontend/VISUAL_QUALITY.md`, `TEST_RECIPES.md` | Submódulo de `design-intelligence` |
| Diseño gráfico, arte, branding, publicidad estática | `knowledge/graphic-design/SKILL.md` y scripts | `graphic-art-direction` |
| Guion, dirección, animación, edición y video | `knowledge/video-production/SKILL.md` y scripts | `video-production` |
| Investigación, validación, prototipos, cierres de alcance | `SKILL.md`, `patterns/` y `templates/` | Submódulos de `project-brain-os` |

## Matices obligatorios
- Los 9 puntos de entrada aparecen en `.agents/skills/` y `.claude/skills/` del repositorio canónico. En `pazo-app` u otros proyectos, **instalar punteros de usuario** usando `scripts/install-user-skills.ps1` desde el checkout local actualizado. Un merge Git no instala nada en una PC ajena.
- Se recuperó selectivamente la guía `MOTIVATIONAL_UX.md` del PR borrador #11, sin sustituir Design OS v0.7 actual. Se recuperó de manera análoga la guía puntual de eje central de #12. Los PR #11/#12 no se fusionaron; su trabajo restante exige comparación con `main` antes de cerrarlos.
- No toda capacidad necesita una skill distinta: el router Brain OS decide qué módulos cargar según tarea para evitar gastar tokens cargándolo todo.
- Tests de estructura o workflows PASS no demuestran ahorros económicos de tokens, calidad creativa ni mejoras de negocio. Las habilidades son protocolos documentados, no modificación de pesos del modelo.
- Ninguna habilidad publica PAZO, modifica Supabase, instala servicios externos, gasta presupuesto ni cambia campañas sin autorización apropiada.
