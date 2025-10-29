from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_delete_user():
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

        # Delete user
        admin.delete_user("testuser123")

        browser.close()
