# Automated script to uninstall disabled VS Code extensions
# This script identifies and uninstalls disabled extensions

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "VS Code Disabled Extensions Uninstaller" -ForegroundColor Cyan
Write-Host "======================================`n" -ForegroundColor Cyan

# Get VS Code's state database path
$stateDbPath = "$env:APPDATA\Code\User\globalStorage\state.vscdb"
$storagePath = "$env:APPDATA\Code\User\globalStorage\storage.json"

# Try to find disabled extensions in storage.json
if (Test-Path $storagePath) {
    Write-Host "Reading VS Code storage..." -ForegroundColor Yellow
    $storage = Get-Content $storagePath -Raw | ConvertFrom-Json
    
    # Look for disabled extensions in various possible keys
    $disabledExtensions = @()
    
    # Check common storage keys for disabled extensions
    $storage.PSObject.Properties | ForEach-Object {
        if ($_.Name -match "extensionsIdentifiers" -and $_.Value -is [array]) {
            $disabledExtensions += $_.Value
        }
    }
}

# Alternative: Parse extensions.json files to find disabled ones
$extensionsJsonFiles = Get-ChildItem -Path "$env:APPDATA\Code\User\profiles" -Recurse -Filter "extensions.json" -ErrorAction SilentlyContinue

$allInstalled = @()
$extensionsJsonFiles | ForEach-Object {
    $content = Get-Content $_.FullName -Raw | ConvertFrom-Json
    $allInstalled += $content
}

# Since we can't reliably detect disabled extensions via CLI,
# let's create an interactive prompt
Write-Host "`nVS Code doesn't expose disabled extensions via CLI." -ForegroundColor Red
Write-Host "Please choose an option:`n" -ForegroundColor Yellow

Write-Host "1. Manual entry: I'll prompt you to paste extension IDs" -ForegroundColor Green
Write-Host "2. Check extensions.json: I'll show you all extensions and you can identify disabled ones" -ForegroundColor Green
Write-Host "3. Open VS Code Extensions view for manual review" -ForegroundColor Green
Write-Host "4. Exit" -ForegroundColor Green

$choice = Read-Host "`nEnter your choice (1-4)"

switch ($choice) {
    "1" {
        Write-Host "`nInstructions:" -ForegroundColor Cyan
        Write-Host "1. Open VS Code" -ForegroundColor White
        Write-Host "2. Go to Extensions (Ctrl+Shift+X)" -ForegroundColor White
        Write-Host "3. Filter by @disabled" -ForegroundColor White
        Write-Host "4. Copy each disabled extension ID and paste below" -ForegroundColor White
        Write-Host "5. Type 'DONE' when finished`n" -ForegroundColor White
        
        $disabledList = @()
        while ($true) {
            $input = Read-Host "Enter extension ID (or DONE)"
            if ($input -eq "DONE") { break }
            if ($input) { $disabledList += $input.Trim() }
        }
        
        if ($disabledList.Count -gt 0) {
            Write-Host "`nFound $($disabledList.Count) disabled extension(s)" -ForegroundColor Yellow
            Write-Host "Uninstalling...`n" -ForegroundColor Yellow
            
            foreach ($ext in $disabledList) {
                Write-Host "Uninstalling: $ext" -ForegroundColor Cyan
                code --uninstall-extension $ext
            }
            
            Write-Host "`nCompleted!" -ForegroundColor Green
        }
    }
    "2" {
        Write-Host "`nListing all installed extensions..." -ForegroundColor Yellow
        $all = code --list-extensions
        $all | ForEach-Object { Write-Host $_ }
        
        Write-Host "`nTotal: $($all.Count) extensions" -ForegroundColor Cyan
        Write-Host "`nNow check VS Code to identify which are disabled," -ForegroundColor Yellow
        Write-Host "then run this script again and choose option 1." -ForegroundColor Yellow
    }
    "3" {
        Write-Host "`nOpening VS Code..." -ForegroundColor Yellow
        code --command workbench.extensions.action.showDisabledExtensions
        Start-Sleep -Seconds 2
        Write-Host "Extension view should now show disabled extensions." -ForegroundColor Green
        Write-Host "Manually uninstall them, or run this script again for automated removal." -ForegroundColor Yellow
    }
    default {
        Write-Host "Exiting..." -ForegroundColor Gray
    }
}
