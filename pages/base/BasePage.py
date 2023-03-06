import time
import appium.webdriver.common.appiumby
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, \
    NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from utilities import log as cl

class BasePage:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorvalue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 60, poll_frequency=10, ignored_exceptions=[ElementNotVisibleException,
                                                                                     ElementNotSelectableException,
                                                                                     NoSuchElementException])
        if locatorType == "resource-id":
            element = wait.until(lambda x: x.find_elements(appium.webdriver.common.appiumby.AppiumBy.ID, locatorvalue))
            return element

        elif locatorType == "class":
            element = wait.until(
                lambda x: x.find_element(appium.webdriver.common.appiumby.AppiumBy.CLASS_NAME, locatorvalue))
            return element

        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element(appium.webdriver.common.appiumby.AppiumBy.ANDROID_UIAUTOMATOR,
                                                          'text("%s")' % locatorvalue))
            return element

    def getElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element found with LocatorType: " + locatorType + " with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Element not found with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        return element

    def clickElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.click()
            self.log.info(
                "Clicked on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)

    def sendText(self, text, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text  on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)

    def isDisplayed(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.is_displayed()

            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is displayed ")
            return True
        except:
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + " is not displayed")
            return False

    def screenShot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "reports/screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path : " + screenshotPath)
        except:
            self.log.info("Unable to save Screenshot to the Path : " + screenshotPath)
