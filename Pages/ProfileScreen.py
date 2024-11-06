from Pages.BasePage import BasePage

class ProfileScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def gotoSettings(self):
        self.click("setting_gear_XPATH")
        pass

    def gotoProfileMenu(self):
        self.click("profile_menu_XPATH")
        pass