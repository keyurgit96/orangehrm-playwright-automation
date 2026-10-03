class recruitmentDetails:
    def __init__(
        self, page, jobtitle=None, vacancy=None, hiringManager=None, status=None
    ):
        self.page = page
        self.jobtitle = jobtitle
        self.vacancy = vacancy
        self.hiringManager = hiringManager
        self.status = status
        self._oxdLocator = page.locator(".oxd-select-text-input")
        self._selectFromDropDown = page.get_by_text

    def addCandidate(self):
        self.page.get_by_text("Candidates").first.click()
        if self.jobtitle:
            self._oxdLocator.nth(0).click()
            self._selectFromDropDown(self.jobtitle).first.click()
        if self.vacancy:
            self._oxdLocator.nth(1).click()
            self._selectFromDropDown(self.vacancy).first.click()
        if self.hiringManager:
            self._oxdLocator.nth(2).click()
            self._selectFromDropDown(self.hiringManager).first.click()
        if self.status:
            self._oxdLocator.nth(3).click()
            self._selectFromDropDown(self.status).first.click()
        self.page.get_by_role("button", name="Search").click()


class userInfo:
    def __init__(self, page, nationality=None, maritalStatus=None):
        self._oxdlocator = page.locator(".oxd-select-text-input")
        self._selectFromDropDown = page.get_by_text
        self._attachment = page.locator(".orangehrm-attachment")
        self._addButton = self._attachment.get_by_role("button", name="Add")
        self._fileButton = self._attachment.get_by_role("button", name="Browse")
        self._saveButton = self._attachment.get_by_role("button", name="Save")
        self._comment = page.get_by_placeholder("Add a comment")
        self.nationality = nationality
        self.maritalStatus = maritalStatus

    def add(self):
        if self.nationality:
            self._oxdlocator.first.click()
            self._selectFromDropDown(self.nationality).last.click()
        if self.maritalStatus:
            self._oxdlocator.nth(1).click()
            self._selectFromDropDown(self.maritalStatus).last.click()

    def uploadAttachment(self, file_path, comment=None):
        self._addButton.click()
        self._fileButton.click()
        """
        WITH ONLY PLAYWRIGHT
        #import time
        #time.sleep(10)
        #file_input = self.page.locator("input[type='file']") #Doesn't work 
        #file_input.set_input_files(file_path)#Doesn't work
        """
        if comment:
            self.__comment.fill(comment)
        self.saveButton.click()
