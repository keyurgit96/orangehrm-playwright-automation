class loginDetails:
    def __init__(self, page, username, password):
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._loginButton = page.get_by_role("button", name="Login")

    def login(self):
        self._username.fill(self._username)
        self._password.fill(self._password)
        self._loginButton.click()
