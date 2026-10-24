# Brain OS — Diseño Gráfico · Director de Arte UI Pro

> Módulo reutilizable de diseño gráfico y dirección de arte inspirado en UI/UX. Versión **1.0.0**, investigación inicial: **2026-10-24**. Idioma operativo: español.

## Objetivo
Diseñar, rediseñar y auditar piezas visuales con **composición editorial, jerarquía tipográfica, retículas, color, criterios UI/UX, accesibilidad y control de calidad**. Aplicable a identidades, anuncios, flyers, contenido social, websites, apps, dashboards, documentos y presentaciones.

## Activación en otro chat
«Activa Project Brain OS desde DigitalAppcorp/project-brain-os y la habilidad Director de Arte UI Pro de la rama skills/diseno-grafico, carpeta knowledge/diseno-grafico. Trabaja como director de arte senior, respetando mi marca y entregando el formato solicitado».

**Importante:** la habilidad se almacena en esta rama de trabajo, no en main; un agente debe consultar la rama expresamente hasta su integración aprobada. Ningún commit modifica main ni un proyecto como PAZO.

## Archivos y orden de lectura
1. [SKILL.md](SKILL.md): contrato de ejecución y las nueve fases de dirección artística.
2. [references/composicion-y-tipografia.md](references/composicion-y-tipografia.md): reglas de jerarquía, retículas, espaciado, tipografía, color y arte.
3. [references/patrones-por-formato.md](references/patrones-por-formato.md): adaptación a distintos soportes y herramientas.
4. [references/rubrica-y-qa.md](references/rubrica-y-qa.md): puntuación interna y bloqueos de calidad.
5. [references/fuentes-y-referencias.md](references/fuentes-y-referencias.md): fuentes primarias, bibliografía y protocolo de actualización.
6. [assets/brief-template.md](assets/brief-template.md): brief mínimo reutilizable.
7. [assets/design-spec-example.json](assets/design-spec-example.json): datos ficticios de ejemplo.
8. [scripts/audit_design_spec.py](scripts/audit_design_spec.py): comprobación parcial de contraste y objetivos.

## Ejecución de auditoría
Con Python 3 disponible, desde esta carpeta:
```bash
python scripts/audit_design_spec.py assets/design-spec-example.json
```
El resultado no certifica cumplimiento WCAG, ni reemplaza revisión visual o pruebas con usuarios.

## Separación entre proyectos y conocimiento
- **Aquí:** métodos transferibles, estándares, checklists, fuentes e instrumentos.
- **Repositorios de producto:** diseños concretos, decisiones aprobadas, marca, assets, presupuestos, datos de clientes y resultados.
- No introducir secretos ni información personal en este repositorio público.
- El SKILL raíz de Brain OS conserva su autoridad para autorizaciones, Git, continuidad y control de producción. Este módulo **complementa**, no sustituye, esas reglas.
- No reutilizar automáticamente decisiones visuales de PAZO en otras marcas.

## Mantenimiento
Los estándares y referencias pueden cambiar. Revalidar fuentes relevantes por encargo y registrar mejoras en esta rama antes de proponer cambios a main. La documentación no se actualiza sola.
