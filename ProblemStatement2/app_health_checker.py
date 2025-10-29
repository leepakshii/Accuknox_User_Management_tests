"""
Application Health Checker
--------------------------
This script checks if a web application or API endpoint is up and running.

It sends an HTTP request and verifies the response status code:
- Status Code 200 → Application is UP
- Any other status or error → Application is DOWN

Libraries Used:
- requests: For sending HTTP requests
"""

import requests
from datetime import datetime

def check_app_health(url):
    print("\n----------------------------------------")
    print(" Application Health Check -", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("----------------------------------------")

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"{url} is UP and running (Status Code: {response.status_code})")
        else:
            print(f" {url} is reachable but returned an unexpected Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f" {url} is DOWN or not reachable.")
        print("Error:", e)

if __name__ == "__main__":
    # You can change this URL to the app you want to check
    url = input("Enter the URL of the application to check: ").strip()
    check_app_health(url)
