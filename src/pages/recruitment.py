class recruitment:
    def __init__(self, page):
        self.page = page

    def recruitmentPage(self):
        self.page.get_by_text("Recruitment").click()

    def addCandidate(
        self, jobtitle=None, vacancy=None, hiringManager=None, status=None
    ):
        self.page.get_by_text("Candidates").first.click()
        if jobtitle:
            self.page.locator(".oxd-select-text-input").nth(0).click()
            self.page.get_by_text(jobtitle).first.click()
        if vacancy:
            self.page.locator(".oxd-select-text-input").nth(1).click()
            self.page.get_by_text(vacancy).first.click()
        if hiringManager:
            self.page.locator(".oxd-select-text-input").nth(2).click()
            self.page.get_by_text(hiringManager).first.click()
        if status:
            self.page.locator(".oxd-select-text-input").nth(3).click()
            self.page.get_by_text(status).first.click()
        self.page.get_by_role("button", name="Search").click()
