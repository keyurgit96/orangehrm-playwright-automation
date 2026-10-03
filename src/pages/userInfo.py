from .basePage import basePage


class userMenu(basePage):
    def __init__(self, page):
        super().__init__(page)
        self._logoutMenu = self.page.get_by_text("Logout")

    def logout(self):
        try:
            self._logoutButton.click()
            self._logoutMenu.click()
        except Exception as e:
            raise RuntimeError(f"Failed to log out: {e}") from e
