# Verificación v0.6.0 — 26 de octubre de 2026

## Alcance entregado

Continuación aislada de PR8 HEAD `e967d076bdd96a74e12e62ffd400eb95a8ab3b7d`, rama `feat/design-learning-v06-20261026`. PR8, PR7 (`5f1cf4bf`) y PR3 (`0ebfe4b2`) comprobados abiertos/draft al inicio; PR3 ya enruta sin duplicar criterios. Ningún merge. Brain OS core sigue1.4.1; módulo propuesto0.6.0.

Motor [learning.py](scripts/learning.py), especificación [ADAPTIVE_LEARNING.md](ADAPTIVE_LEARNING.md), [tests locales](scripts/test_learning.py) e integración en recuperación, exploración, memoria, integridad, gates y aprobación visual. No usa red, modelos, dependencias nuevas, servicios comerciales ni MCP nuevo. Conserva el flujo de previews de v0.5.

El conocimiento particular está en la [rama documental de PAZO](https://github.com/DigitalAppcorp/pazo-app/tree/docs/f13-design-learning-20261026/docs/design-learning): ledger JSONL, índice legible y manifiesto de fuentes. No se copia su estética al OS. PAZO base `5036f6d7024ace157c7dad96afc270ba4728d327`; todos sus cambios de esta tarea quedan bajo `docs/design-learning/`.

## Comprobaciones realmente ejecutadas

```text
python -X utf8 -B knowledge/ui-ux-frontend/scripts/test_learning.py
Ran 13 tests
OK
```

| Comprobación local | Resultado |
| --- | --- |
| Aprobación del patrón correcto | Prioridad vacía → +2 para ese patrón |
| Rechazo contextual | −2 en el ámbito afectado |
| Feedback mixto | Acierto+2, aspecto rechazado−2, sin castigo global |
| Corrección solicitada | −1 al patrón señalado; reemplazo no aprobado no recibe premio |
| Separación Feed/Perfil, componente y proyecto | Ninguna coincidencia fuera del ámbito |
| Sustitución posterior explícita | Solo nueva dirección activa; aspectos no sustituidos se conservan |
| Retractación de atribución errónea | Retira el reemplazo y recupera antecedente aplicable |
| Proceso nuevo | Lee el mismo archivo sin depender del proceso anterior |
| Evidencia técnica y no verificada | No puede conferir aprobación; no verificado0 |
| Idempotencia y replay | Mismo evento no duplica, otra ID no multiplica la misma evidencia |
| Lote inválido | No deja escrituras parciales |
| Contexto, caducidad y fecha futura | Excluye condiciones no coincidentes, expiradas o posteriores |
| Error de proceso recurrente | Cuenta revisiones independientes; no suma aspectos duplicados del mismo evento |

Además se cargó el **registro histórico real preparado**, mediante la utilidad, y se repitió una consulta en un proceso independiente:

| Consulta del ledger PAZO | Resultado observado |
| --- | --- |
| feed / follow-button | transparent-follow +2, sin solid-follow |
| profile / follow-button | solid-follow +2, sin transparent-follow |
| feed / post-header | menú de tres puntos+2, Seguir sólido−2 |
| places / layout | Opción3+2, congelación sustituida ausente |
| another-project / feed / follow-button | Ningún patrón PAZO |
| Auditoría pazo | Tres rechazos en revisiones de Perfil1/Perfil2/Admin1: falta de comparación fiel |

Las consultas de PAZO también recuperan su identidad general explícita con especificidad reducida; nunca aparece para otro producto. Los números son deltas heurísticos, no probabilidades ni métricas de calidad UX.

El registro contiene **28 eventos /37 aspectos**: decisiones globales del evento14 APPROVED,5 UNVERIFIED,1 CORRECTED,3 PARTIAL,5 REJECTED. Los aspectos mixtos se puntúan individualmente. Las aprobaciones de referencia no se convierten en aceptación de implementación.

## Integridad y procedencia

- Fuentes históricas selectivas: changeset F13 y gate visual administrativo por SHA `716ebcc081a1d54ecc4579860bee6f4ced3e47ed`; seis comentarios de PR44, cinco de bots y uno humano relevante. Metadatos de commits41b1fe61,ef90d7f5,1934a5d4 contrastados; no se leyó todo el código ni se reconstruyó toda la historia financiera.
- Capturas originales del PO/Library no accesibles por herramientas conectadas. Ledger conserva `DOCUMENTED_PO` y `UNAVAILABLE`; las decisiones se apoyan en documentos verificables, sin afirmar revisión visual propia ni pedir reelegir diseños históricos.
- Arquitectura, helper estático, demo y capturas de v0.5 comparados por **blob Git idéntico** a PR8; diferencia local CRLF normalizada antes de comparar. No hizo falta repetir navegador ni abrir producto.
- Token Savior consultado realmente con `project` absoluto de este checkout; localizó `record` y `query` en el archivo correcto. WORKSPACE_ROOTS global permanece en el checkout previo; no se consultó ese índice para esta rama. Cache de navegación excluida solo en metadatos Git locales, sin hooks ni memoria MCP.
- Referencias relativas del módulo y README, YAML según convención Brain OS y `git diff --check` comprobados. `quick_validate.py` genérico conserva la incompatibilidad histórica con `version/reviewed_at/status`, igual en v0.5; no se declara PASS de ese validador ni se cambia su convención para ocultarlo.
- Sin instalación de paquetes, benchmarks, simulaciones masivas ni runtime de PAZO. Sin cambios de pantallas, funciones, estilos, Supabase, PayPal, Vercel o producción. No se modificaron workflows para este trabajo.

## Qué significa aprender automáticamente

Cuando el agente carga esta versión, consulta el ledger antes de diseñar y registra aspectos del feedback normal después de cada revisión autorizada. No exige formularios nuevos al PO. El ledger versionado sobrevive a cambios de proceso/chat y sus prioridades se recalculan en cada lectura.

La captura depende de que el agente tenga acceso a la revisión y ejecute ese flujo; no existe escucha de chats, cron ni monitor. Registrar feedback no autoriza commit/push/implementación/publicación fuera del alcance. READ_ONLY_AUDIT conserva cero escrituras.

## Limitaciones y siguiente uso

Formato y coherencia se verifican localmente; el motor no autentica al PO ni contrasta enlaces por red. La atribución histórica es revisable y reversible. El seed es selectivo; ausencia de evidencia no es rechazo ni aprobación. No hay evaluación conductual de agentes, calibración científica o mejora visual cuantificada. Apps complejas y comparación de una pantalla implementada con una preview nueva siguen fuera de este encargo.

Los PR siguen en borrador: para usar la capacidad antes de integrar, cargar esta referencia de Brain OS y el registro documental de PAZO. La próxima revisión normal puede aportar un evento nuevo; no queda pendiente ninguna reaprobación obligatoria del historial. Cambiar la política general o incorporar lecciones a otros productos requiere revisión explícita, no propagación automática.
