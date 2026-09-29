class editUserDetails:
    def __init__(self,page):
        self.page=page
    def myInfo(self):
        self.page.get_by_text("My Info").click()
    
    def editNationality(self,Nation='Indian'):
        self.page.locator(".oxd-select-text-input").first.click()
        self.page.get_by_text(Nation).last.click()
    
    def editMaritalStatus(self,input='Single'):
        self.page.locator(".oxd-select-text-input").nth(1).click()
        self.page.get_by_text(input).last.click()

    def uploadAttachment(self, file_path=r"C:\Users\Keyur\Desktop\SomeDoc.txt", comment=None):
        self.page.locator(".orangehrm-attachment").get_by_role("button", name="Add").click()
        self.page.locator(".oxd-file-button").click()
        file_input = self.page.locator("input[type='file']") #Doesn't work 
        file_input.set_input_files(file_path)#Doesn't work
        if comment:
            self.page.locator(".orangehrm-attachment textarea").fill(comment)
        self.page.locator(".orangehrm-attachment").get_by_role("button", name="Save").click()
