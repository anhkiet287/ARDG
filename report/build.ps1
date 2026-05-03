$ErrorActionPreference = "Stop"

$reportDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$miktexBin = Join-Path $env:LOCALAPPDATA "Programs\MiKTeX\miktex\bin\x64"

if (Test-Path (Join-Path $miktexBin "xelatex.exe")) {
    $env:PATH = "$miktexBin;$env:PATH"
}

foreach ($tool in @("xelatex", "bibtex")) {
    if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) {
        throw "Missing required tool '$tool'. Install MiKTeX and make sure its bin directory is on PATH."
    }
}

function Invoke-LatexTool {
    param(
        [Parameter(Mandatory = $true)]
        [string] $Tool,

        [Parameter(Mandatory = $true)]
        [string[]] $Arguments
    )

    & $Tool @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$Tool failed with exit code $LASTEXITCODE."
    }
}

Push-Location $reportDir
try {
    Invoke-LatexTool "xelatex" @("-interaction=nonstopmode", "-file-line-error", "main.tex")
    Invoke-LatexTool "bibtex" @("main")
    Invoke-LatexTool "xelatex" @("-interaction=nonstopmode", "-file-line-error", "main.tex")
    Invoke-LatexTool "xelatex" @("-interaction=nonstopmode", "-file-line-error", "main.tex")
}
finally {
    Pop-Location
}
