Set-Location $PSScriptRoot
Write-Host "Starting Module Discovery Dashboard..."
Write-Host "Open http://localhost:5555/view/dashboard in your browser."
python -m uvicorn api_server:app --host 127.0.0.1 --port 5555 --reload