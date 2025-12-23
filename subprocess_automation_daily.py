import subprocess

task_name = "Daily_news_automation"
exe_path = "Z:/python_automation/dist/news_automation_everyday_3.exe"


command = [
    "schtasks",
    "/create",
    "/sc", "daily",
    "/st", "09:00",
    "/tn", task_name,
    "/tr", f'python "{exe_path}"',
    "/f"
]

subprocess.run(command, check=True)

print("Windows scheduled task created successfully!")