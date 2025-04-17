# Define font paths
$FontFolder = "$PSScriptRoot\Fonts"
$FontDir = "$env:WINDIR\Fonts"

# Function to pause before exiting
function Pause-And-Exit {
    Write-Host "`nPress ENTER to exit..."
    Read-Host | Out-Null
    Exit
}

try {
    # Check if running as Admin
    $CurrentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    $Principal = New-Object System.Security.Principal.WindowsPrincipal $CurrentUser
    if (-not $Principal.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)) {
        Write-Host "❌ Run this script as Administrator!" -ForegroundColor Red
        Pause-And-Exit
    }

    # Check if font folder exists
    if (-not (Test-Path $FontFolder)) {
        Write-Host "❌ Font folder not found!" -ForegroundColor Red
        Pause-And-Exit
    }

    # Install each .otf file
    Get-ChildItem -Path $FontFolder -Filter "*.otf" | ForEach-Object {
        Write-Host "Installing: $($_.Name)"
        Copy-Item $_.FullName -Destination $FontDir -Force -ErrorAction Stop
        $FontName = $_.BaseName
        $FontRegPath = "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts"
        New-ItemProperty -Path $FontRegPath -Name $FontName -PropertyType String -Value $_.Name -Force -ErrorAction Stop
    }

    # Restart Explorer to refresh fonts
    #Stop-Process -Name explorer -Force -ErrorAction SilentlyContinue
    #Start-Process "explorer.exe"

    Write-Host "✅ Fonts installed successfully!" -ForegroundColor Green
}
catch {
    Write-Host "❌ An error occurred: $_" -ForegroundColor Red
    Pause-And-Exit
}

Pause-And-Exit
