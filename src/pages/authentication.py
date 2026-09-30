class authentication:
    def __init__(self, username, password, playwright, url, browser="chrome"):
        self.username = username
        self.password = password
        self.browser = browser
        self.playwright = playwright
        self.url = url

    def login(self):
        if self.browser.lower() == "firefox":
            browser = self.playwright.firefox.launch(headless=False)
        elif self.browser.lower() == "chrome":
            browser = self.playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(self.url)
        page.get_by_placeholder("Username").fill(self.username)
        page.get_by_placeholder("Password").fill(self.password)
        page.get_by_role("button", name="Login").click()
        self.page = page
        return page

    def logout(self):
        try:
            self.page.locator(".oxd-userdropdown-name").click()
            self.page.get_by_text("Logout").click()
        except Exception as e:
            raise RuntimeError(f"Failed to log out: {e}") from e

        # context.close()
        # self.playwright.close()
