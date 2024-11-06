from Pages.BasePage import BasePage

class HomeScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def gotoProfile(self):
        self.click("btnShProfile_XPATH")
        pass

    def gotoWorkout(self):
        pass
