import logging

from appium.webdriver.common.appiumby import AppiumBy

from Utilities.LogUtil import Logger
from Utilities import configReader

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator)).click()
        log.logger.info("Clicking on an Element "+ str(locator))

    def scrollToElement(self, locator):
        if str(locator).endswith("_ANDROID_UIAUTOMATOR"):
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(' + configReader.readConfig("locators", locator) + ')')
        else: pass

    def clickIndex(self, locator, index):
        if str(locator).endswith("_XPATH"):
            self.driver.find_elements_by_xpath(configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_elements_by_accessibility_id(configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_ID"):
            self.driver.find_elements_by_id(configReader.readConfig("locators", locator))[index].click()
        log.logger.info("Clicking on an Element "+ str(locator) + "with index : " + str(index))

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element_by_accessibility_id(configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configReader.readConfig("locators", locator)).send_keys(value)
        log.logger.info("Typing in an Element "+ str(locator)+ " entered the value as : "+ str(value))

    def getText(self, locator):
        if str(locator).endswith("_XPATH"):
            text = self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_ACCESSIBILITYID"):
            text = self.driver.find_element_by_accessibility_id(configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_ID"):
            text = self.driver.find_element_by_id(configReader.readConfig("locators", locator)).text
        #log.logger.info("Getting text from an element "+ str(locator))
        return text

    def isDisplay(self, locator):
        try:
            if str(locator).endswith("_XPATH"):
                self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator))
            elif str(locator).endswith("_ACCESSIBILITYID"):
                self.driver.find_element_by_accessibility_id(configReader.readConfig("locators", locator))
            elif str(locator).endswith("_ID"):
                self.driver.find_element_by_id(configReader.readConfig("locators", locator))
            return True
        except:
            return False

    def closeModal(self, x, y):
        self.driver.tap([(x, y)], 1)

    def flick(self, start_x, start_y, end_x, end_y):
        self.driver.flick(start_x, start_y, end_x, end_y)
