import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_validate_user_update():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Page Objects
        login = LoginPage(page)
        admin = AdminPage(page)

        # Login
        login.navigate()
        login.login("Admin", "admin123")

        # Navigate to Admin module
        admin.navigate_to_admin()

        # Validate user update
        admin.validate_user_update(username="testuser123", expected_status="Disabled")

        print("Validation test successful - Updated user details verified")

        browser.close()
