from pages.base.BasePage import BasePage


class League(BasePage):
    def __int__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _myLeagues = "My Leagues"

    def myLeagues(self):
        element = self.isDisplayed(self._myLeagues, "text")

    def selectALeague(self, myLeague):
        element = self.isDisplayed(myLeague, "text")
        assert element == True
        self.clickElement(myLeague, "text")
