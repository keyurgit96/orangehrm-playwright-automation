class updateTimesheet:
    def __init__(self,page):
        self.page=page
    def punchIn(self):
        status=self.page.locator(".orangehrm-attendance-card-state").inner_text()
        if status.lower() =="punched out":
            self.page.locator(".orangehrm-attendance-card-action").click()
        else:
            raise AssertionError(f"User Status: {status}")
    def updateInDate(self,year,month,day,comment=None):
        if type(year)==int:
            year=str(year)
        if type(day)==int:
            day=str(day)
        self.page.get_by_placeholder('yyyy-dd-mm').click()
        self.page.locator(".oxd-calendar-selector-year").click()
        self.page.get_by_text(year,exact=True).last.click()
        self.page.locator(".oxd-calendar-selector-month").click()
        self.page.get_by_text(month).last.click()
        self.page.get_by_text(day,exact=True).last.click()
        if comment!=None:
            self.page.get_by_placeholder('Type here').fill(comment)
        self.page.get_by_role('button',name='In').click()
        status=self.page.locator(".orangehrm-main-title").inner_text().lower()
        import time ; time.sleep(5)
        assert status == 'punch out'