class updateTimesheet:
    def __init__(self,page):
        self.page=page
    def punchIn(self):
        self.page.locator(".orangehrm-attendance-card-action").click()