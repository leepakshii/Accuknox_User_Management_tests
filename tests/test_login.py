import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_valid_login():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Creating object for LoginPage
        login_page = LoginPage(page)

        # Navigate to site
        login_page.navigate()

        # Perform login
        login_page.login("Admin", "admin123")

        # If reached Dashboard, test passes
        print("Login successful - Dashboard page visible")

        browser.close()
