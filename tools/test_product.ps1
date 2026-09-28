[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $repoRoot

$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (Test-Path -LiteralPath $venvPython) {
    $pythonExe = $venvPython
} else {
    $pythonExe = (Get-Command python -ErrorAction Stop).Source
}

$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

Write-Host "==> Run video-spec-builder product verification suite (Windows)"

Write-Host "--> 1. Verify SKILL.md and References Structure"
$requiredRefs = @(
    "components-catalog.md",
    "dialogue-style.md",
    "pacing-rules.md",
    "question-bank.md",
    "scene-breakdown.md",
    "spec-rules.md",
    "workflow-0-1.md",
    "workflow-iteration.md"
)

foreach ($ref in $requiredRefs) {
    $refPath = Join-Path $repoRoot "references\$ref"
    if (-not (Test-Path -LiteralPath $refPath)) {
        throw "Missing required reference document: references\$ref"
    }
    $len = (Get-Item -LiteralPath $refPath).Length
    if ($len -lt 100) {
        throw "Reference document is unexpectedly truncated: references\$ref ($len bytes)"
    }
}
Write-Host "    All 8 reference documents verified."

Write-Host "--> 2. Verify Spec Template and SpaceX Example"
$templatePath = Join-Path $repoRoot "templates\video-spec-template.md"
$examplePath = Join-Path $repoRoot "examples\video-spec-spacex.md"
if (-not (Test-Path -LiteralPath $templatePath)) {
    throw "Missing templates\video-spec-template.md"
}
if (-not (Test-Path -LiteralPath $examplePath)) {
    throw "Missing examples\video-spec-spacex.md"
}
Write-Host "    Templates and examples verified."

Write-Host "--> 3. Verify Spec Mono Theme"
$monoDesign = Join-Path $repoRoot "spec-mono\design.md"
$monoTokens = Join-Path $repoRoot "spec-mono\tokens.css"
$monoComponents = Join-Path $repoRoot "spec-mono\spec-mono-components.md"
if (-not (Test-Path -LiteralPath $monoDesign) -or -not (Test-Path -LiteralPath $monoTokens) -or -not (Test-Path -LiteralPath $monoComponents)) {
    throw "Spec Mono theme files missing!"
}
Write-Host "    Spec Mono theme verified."

Write-Host "--> 4. Verify Full Code Component Library (13 files)"
$fullCodeFiles = Get-ChildItem -Path (Join-Path $repoRoot "Full Code") -Recurse -File
if ($fullCodeFiles.Count -lt 13) {
    throw "Full Code directory is incomplete: found $($fullCodeFiles.Count) files, expected at least 13."
}
Write-Host "    Full Code component library verified ($($fullCodeFiles.Count) files)."

Write-Host "--> 5. Execute Product Contract Tests (pytest)"
& $pythonExe -m pytest -c tools/pytest.ini tools/tests/test_skill_and_specs.py
if ($LASTEXITCODE -ne 0) {
    throw "Product contract tests failed with exit code $LASTEXITCODE"
}

Write-Host "PRODUCT TESTS GREEN"
