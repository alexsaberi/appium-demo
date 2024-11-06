from Pages.BasePage import BasePage

class LoginScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def setUsername(self, value):
        self.type("username_field_XPATH", value)
        pass

    def setPassword(self, value):
        self.type("password_field_XPATH", value)
        pass

    def clickOnLogin(self):
        self.click("login_XPATH")
        pass

