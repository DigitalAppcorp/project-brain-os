# Instalar Brain OS en Codex y Claude Code (Windows)

El código **canónico** está en `DigitalAppcorp/project-brain-os` rama `main`. Las habilidades NO se activan por el mero hecho de que exista una carpeta `knowledge/` en GitHub.

## Descubrimiento dentro del repositorio
- Codex lee `.agents/skills/<nombre>/SKILL.md`.
- Claude Code lee `.claude/skills/<nombre>/SKILL.md`.
- Estos adaptadores referencian los módulos canónicos, evitando copiar y mantener dos versiones.
- El instalador registra nueve puntos de entrada: seis habilidades principales, `token-efficiency`, `verifiable-handoff` y `find-skills`. Este último es un módulo opcional de descubrimiento; no instala paquetes externos sin autorización.
- Los patrones siguen siendo canónicos en `patterns/`; los adaptadores nunca duplican su contenido.

## Disponibilidad desde PAZO o cualquier otro proyecto Windows
1. Haz checkout del repositorio canónico en tu PC (**no** uses un snapshot histórico de otra rama):
   ```powershell
   git clone https://github.com/DigitalAppcorp/project-brain-os.git
   cd project-brain-os
   git switch main
   git pull --ff-only
   ```
   Si ya está clonado, **no hagas clone otra vez**; ve a su carpeta y ejecuta `git status` antes de `git pull --ff-only`. No descartes cambios locales.
2. Ejecuta desde la raíz de ese checkout:
   ```powershell
   powershell -NoProfile -File .\scripts\install-user-skills.ps1
   ```
   En PowerShell 7 también: `pwsh -NoProfile -File ./scripts/install-user-skills.ps1`.
3. El script escribe únicamente **adaptadores personales** en `~/.agents/skills` (Codex) y `~/.claude/skills` (Claude Code). No toca `pazo-app`, ni `main`, ni Supabase, ni producción. No requiere copiar todo Brain OS al repositorio de la aplicación.
4. Reinicia sesiones de Codex/Claude Code y prueba desde el directorio de `pazo-app`: pide listar `project-brain-os`, `marketing-brain`, `design-intelligence`, `video-production`, `graphic-art-direction`, `expert-evidence-review`, `token-efficiency`, `verifiable-handoff` y `find-skills`. En Codex usa `/skills`; en Claude Code comprueba las habilidades de proyecto/usuario y llama `/project-brain-os` si corresponde. **Ver en el selector no garantiza uso**: solicita al agente que abra el archivo canónico y cite su versión.

## Sin sobrescrituras ni dependencia de una sesión
- Si existe una habilidad del usuario no gestionada por este instalador con el mismo nombre, no se sobrescribe. Revisar el aviso de salida.
- El instalador se puede volver a ejecutar cuando cambian rutas o módulos. Los adaptadores apuntan al checkout actual, por lo que actualizar `main` local con `git pull --ff-only` actualiza sus referencias.
- Si mueves o borras ese checkout, reinstala desde la nueva ubicación; los adaptadores globales apuntarán a la ruta anterior hasta hacerlo.
- El contenido de `knowledge/` es metodología, no credenciales, datos productivos ni garantía de calidad de entregables.
- PR #11 y #12 de Design OS siguen en borrador; **no** tratarlos como habilidad publicada sin evaluación de compatibilidad con la versión vigente.

## Chequeo reproducible
```powershell
python scripts/check_skill-discovery.py
```

Referencias: [Codex skills](https://learn.chatgpt.com/docs/build-skills) y [Claude Code skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

## Inventario de capacidades y borradores

[Inventario de Brain OS](BRAIN_OS_CAPABILITY_INVENTORY.md) muestra módulos, rutas de verdad, estado publicado y borradores. El módulo complementario de UX motivacional fue transferido de manera selectiva desde el PR #11, sin fusionar su antigua versión de Design OS. La guía de alineación textual de #12 también quedó integrada selectivamente; ambos PR históricos continúan en borrador hasta su reconciliación formal.
