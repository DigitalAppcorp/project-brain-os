#requires -Version 5.1
<#
.SYNOPSIS
  Instala adaptadores globales para Codex y Claude Code usando el checkout canonico.
.DESCRIPTION
  No modifica PAZO ni hace git pull/clone. Ejecutar desde el checkout
  de project-brain-os. No sobrescribe habilidades ajenas o editadas manualmente.
.EXAMPLE
  powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install-user-skills.ps1
#>
[CmdletBinding()]
param(
  [ValidateSet('Both','Codex','Claude')][string]$Agent = 'Both',
  [string]$HomePath = $HOME
)
$ErrorActionPreference = 'Stop'
$repoRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
if (-not (Test-Path -LiteralPath (Join-Path $repoRoot 'SKILL.md') -PathType Leaf)) {
  throw 'No se encuentra SKILL.md de project-brain-os; usa el checkout completo.'
}
if ([string]::IsNullOrWhiteSpace($HomePath)) { throw 'HomePath no valido.' }
$specs = @(
  @{ Name='project-brain-os'; Target='SKILL.md'; Description='Operating system for software product planning, architecture, QA and evidence-based delivery.' },
  @{ Name='marketing-brain'; Target='knowledge/marketing/SKILL.md'; Description='Marketing Brain for campaigns, conversion measurement, paid media, growth and business outcomes.' },
  @{ Name='design-intelligence'; Target='knowledge/ui-ux-frontend/SKILL.md'; Description='UI UX Design OS for real web PWA design, accessibility, frontend and verified visual QA.' },
  @{ Name='video-production'; Target='knowledge/video-production/SKILL.md'; Description='Video Production OS for screenwriting, directing, editing, animation and audiovisual QA.' },
  @{ Name='graphic-art-direction'; Target='knowledge/graphic-design/SKILL.md'; Description='Art direction for advertising images, branding and graphic design; independent from UI UX.' },
  @{ Name='expert-evidence-review'; Target='patterns/EXPERT_EVIDENCE_PROTOCOL.md'; Description='Expert evidence protocol for primary sources, falsifiable tests and independent review.' },
  @{ Name='token-efficiency'; Target='patterns/LOCAL_FIRST_EFFICIENCY.md'; Description='Token saving, local-first workflow, batched tests, less rework and fewer needless remote calls.' },
  @{ Name='verifiable-handoff'; Target='patterns/VERIFIABLE_HANDOFF.md'; Description='Concise verifiable context transfer between chats and agents, with branches, CI and safety gates.' },
  @{ Name='find-skills'; Target='.agents/skills/find-skills/SKILL.md'; Description='Find, compare and verify existing agent skills; do not install external skills without approval.' }
)
$marker = '<!-- managed-by: project-brain-os-install-user-skills -->'
$utf8 = New-Object System.Text.UTF8Encoding($false)
$targetRoots = @()
if ($Agent -ne 'Claude') { $targetRoots += (Join-Path (Join-Path $HomePath '.agents') 'skills') }
if ($Agent -ne 'Codex') { $targetRoots += (Join-Path (Join-Path $HomePath '.claude') 'skills') }
$added = 0
$skipped = 0
foreach ($targetRoot in $targetRoots) {
  foreach ($spec in $specs) {
    $canonical = Join-Path $repoRoot ($spec.Target.Replace('/', [System.IO.Path]::DirectorySeparatorChar))
    if (-not (Test-Path -LiteralPath $canonical -PathType Leaf)) {
      throw "Falta el archivo canonico: $canonical"
    }
    $folder = Join-Path $targetRoot $spec.Name
    $destination = Join-Path $folder 'SKILL.md'
    if (Test-Path -LiteralPath $destination) {
      $existing = [System.IO.File]::ReadAllText($destination)
      if (-not $existing.Contains($marker)) {
        Write-Warning "Conservada habilidad existente no gestionada: $destination"
        $skipped++
        continue
      }
    }
    $body = @'
---
name: __NAME__
description: __DESCRIPTION__
---

# __NAME__ — Project Brain OS
<!-- managed-by: project-brain-os-install-user-skills -->

This user-level skill is a lightweight pointer to the canonical checkout,
not a fork. Read the full Brain OS rules at:
__ROOT_SKILL__

Then read the domain source of truth at:
__SOURCE_SKILL__

Read any linked references or scripts from the same checkout. Respect the
product repository's AGENTS.md, current CI, privacy gates and approvals.
Never treat a draft PR, a CI pass or a written plan as a production release.
If these files are unavailable, ask to update the local Brain OS checkout
rather than inventing missing instructions.
'@
    $body = $body.Replace('__NAME__', $spec.Name)
    $body = $body.Replace('__DESCRIPTION__', $spec.Description)
    $body = $body.Replace('__ROOT_SKILL__', (Join-Path $repoRoot 'SKILL.md'))
    $body = $body.Replace('__SOURCE_SKILL__', $canonical)
    if (-not (Test-Path -LiteralPath $folder)) {
      [void](New-Item -ItemType Directory -Path $folder -Force)
    }
    [System.IO.File]::WriteAllText($destination, $body, $utf8)
    Write-Output "INSTALLED $destination"
    $added++
  }
}
Write-Output "BRAIN_SKILLS_INSTALLED=$added SKIPPED_UNMANAGED=$skipped"
