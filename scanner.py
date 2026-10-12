import os
import time
from dotenv import load_dotenv
import google.generativeai as genai
from colorama import init, Fore, Style
import sys

# Initialize colorama
init(autoreset=True)
# Load environment variables from .env file
load_dotenv()

# Configure with your API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel("gemini-3.8-flash")

# ===========================================
# =================
# Test code with a security vulnerability
# Vulnerable code example 1: SQL Injection
vulnerable_code_1 = '''
def get_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()
'''

# Vulnerable code example 2: Hardcoded credentials
vulnerable_code_2 = '''
DATABASE_PASSWORD = "supersecret123"
API_KEY = "sk-1234567890abcdef"

def connect_db():
    return psycopg2.connect(
        host="localhost",
        password=DATABASE_PASSWORD
    )
'''

# Vulnerable code example 3: Weak cryptography
vulnerable_code_3 = '''
import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
'''
security_prompt = """
Analyze this code for security vulnerabilities. Be concise.

For each issue use this exact format:

- --
SEVERITY: [CRITICAL/HIGH/MEDIUM/LOW]
TYPE: [Vulnerability Name]
DESCRIPTION: [One sentence explaining the issue]
IMPACT: [One sentence on potential damage]
FIX: [Code snippet only]
---

Code:
{code}
"""

def add_colors_to_output(text):
    """Add colors to severity levels in the output."""
    text = text.replace("SEVERITY: CRITICAL", f"SEVERITY: {Fore.RED}{Style.BRIGHT}CRITICAL{Style.RESET_ALL}")
    text = text.replace("SEVERITY: HIGH", f"SEVERITY: {Fore.YELLOW}{Style.BRIGHT}HIGH{Style.RESET_ALL}")
    text = text.replace("SEVERITY: MEDIUM", f"SEVERITY: {Fore.BLUE}MEDIUM{Style.RESET_ALL}")
    text = text.replace("SEVERITY: LOW", f"SEVERITY: {Fore.GREEN}LOW{Style.RESET_ALL}")
    return text
def scan_file(filepath):
    """Read a file and analyze it for vulnerabilities."""
    try:
        with open(filepath, 'r') as f:
            code = f.read()

        print(f"\n{'=' * 60}")
        print(f"Scanning: {filepath}")
        print(f"{'=' * 60}\n")

        # Use the existing security prompt
        response = model.generate_content(security_prompt.format(code=code))
        output = add_colors_to_output(response.text)
        print(output)
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File '{filepath}' not found.{Style.RESET_ALL}")
#Your code goes here
# Test with SQL injection example
print("=" * 50)
print("Analyzing SQL Injection Example...")
print("=" * 50)

response = model.generate_content(security_prompt.format(code=vulnerable_code_1))
output = add_colors_to_output(response.text)
print(output)

# Test with hardcoded credentials
print("\n" + "=" * 50)
print("Analyzing Hardcoded Credentials Example...")
print("=" * 50)

response = model.generate_content(security_prompt.format(code=vulnerable_code_2))
output = add_colors_to_output(response.text)
print(output)

# Test with weak cryptography
print("\n" + "=" * 50)
print("Analyzing Weak Cryptography Example...")
print("=" * 50)

response = model.generate_content(security_prompt.format(code=vulnerable_code_3))
output = add_colors_to_output(response.text)
print(output)
# ============================================================

# Test with a simple prompt

# Example: Adding a 12-second pause between each analysis
print("==================================================")
print("Analyzing SQL Injection Example...")
response = model.generate_content(security_prompt.format(code=vulnerable_code_1))
print(response.text)

# Pause for 12 seconds to prevent hitting the 5 RPM limit
time.sleep(12)

print("==================================================")
print("Analyzing Broken Authentication Example...")
response = model.generate_content(security_prompt.format(code=vulnerable_code_2))
print(response.text)

# Pause again before the next call
time.sleep(12)

print("==================================================")
print("Analyzing Sensitive Data Exposure Example...")
response = model.generate_content(security_prompt.format(code=vulnerable_code_3))
print(response.text)
    
# Test with SQL injection example
print("=" * 50)
print("Analyzing SQL Injection Example...")
print("=" * 50)

response = model.generate_content(security_prompt.format(code=vulnerable_code_1))
print(response.text)

# Test with hardcoded credentials
print("\n" + "=" * 50)
print("Analyzing Hardcoded Credentials Example...")
print("=" * 50)

response = model.generate_content(security_prompt.format(code=vulnerable_code_2))
print(response.text)

# Test with weak cryptography
print("\n" + "=" * 50)
print("Analyzing Weak Cryptography Example...")
print("=" * 50)

response = model.generate_content(security_prompt.format(code=vulnerable_code_3))
print(response.text)

# ============================================================
# YOUR CODE GOES ABOVE HERE
# ============================================================
# Check if a filename was provided
if len(sys.argv) > 1:
    filepath = sys.argv[1]
    print(f"Scanning file: {filepath}\n")
    scan_file(filepath)
else:
    print("Usage: python scanner.py <filepath>")
    print("Example: python scanner.py vulnerable.py")


    