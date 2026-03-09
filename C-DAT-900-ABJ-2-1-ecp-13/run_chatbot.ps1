Write-Host "=== RASA + GPT Chatbot Launcher (Windows PowerShell) ===" -ForegroundColor Cyan

# ---------- CHECK DOCKER ----------
Write-Host "`n[1/6] Vérification de Docker Desktop..." -ForegroundColor Yellow

$dockerStatus = (Get-Process "Docker Desktop" -ErrorAction SilentlyContinue)

if (-not $dockerStatus) {
    Write-Host "Docker Desktop n'est pas lancé. Démarrage en cours..." -ForegroundColor Red
    Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    Start-Sleep -Seconds 12
} else {
    Write-Host "Docker Desktop est actif." -ForegroundColor Green
}

# ---------- CHECK WSL2 ----------
Write-Host "`n[2/6] Vérification du backend WSL2..." -ForegroundColor Yellow

$wslCheck = wsl --status 2>$null

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ WSL2 n'est pas installé ou activé." -ForegroundColor Red
    Write-Host "Active WSL2 avec :" -ForegroundColor White
    Write-Host "  wsl --install" -ForegroundColor Green
    exit
} else {
    Write-Host "WSL2 OK." -ForegroundColor Green
}

# ---------- CHECK PROJECT LOCATION ----------
Write-Host "`n[3/6] Vérification du chemin du projet..." -ForegroundColor Yellow

$currentPath = (Get-Location).Path

if ($currentPath -like "*OneDrive*") {
    Write-Host "❌ ERREUR : Le projet est dans OneDrive !" -ForegroundColor Red
    $newPath = "C:\docker_projects\rasa_gpt_full_project"

    Write-Host "Déplacement automatique du projet vers :" -ForegroundColor White
    Write-Host "  $newPath" -ForegroundColor Green

    New-Item -ItemType Directory -Force -Path $newPath | Out-Null
    Copy-Item -Path $currentPath\* -Destination $newPath -Recurse -Force

    Set-Location $newPath
    Write-Host "Projet déplacé avec succès dans un dossier compatible Docker." -ForegroundColor Green
} else {
    Write-Host "Chemin OK ✔️" -ForegroundColor Green
}

# ---------- DOCKER COMPOSE UP ----------
Write-Host "`n[4/6] Construction des containers Docker..." -ForegroundColor Yellow

docker compose build

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Erreur lors du build Docker." -ForegroundColor Red
    exit
}

# ---------- RUN PROJECT ----------
Write-Host "`n[5/6] Démarrage du chatbot..." -ForegroundColor Yellow

Start-Process powershell -ArgumentList "docker compose up"

Write-Host "Le chatbot démarre dans un autre terminal..." -ForegroundColor Green

# ---------- NGROK INFO ----------
Write-Host "`n[6/6] Information NGROK" -ForegroundColor Cyan
Write-Host "Pour connecter WhatsApp, lance : " -ForegroundColor White
Write-Host "  ngrok http 5005" -ForegroundColor Green
Write-Host "puis colle l'URL HTTPS dans Twilio :" -ForegroundColor Yellow
Write-Host "  https://xxxx.ngrok-free.app/webhooks/twilio/webhook" -ForegroundColor Magenta

Write-Host "`n=== Chatbot prêt à fonctionner ! ===" -ForegroundColor Cyan
