Write-Host ===================================
Write-Host       FridgeBook installation
Write-Host ===================================
Write-Host `n

# Check if python is already installed
Write-Host ====== Python ======

$p = &{python -V} 2>&1
$version = if($p -is [System.Management.Automation.ErrorRecord]) { $p.Exception.Message } else { $p }

if ($version -like '*Python 3.8.*') {
    Write-Host $p already installed. Skipping.
} else {
    Write-Host Python not installed
    Write-Host Python 3.8.2 will be installed now

    $scriptPath = Split-Path $MyInvocation.InvocationName
    & "$scriptPath\install-python.ps1"
}

Write-Host `n

# Install dependencies
Write-Host ====== Installing dependencies ======
pip install -r production-requirements.txt
Write-Host `n

# Migrate database
Write-Host ====== Database ======
python manage.py migrate
Write-Host `n

# Create superuser with
Write-Host ====== Administrator ======
Write-Host Please specify password for admin
python manage.py createsuperuser --username=admin --email "admin@fridgebook.com"
Write-Host `n

# Application successfully installed
Write-Host ====== Installation successful ======
Write-Host Application successfully installed
