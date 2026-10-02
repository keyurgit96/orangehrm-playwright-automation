class basePage:
    def __init__(self,page):
        self._page = page
        self._oxdLocator = page.locator(".oxd-select-text-input")
        self._dateInput = page.get_by_placeholder("yyyy-dd-mm")
        self._yearSelector = page.locator(".oxd-calendar-selector-year")
        self._monthSelector = page.locator(".oxd-calendar-selector-month")
        self._dateSelector = page.get_by_text
        self._punchcomment = page.get_by_placeholder("Type here")
        self._inButton = page.get_by_role("button", name="In")
        self._outButton = page.get_by_role("button", name="Out")
        self._punchButton = page.locator(".orangehrm-attendance-card-action")
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._loginButton = page.get_by_role("button", name="Login")
        self._attachment = page.locator(".orangehrm-attachment")
        self._addButton = self._attachment.get_by_role("button", name="Add")
        self._fileButton = self._attachment.get_by_role("button", name="Browse")
        self._saveButton = self._attachment.get_by_role("button", name="Save")
        self._comment = page.get_by_placeholder("Add a comment")