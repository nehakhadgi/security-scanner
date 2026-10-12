
# AI Security Scanner for Python

A lightweight, static application security testing (SAST) utility powered by the **Google Gemini API** that analyzes Python source code for critical security vulnerabilities, weak cryptographic patterns, and bad practices.

This scanner parses target code files, coordinates with Gemini to run heuristic security reviews, and generates high-fidelity, color-coded terminal reports with classified severity levels and remediation advice.

---

## 🚀 Key Features

* **AI-Powered Static Analysis**: Utilizes generative AI (`gemini-3.8-flash`) to trace complex logic paths and catch subtle structural bugs.
* **Vulnerability Class Mapping**: Audits source code for major vulnerability classes including:
  * SQL Injection (SQLi)
  * Command Injection
  * Broken Authentication (hardcoded secrets, keys, and passwords)
  * Insecure Cryptographic Hashing (e.g., MD5, SHA-1)
* **High-Contrast Terminal UI**: Colorized outputs mapping severity ratings (HIGH, MEDIUM, LOW) to logical colors using `colorama` for immediate threat triage.
* **Dynamic CLI Execution**: Flexible input structure allowing engineers to scan specific files dynamically via command-line arguments.
* **Production-Safe Configuration**: Strict dotenv isolation mapping sensitive API credentials safely out of source control.

---

## 🛠️ Prerequisites

* **Operating System**: Windows 10/11
* **Runtime**: Python 3.10 or higher
* **Credentials**: Google AI Studio API Key

---

## 📦 Installation & Setup

Follow these steps to set up the project locally on Windows:

### 1. Set Up the Virtual Environment
Open **PowerShell** in your project directory and execute:
```powershell
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\Activate.ps1
```

### 2. Install Required Dependencies
Install the Python library ecosystem:
```powershell
pip install google-generativeai python-dotenv colorama
```

### 3. Securely Configure Credentials
Create a `.env` file in the root of the project to isolate your keys:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```
*(Make sure `.env` is listed in your `.gitignore` to prevent leaking keys to version control!)*

---

## 💻 Usage

To run a static analysis on any target Python file, invoke the CLI script with the filepath as an argument:

```powershell
python scanner.py vulnerable.py
```

### Example Test File (`vulnerable.py`)
To verify the scanner's heuristic analysis, you can create a test file containing deliberate vulnerabilities:
```python
import hashlib
import sqlite3

# Hardcoded credentials
DB_PASSWORD = "password123"

def authenticate(username, password):
    # SQL Injection path
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchone()
```

---

## 📁 Project Architecture

```text
security-scanner/
│
├── venv/                 # Local Python isolation environment
├── .env                  # Sensitive system secrets (ignored by Git)
├── .gitignore            # Tells Git what directory elements to ignore
├── scanner.py            # Primary scanning CLI script & API controller
├── vulnerable.py         # Test code file populated with vulnerabilities
└── README.md             # Project documentation (this file)
```

---



