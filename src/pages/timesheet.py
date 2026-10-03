from src.pages.basePage import basePage


class markAttendance(basePage):
    def __init__(self, page):
        super().__init__(page)

    def punchIn(self, state="punched out"):
        if self._status.lower() == state:
            self._punchButton.click()
        else:
            raise AssertionError(f"User Status: {self._status}")

    def punchOut(self, state="punched In"):
        self.punchIn(state)


class attendanceDetails:
    def __init__(self, page, year, month, day, comment=None):
        self.page = page
        self._dateInput = page.get_by_placeholder("yyyy-dd-mm")
        self._yearSelector = page.locator(".oxd-calendar-selector-year")
        self._monthSelector = page.locator(".oxd-calendar-selector-month")
        self._dateSelector = page.get_by_text
        self._comment = page.get_by_placeholder("Type here")
        self._inButton = page.get_by_role("button", name="In")
        self._outButton = page.get_by_role("button", name="Out")
        self.year = year
        self.month = month
        self.day = day
        self.comment = comment

    def updateInDetails(self, inButton=True):
        if type(self.year) == int:
            year = str(self.year)
        if type(self.day) == int:
            day = str(self.day)
        self._dateInput.click()
        self._yearSelector.click()
        self._dateSelector(year).last.click()
        self._monthSelector.click()
        self._dateSelector(self.month).last.click()
        self._dateSelector(day).last.click()
        if self.comment != None:
            self._comment.fill(self.comment)
        if inButton:
            self._inButton.click()
        elif not inButton:
            self._outButton.click()

    def updateOutDetails(self, inButton=True):
        self.updateInDetails(False)
