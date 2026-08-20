# One-click install all Apple Design skills to your project (PowerShell)
# Usage: .\scripts\install.ps1 [target_dir]
#
# This copies all skills into <target_dir>\.claude\skills\
# or <target_dir>\.mimocode\skills\ (auto-detected)

param(
    [string]$Target = "."
)

$ErrorActionPreference = "Stop"

$RepoDir = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)

# Detect agent platform
if (Test-Path "$Target\.claude") {
    $SkillsDir = "$Target\.claude\skills"
} elseif (Test-Path "$Target\.mimocode") {
    $SkillsDir = "$Target\.mimocode\skills"
} else {
    $SkillsDir = "$Target\.claude\skills"
}

Write-Host "Installing Apple Design skills to: $SkillsDir" -ForegroundColor Cyan
Write-Host ""

New-Item -ItemType Directory -Force -Path $SkillsDir | Out-Null

$skills = Get-ChildItem -Path "$RepoDir\skills" -Directory
foreach ($skill in $skills) {
    Write-Host "  -> $($skill.Name)" -ForegroundColor Green
    Copy-Item -Recurse -Force "$($skill.FullName)" "$SkillsDir\$($skill.Name)"
}

Write-Host ""
Write-Host "Done! Installed $($skills.Count) skills." -ForegroundColor Cyan
Write-Host ""
Write-Host "Skills installed:" -ForegroundColor Yellow
Get-ChildItem -Path $SkillsDir -Directory | ForEach-Object { Write-Host "  $($_.Name)" }
