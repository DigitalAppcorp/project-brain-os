# Memoria de diseño y continuidad entre sesiones

## Regla central
El sistema visual no es solo colores y componentes. Conservar **intención, razones, contratos de experiencia y decisiones** permite implementar cambios sin degradar lo aprobado. La memoria debe ser verificable, acotada, versionada y específica de cada producto.

## Qué vive dónde
- **Project Brain OS / habilidad**: método general, plantillas y criterios de calidad.
- **Repositorio del producto**: objetivos, perfil de audiencia, voz, decisiones aprobadas, capturas/referencias con permiso, componentes/tokens, restricciones, estados de UI, experimentos y evidencias.
- **Chat**: discusión y contexto temporal, no único origen de verdad.
- **Datos sensibles**: fuentes seguras del proyecto; no guardar secretos/PII en archivos públicos.

## Design Intent Record (DIR)
Crear o actualizar cuando cambia una dirección importante, no por cada padding.

```yaml
decision_id: UI-DIR-001
surface: "ejemplo/membresia"
status: approved | proposed | superseded
audience: "usuarios elegibles"
task: "comprender y decidir si apoyar"
intent: "invitación cálida, libre de presión"
must_show: ["precio", "renovación", "consentimiento"]
must_preserve: ["jerarquía aprobada", "tono", "acción clara"]
not_for_public_ui: ["detalles de idempotencia y webhooks"]
visual_principles: ["claridad", "fluidez", "espacio acorde a tarea"]
references: ["enlace a archivo aprobado + qué se aprende"]
constraints: ["a11y WCAG", "verdad autoritativa de pago"]
evidence: ["captura/revisión/feedback con fecha"]
owner_approval: "quién/cuándo/alcance, si existe"
source_commit: "sha cuando aplique"
```

Este ejemplo es ilustrativo; no inserta decisiones de un proyecto real en la habilidad.

## Flujo de recuperación
1. Antes de diseño/código leer AGENTS, roadmap, contratos de pantalla y decisiones aprobadas en el repositorio del producto.
2. Distinguir la versión **actual en producción** de la pantalla aprobada en propuesta/rama. Una captura de diseño no acredita deployment.
3. Registrar qué se conserva, qué está obsoleto y qué cambia; enlazar evidencia nueva si contradice una decisión.
4. Si no hay contrato formal, recuperar de mensajes/documentos existentes sin inventar aprobación ni formalizar preferencias a ciegas.
5. Tras revisión, guardar únicamente decisiones transferibles al proyecto, no largas transcripciones de chat.

## Conflicto entre memoria y evidencia
- Hechos de runtime/código probado pueden revelar que la memoria está desactualizada: registrar divergencia y corregir el contrato tras revisión, no fingir que diseño y app coinciden.
- Prioridad: seguridad/requisitos vigentes > hechos actuales verificados > aprobación más reciente del producto > borradores anteriores > interpretación del agente.
- Cambios en preferencia no alteran automáticamente accesibilidad, requisitos legales o decisiones de otros productos.

## Anti-deriva
En cada cambio relevante comprobar `invariantes`: tono, arquitectura de información, layout aprobado, funciones, roles, foco, navegación y mensajes contractuales. Señalar explícitamente una modificación no autorizada aunque compile.
Véase [CHANGE_INTEGRITY.md](CHANGE_INTEGRITY.md).

## Handoff entre chats
`producto/ref | rama/HEAD | superficie | tarea | decisiones DIR aplicables | diferencias visibles | cambios realizados | pruebas/estado | pendientes | siguiente acción | prohibiciones/autorizaciones`.
No decir «recordado para siempre» si no existe documentación recuperable.
