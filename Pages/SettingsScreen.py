from Pages.BasePage import BasePage

class SettingsScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def gotoProfileMenu(self):
        self.click("profile_menu_XPATH")
        pass

    def clickOnLogout(self):
        self.scrollToElement("logout_ANDROID_UIAUTOMATOR")
        self.click("logout_XPATH")
        pass
