class sideBar:
    def __init__(self, page):
        self._myInfo = page.get_by_text("My Info")
        self._recruitment = page.get_by_text("Recruitment")

    def myInfo(self):
        self._myInfo.click()

    def recruitment(self):
        self._recruitment.click()


class userMenu:
    def __init__(self, page):
        self._logoutButton = page.locator(".oxd-userdropdown-name")
        self._logoutMenu = page.get_by_text("Logout")

    def logout(self):
        try:
            self._logoutButton.click()
            self._logoutMenu.click()
        except Exception as e:
            raise RuntimeError(f"Failed to log out: {e}") from e
