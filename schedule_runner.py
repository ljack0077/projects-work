import subprocess
import schedule
import time
import os

# --- CONFIG ---
TASKS = [
    {
        "name": "Run Python Script",
        "path": r"C:\Users\Desktop\my_script.py",
        "time": "09:00"  # daily at 9:00
    },
    {
        "name": "Run EXE App",
        "path": r"C:\Program Files\Notepad++\notepad++.exe",
        "time": "18:30"  # daily at 18:30
    }
]


def run_task(path):
    try:
        if path.endswith(".py"):
            subprocess.Popen(["python", path], shell=True)
        else:
            subprocess.Popen(path, shell=True)
        print(f"✅ Launched: {path}")
    except Exception as e:
        print(f"❌ Failed to run {path}: {e}")


# Register all tasks in the scheduler
for task in TASKS:
    schedule.every().day.at(task["time"]).do(run_task, path=task["path"])
    print(f"⏰ Scheduled '{task['name']}' at {task['time']}")


# Loop forever and execute when time matches
while True:
    schedule.run_pending()
    time.sleep(1)
