from pages.base.BasePage import BasePage


class LeagueSubTabTopBars(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _scores = "SCORES"
    _news = "NEWS"
    _chat = "Chat"
    _standings = "STANDINGS"
    _leaders = "LEADERS"

    def clickOnLeaders(self):
        self.clickElement(self._leaders, "text")
