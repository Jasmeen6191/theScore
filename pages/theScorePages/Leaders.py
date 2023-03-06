from pages.base.BasePage import BasePage
from utilities.log import customLogger


class Leaders(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _leader = "com.fivemobile.thescore:id/big_leader_name"

    def verifyLeaders(self, setVariable):
        element = self.waitForElement(self._leader, "resource-id")
        self.isDisplayed(self._leader, "resource-id")
        for x in element:
            if x.text in setVariable:
                logObject = customLogger()
                logObject.info("Leaders are present for the league " + x.text + "")
                assert x.text in setVariable, f"{x.text} not found in {setVariable}"
            else:
                logObject.error("Leaders are not present for the league " + x.text + "")
                assert x.text in setVariable, f"{x.text} not found in {setVariable} (expected to not be found)"
