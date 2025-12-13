import sys
from pathlib import Path
sys.path.insert(0, str(Path("c:/Users/WORK_ADMIN/Documents/__WORK__/01_COLLEGE/FALL_2025/COSC_1336_09/__CLASS_FILES__/__ASSIGNMENTS__/02_PROJECTS/__My_Projects__/__MY_CLASSES__/Volume_01/PythonModuleMapper")))

from scanner import ScanModuleCommand
import logging

# Configure logging to see debug output
logging.basicConfig(level=logging.DEBUG)

cmd = ScanModuleCommand("json")
result = cmd.execute()

print("Success:", result['success'])
if result['success']:
    print("Filepath:", result['data'].get('filepath'))
    print("Imports:", result['data'].get('imports'))
else:
    print("Error:", result.get('error'))
