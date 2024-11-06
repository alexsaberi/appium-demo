from sys import platform
from time import sleep

from Pages.BasePage import BasePage
from Utilities.AndroidActions import android_zoom_photo


class EditProfileScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def clickOnChangePicture(self):
        self.click("change_picture_XPATH")
        pass

    def clickOnLibraryPhoto(self):
        self.click("library_photo_XPATH")
        pass

    def chosePhoto(self):
        self.click("first_photo_XPATH")
        pass

    def zoomPhoto(self):
        if platform == 'ios':
            username = ""
        else:
            android_zoom_photo(self.driver, 200, 500, 1000, 1000, 0.5)
        pass

    def swipePhoto(self):
        if platform == 'ios':
            username = ""
        else:
            self.driver.swipe(558, 777, 558, 1270)
        pass

    def acceptPhoto(self):
        self.click("accept_photo_XPATH")
        pass

    def setName(self, value):
        self.type("name_field_XPATH", value)
        pass

    def getName(self):
        return self.getText("name_field_XPATH")

    def setBio(self, value):
        self.type("bio_field_XPATH", value)
        pass

    def getBio(self):
        return self.getText("bio_field_XPATH")

    def setLink(self, value):
        self.type("link_field_XPATH", value)
        pass

    def getLink(self):
        return self.getText("link_field_XPATH")

    def choseSex(self, value):
        self.click("sex_field_XPATH")
        if value == "Male":
            self.click("male_item_XPATH")
        elif value == "Female":
            self.click("female_item_XPATH")
        else:
            self.click("other_item_XPATH")
        self.closeModal(100, 200)
        pass

    def genderStatus(self, value):
        if value == "Male":
            return self.isDisplay("male_display_XPATH")
        elif value == "Female":
            return self.isDisplay("female_display_XPATH")
        else:
            return self.isDisplay("other_display_XPATH")

    def choseBirthday(self, value):
        self.click("birthday_field_XPATH")
        sleep(1.5)
        self.flick(start_x=735, start_y=1736, end_x=735, end_y=2206)
        sleep(0.5)
        self.flick(start_x=735, start_y=1736, end_x=735, end_y=2206)
        sleep(0.5)
        self.flick(start_x=735, start_y=1736, end_x=735, end_y=2206)
        sleep(0.5)
        self.flick(start_x=735, start_y=1736, end_x=735, end_y=2206)
        sleep(0.5)
        self.flick(start_x=390, start_y=1736, end_x=390, end_y=2206)
        self.flick(start_x=45, start_y=1736, end_x=45, end_y=2206)
        sleep(4)
        self.closeModal(100, 200)
        pass

    def clickOnSave(self):
        self.click("save_XPATH")
        pass

    def clickOnOk(self):
        self.click("ok_XPATH")
        pass

