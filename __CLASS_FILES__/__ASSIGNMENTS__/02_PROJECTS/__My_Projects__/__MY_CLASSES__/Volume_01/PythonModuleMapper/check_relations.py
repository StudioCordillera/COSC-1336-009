import sqlite3
from pathlib import Path

db_path = Path("c:/Users/WORK_ADMIN/Documents/__WORK__/01_COLLEGE/FALL_2025/COSC_1336_09/__CLASS_FILES__/__ASSIGNMENTS__/02_PROJECTS/__My_Projects__/__MY_CLASSES__/Volume_01/PythonModuleMapper/python_modules.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT name, module_id FROM functions WHERE length(name) = 1")
rows = cursor.fetchall()
print(f"Single letter functions: {len(rows)}")
for row in rows:
    print(row)

conn.close()
