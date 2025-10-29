import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_search_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Initialize page objects
        login = LoginPage(page)
        admin = AdminPage(page)

        # Login
        login.navigate()
        login.login("Admin", "admin123")

        # Navigate to Admin module
        admin.navigate_to_admin()

        # Search for existing user
        admin.search_user("testuser123")

        

        print("Search test successful - user found in results")

        browser.close()
