
# 📄 README.md

```md
# 📰 Headless Football News Automation (Windows)

This project automates the daily extraction of football news headlines from  
**The Sun – Football section** using **Selenium (headless Chrome)**, saves the data as a CSV file, converts the script into a Windows `.exe`, and schedules it to run automatically every day at **9:00 AM** using **Windows Task Scheduler**.

---
```
## 🚀 Features
```
- Headless web scraping using Selenium
- Extracts:
  - Headline titles
  - Subtitles / descriptions
  - Article links
- Saves data as a CSV file with date-based naming
- Converts Python script into a standalone `.exe`
- Automatically schedules the task daily using Windows Task Scheduler

---
```
## 📁 Project Structure


```

python_automation/  
│  
├── news_automation_everyday_3.py # Main scraper script  
├── schedule_task.py # Task Scheduler automation (subprocess)  
├── requirements.txt # Python dependencies  
├── README.md  
│  
├── dist/  
│ └── news_automation_everyday_3.exe # Generated EXE (after PyInstaller)  
│  
└── myenv/ # Virtual environment (optional)

```

---

## 🧠 How the Scraper Works

- Launches Chrome in headless mode
- Loads:  
  https://www.thesun.co.uk/sport/football/
- Extracts elements with:
  ``xpath
  //div[@class="story__copy-container"]
``

-   Saves CSV file in the same directory as the executable:

    headless_news_MM_DD_YYYY.csv
  ``

## STEPS

Create a virtual environment (recommended):

```bash
python -m venv myenv
myenv\Scripts\activate

```

Install dependencies:

```bash
pip install -r requirements.txt

```
> ⚠️ Chrome must be installed on the system.  
> Selenium (v4.6+) automatically manages ChromeDriver.

----------

## ▶️ Run the Script (Python)

```bash
python news_automation_everyday_3.py

```

A CSV file will be created in the **Python executable directory** (or EXE directory once packaged).

----------

## 🔧 Convert Python Script to EXE

on powershell:

```bash
pyinstaller --onefile --noconsole news_automation_everyday_3.py

```

Output:

```
dist/news_automation_everyday_3.exe

```

-   `--onefile` → single executable
    
-   `--noconsole` → no terminal popup (recommended for scheduled tasks)
    

----------

## ⏰ Schedule Daily Execution (Windows)

The following script creates a **Windows Scheduled Task** that runs the EXE daily at **9:00 AM**.
Run once:

```bash
python schedule_task.py

```
----------

## ✅ Verify Scheduled Task

### Command line

```powershell
schtasks /query | findstr Daily_news_automation

```
#### or
### GUI

-   Open **Task Scheduler**
    
-   Go to **Task Scheduler Library**
    
-   Look for **Daily_news_automation**
    

----------

## 📂 Where Are CSV Files Stored?

When running as an `.exe`, CSV files are saved to:

```
dist/
├── headless_news_MM_DD_YYYY.csv

```

This is controlled by:

```python
application_path = os.path.dirname(sys.executable)

```
----------

## ⚠️ Important Notes & Pitfalls

-   ❌ Do NOT name files `subprocess.py`, `datetime.py`, `selenium.py`
    
-   ❌ Do NOT use relative paths in scheduled tasks
    
-   ✅ Always use absolute paths for EXE and output files
    
-   ✅ Set "Run whether user is logged on or not" in Task Scheduler
    
-   ✅ Headless mode uses:
    
    ```python
    options.add_argument("--headless=new")
    
    ```
    

----------

## 🔐 Legal & Ethical Notice

-   This project is for **educational and personal use**
    
-   Websites may block or restrict scraping
    
-   Respect website **Terms of Service**
    
----------

## 👤 Author - Aryan 
```
Python • Selenium • Xpath • Subprocess • pyinstaller • Automation • Windows Scheduling 


```
