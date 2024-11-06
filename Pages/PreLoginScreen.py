from Pages.BasePage import BasePage

class PreLoginScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def gotoLoginScreen(self):
        self.click("login_using_user_pass_XPATH")
        pass