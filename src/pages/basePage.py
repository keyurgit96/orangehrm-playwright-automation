class basePage:
    def __init__(self, page):
        self.page = page
        self._myInfo = page.get_by_text("My Info")
        self._recruitment = page.get_by_text("Recruitment")
        self._logoutButton = page.locator(".oxd-userdropdown-name")
        self._punchButton = page.locator(".orangehrm-attendance-card-action")
        self._status_locator = self.page.locator(
            ".orangehrm-attendance-card-state"
        ).inner_text()

    def myInfo(self):
        self._myInfo.click()

    def recruitment(self):
        self._recruitment.click()
