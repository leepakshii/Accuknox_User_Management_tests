import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_add_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Create page objects
        login = LoginPage(page)
        admin = AdminPage(page)

        # Login
        login.navigate()
        login.login("Admin", "admin123")

        # Navigate to Admin module
        admin.navigate_to_admin()

        # Add new user
        admin.add_user(emp_name="Ravi M B", username="testuser123",status="Enabled" ,password="test@1234")

        print("User added successfully")

        browser.close()
