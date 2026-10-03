from src import pages


class loginDetails:
    def __init__(self, page, username, password):
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._loginButton = page.get_by_role("button", name="Login")
        self.username = username
        self.password = password
        self.page = page

    def login(self):
        self.page.wait_for_load_state("domcontentloaded")
        self._username.fill(self.username)
        self._password.fill(self.password)
        self._loginButton.click()
