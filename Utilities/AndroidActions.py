from logging import exception

from appium.webdriver.common.appiumby import AppiumBy

def android_scroll_element_to_accessibility_id(driver, element_id, direction, percent, accessibility_id):
    driver.execute_script('mobile: scrollGesture', {
        'elementId': element_id,
        'direction': direction,
        'percent': percent
    })
    while True:
        try:
            if driver.find_element(AppiumBy.ACCESSIBILITY_ID, accessibility_id):
                return
        except :
            driver.execute_script('mobile: scrollGesture', {
                'elementId': element_id,
                'direction': direction,
                'percent': percent
            })

def android_zoom_photo(driver, left, top, width, height, percent):
    driver.execute_script('mobile: pinchOpenGesture', {
        'left': 200,
        'top': 500,
        'width': 1000,
        'height': 1000,
        'percent': 0.5
    })