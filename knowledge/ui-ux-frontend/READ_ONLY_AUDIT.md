# READ_ONLY_AUDIT — contrato estricto de auditoría sin cambios

## Activación y precedencia
Activar este modo cuando el Product Owner pida **analizar, inspeccionar, evaluar, comparar o auditar** una interfaz **sin modificarla**, aunque el agente disponga de permisos de escritura. También se aplica si el usuario pide «solo lectura» o «no cambies nada».
La intención **más restrictiva** prevalece: una recomendación, un GO previo para desarrollo o la capacidad técnica de editar **no autorizan** mutaciones durante esta auditoría. Sólo una instrucción posterior, explícita y separada del Product Owner puede abrir un trabajo de implementación. Al cambiar de modo, declarar el nuevo alcance y volver a comprobar permisos/gates del proyecto.

## Invariante: cero mutaciones en el objetivo auditado
**PERMITIDO**, según acceso y legalidad:
- Leer repositorio, PR, commits, documentación, código, pruebas ya ejecutadas, logs disponibles, configuraciones no secretas y resultados de herramientas de consulta.
- Inspeccionar visualmente capturas y páginas de forma pasiva; abrir vistas públicas o estado reproducible ya autorizado sin iniciar operaciones de negocio.
- Leer evidencias de entornos QA existentes sin provocar nuevas transacciones, cuentas ni cambios duraderos.
- Calcular contraste, comparar tokens y analizar código en memoria; contrastar con las normas vigentes.

**PROHIBIDO** incluso cuando las herramientas lo permitan:
- Crear, editar, borrar, mover, comentar, aprobar, hacer commit/push, merge, cherry-pick, modificar ramas, PRs, issues, configuraciones, archivos o registros del **producto auditado**.
- Mutar Supabase, Vercel, GitHub, Storage, pagos, autenticación, permisos, datos de usuario, banderas de funciones, despliegues o secretos.
- Simular pruebas E2E sobre producción que envíen formularios, creen contenido, alteren datos, disparen eventos financieros, generen cuentas o modifiquen estado remoto.
- Instalar dependencias, ejecutar migraciones, cambiar configuración local o iniciar comandos potencialmente mutantes sobre la copia del producto.
- Usar un navegador para hacer clic en acciones cuya mutación no se haya descartado. Un GET no garantiza ausencia de efectos secundarios; si la navegación podría alterar estado, detenerse y señalar límite.

**Evidencia fuera del producto:** elaborar el informe en la respuesta sin crear archivos. Guardar capturas, resultados o informes en una ubicación distinta del proyecto **únicamente si el PO lo autorizó de forma explícita** y respetando sensibilidad/privacidad. Una auditoría solicitada «sin cambios» no da permiso implícito para escribir en otro repositorio.

## Secuencia ejecutable
1. Identificar objetivo, rama y SHA del código, versión desplegada, entorno, fecha y roles; distinguirlos entre sí. No inferir que `main` = producción.
2. Registrar solo las superficies y recorridos accesibles con consultas pasivas. No exigir credenciales, cuentas ni pruebas activas que muten el sistema.
3. Revisar intención aprobada y contratos de experiencia; aplicar [DESIGN_MEMORY.md](DESIGN_MEMORY.md), [AUDIENCE_BOUNDARY.md](AUDIENCE_BOUNDARY.md), [UX_CONTENT.md](UX_CONTENT.md), [REFERENCE_ANALYSIS.md](REFERENCE_ANALYSIS.md) según alcance.
4. Separar **evidencia observada** de **código inspeccionado**, **reporte de terceros**, **inferencia** y **prueba no ejecutada**. No afirmar una experiencia accesible, no accesible o «conforme» global sin la cobertura necesaria.
5. Para mediciones aplicar [MEASUREMENT_PROTOCOL.md](MEASUREMENT_PROTOCOL.md). Para defectos clasificar independientemente severidad, estado del incidente, confianza y estado de prueba en [AUDIT_QA.md](AUDIT_QA.md).
6. Exponer el menor conjunto de problemas accionables, riesgos, alternativas y criterios de aceptación; no ejecutar las soluciones.
7. Cerrar con declaración de integridad: fuentes consultadas, pruebas y partes no observadas, mutaciones: **ninguna**, y siguiente gate que **requiere nuevo GO**.

## Si no se puede comprobar algo
- Sin navegador/dispositivo: `NOT_TESTED`, diagnóstico de código o screenshot, sin adjudicar PASS de interacción.
- Captura sola: permite detectar señales visuales, no prueba Tab/foco, persistencia, red, API ni respuestas del lector.
- Sin token o sesión de QA autorizada: no intentar desbloquear ni crear usuarios de prueba.
- Una persona informa «2,2:1»: clasificar **REPORTED**, no copiarlo como **MEASURED**, hasta repetir método/superficie.
- Lectura insuficiente o repositorio no disponible: entregar hallazgos limitados; no concluir que no hay problemas.
- Si se descubre un riesgo S3/S4: reportarlo con urgencia y evidencia disponible, **pero no cambiar código**. Si corregir es imprescindible, solicitar o esperar nueva autorización de implementación.

## Estado final obligatorio
`MODO: READ_ONLY_AUDIT | Repositorio/URL | Rama+SHA | Entorno observado | Evidencia | Límites | Hallazgos e incertidumbre | Mutaciones: 0 | Implementación: NO AUTORIZADA EN ESTE MODO`.

Esta es una política operativa del agente; por sí sola no convierte un token de escritura en credencial técnicamente restringida. Cuando haya herramientas o credenciales **realmente de solo lectura**, preferirlas. No anunciar una garantía técnica de permisos que no exista.
