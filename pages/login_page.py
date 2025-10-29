from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")
        self.dashboard_header = page.locator("header h6")


    def navigate(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username: str, password: str):
        
        expect(self.username_input).to_be_visible(timeout=8000)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

        
        expect(self.dashboard_header).to_be_visible(timeout=10000)
