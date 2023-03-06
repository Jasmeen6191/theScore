from appium.webdriver.common.touch_action import TouchAction

from pages.base.BasePage import BasePage


class Welcome(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _welcome = "WELCOME"  # text
    _getStarted = "Get Started"  # text
    _logIn = "HAVE AN ACCOUNT? LOG IN"

    def verifyWelcomeButton(self):
        element = self.isDisplayed(self._welcome, "text")
        assert element == True

    def clickOnGetStarted(self):
        self.clickElement(self._getStarted, "text")

    def clickOnLogin(self, driver):
        element = self.clickElement(self._logIn, "text")
        actions = TouchAction(driver)
        actions.move_to(element, 958, 2469)
        actions.perform()
