# Define the name of the virtual environment
$venvName = "venv"

# Define the path to the requirements file
$requirementsFile = "requirements.txt"

# Check if the virtual environment already exists
if (Test-Path -Path $venvName) {
    Write-Host "Virtual environment '$venvName' already exists." -ForegroundColor Yellow
} else {
    Write-Host "Creating virtual environment '$venvName'..." -ForegroundColor Green
    py -m venv $venvName
}

# Activate the virtual environment
Write-Host "Activating virtual environment '$venvName'..." -ForegroundColor Blue
& "$venvName\Scripts\Activate.ps1"

# Check if the requirements file exists
if (Test-Path -Path $requirementsFile) {
    Write-Host "Installing dependencies from '$requirementsFile'..." -ForegroundColor Green
    pip install -r $requirementsFile
} else {
    Write-Host "No '$requirementsFile' found. Skipping dependency installation." -ForegroundColor Red
}

Write-Host "Virtual environment setup complete." -ForegroundColor Green