from appium import webdriver
from selenium.common.exceptions import ElementNotVisibleException , ElementNotSelectableException , \
    NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy


class Wait:
    def __int__(self, driver):
        self.driver= driver
    def waitForElement(self, locatorvalue, locatorType):
        locatorType =locatorType.lower()
        element =None
        wait = WebDriverWait(self.driver,60,poll_frequency=10,ignored_exceptions=[ElementNotVisibleException,
                                                                           ElementNotSelectableException,
                                                                                NoSuchElementException])
        if locatorType =="id":
            element =wait.until(lambda x: x.find_element(AppiumBy.ID,locatorvalue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME,locatorvalue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().description("%s")' % (locatorvalue)))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(%d)" % int(locatorvalue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("%s")' % locatorvalue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH,'%s' % (locatorvalue)))
            return element
        else:
            self.log.info("Locator value " + locatorvalue + "not found")

        return element

