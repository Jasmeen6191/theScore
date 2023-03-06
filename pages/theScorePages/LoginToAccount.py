from pages.base import BasePage


class LoginToAccount(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _email = "Email"
    _password = "Password"
    _logIn = "Log In"

    def login(self, emailId, password):
        self.isDisplayed(self._logIn, "text")
        self.sendText(self._email, emailId, "text")
        self.sendText(self._password, password, "text")
        self.clickElement(self._logIn, "text")
