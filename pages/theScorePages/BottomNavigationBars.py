from pages.base.BasePage import BasePage


class BottomNavigationBars(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _news = "News"
    _score = "Score"
    _favorites = "Favorites"
    _bet = "Bet"
    _leagues = "Leagues"

    def BottomNavigationBarsIsPresent(self):
        self.isDisplayed(self._bet, "text")

    def ClickOnLeagues(self):
        self.clickElement(self._leagues, "text")
