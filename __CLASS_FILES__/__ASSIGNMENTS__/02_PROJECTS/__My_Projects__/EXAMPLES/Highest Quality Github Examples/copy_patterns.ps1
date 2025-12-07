# Copy all design pattern files to unified structure
$base = "c:\Users\WORK_ADMIN\Documents\__WORK__\01_COLLEGE\FALL_2025\COSC_1336_09\__CLASS_FILES__\__ASSIGNMENTS__\02_PROJECTS\__My_Projects__\EXAMPLES\Highest Quality Github Examples"
$templates = "$base\TEMPLATES"
$unified = "$base\UNIFIED_PATTERNS"

# Copy from Design-Patterns-in-Python (flat structure)
Write-Host "Copying Design-Patterns-in-Python..."
Copy-Item "$templates\Design-Patterns-in-Python\*.py" "$unified\other\" -Exclude "README.md"

# Copy from design-patterns-python
Write-Host "Copying design-patterns-python..."
Get-ChildItem "$templates\design-patterns-python\src" -Recurse -Filter "main.py" | ForEach-Object {
    Copy-Item $_.FullName "$unified\other\refactoring_$($_.Directory.Parent.Name)_main.py"
}

# Copy from Python-Design-Patterns
Write-Host "Copying Python-Design-Patterns..."
robocopy "$templates\Python-Design-Patterns\src" "$unified" *.py /S /NJH /NJS /NFL /NDL | Out-Null

# Copy from python_design_patterns
Write-Host "Copying python_design_patterns..."
Copy-Item "$templates\python_design_patterns\adapter\*.py" "$unified\structural\"
Copy-Item "$templates\python_design_patterns\bridge\*.py" "$unified\structural\"
Copy-Item "$templates\python_design_patterns\builder\*.py" "$unified\creational\"
Copy-Item "$templates\python_design_patterns\chain_of_res\*.py" "$unified\behavioral\"
Copy-Item "$templates\python_design_patterns\command\*.py" "$unified\behavioral\"
Copy-Item "$templates\python_design_patterns\composite\*.py" "$unified\structural\"
Copy-Item "$templates\python_design_patterns\decorator\*.py" "$unified\structural\"
Copy-Item "$templates\python_design_patterns\facade\*.py" "$unified\structural\"
Copy-Item "$templates\python_design_patterns\factories\*.py" "$unified\creational\"
Copy-Item "$templates\python_design_patterns\flyweight\*.py" "$unified\structural\"
Copy-Item "$templates\python_design_patterns\interpreter\*.py" "$unified\behavioral\"
Copy-Item "$templates\python_design_patterns\iterator\*.py" "$unified\behavioral\"
Copy-Item "$templates\python_design_patterns\mediator\*.py" "$unified\behavioral\"
Copy-Item "$templates\python_design_patterns\memento\*.py" "$unified\behavioral\"
Copy-Item "$templates\python_design_patterns\observer\*.py" "$unified\behavioral\"
Copy-Item "$templates\python_design_patterns\prototype\*.py" "$unified\creational\"
Copy-Item "$templates\python_design_patterns\proxy\*.py" "$unified\structural\"
Copy-Item "$templates\python_design_patterns\singleton\*.py" "$unified\creational\"
Copy-Item "$templates\python_design_patterns\solid\*.py" "$unified\solid\"
Copy-Item "$templates\python_design_patterns\state\*.py" "$unified\behavioral\"
Copy-Item "$templates\python_design_patterns\strategy\*.py" "$unified\behavioral\"
Copy-Item "$templates\python_design_patterns\template\*.py" "$unified\behavioral\"
Copy-Item "$templates\python_design_patterns\visitor\*.py" "$unified\behavioral\"

Write-Host "All patterns copied successfully!"
Write-Host "Counting files..."
$counts = @{
    behavioral = (Get-ChildItem "$unified\behavioral" -Filter *.py).Count
    creational = (Get-ChildItem "$unified\creational" -Filter *.py).Count
    structural = (Get-ChildItem "$unified\structural" -Filter *.py).Count
    fundamental = (Get-ChildItem "$unified\fundamental" -Filter *.py).Count
    solid = (Get-ChildItem "$unified\solid" -Filter *.py).Count
    other = (Get-ChildItem "$unified\other" -Filter *.py -Recurse).Count
}
Write-Host "Behavioral: $($counts.behavioral) files"
Write-Host "Creational: $($counts.creational) files"
Write-Host "Structural: $($counts.structural) files"
Write-Host "Fundamental: $($counts.fundamental) files"
Write-Host "SOLID: $($counts.solid) files"
Write-Host "Other: $($counts.other) files"
