import time
from pages.base.BasePage import BasePage

class InitialAppSetup(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _continueButton = "Continue"
    _locationAccessLater = "Maybe Later"
    _neverMissAGame = "Done"
    _notificationDoNotAllow = "Don’t allow"
    _downloadLiveAppAlert = "android.widget.ImageView"

    def clickOnContinueButton(self):
        self.clickElement(self._continueButton, "text")  # Continue Button

    def neverMissAGame(self):
        self.clickElement(self._neverMissAGame, "text")  # Done Button

    def locationPermissions(self):
        elementLocationAccessLater = self.isDisplayed(self._locationAccessLater,
                                                      "text")  # Maybe Later for location access
        assert elementLocationAccessLater == True
        self.clickElement(self._locationAccessLater, "text")

    def notificationPermssion(self):
        time.sleep(5)
        elementNotificationDoNotAllow = self.isDisplayed(self._notificationDoNotAllow,
                                                         "text")  # Don't Allow notifications for now
        assert elementNotificationDoNotAllow == True
        self.clickElement(self._notificationDoNotAllow, "text")

    def wantToDownloadLiveapp(self):
        time.sleep(5)
        Element_downloadLiveAppAlert = self.isDisplayed(self._downloadLiveAppAlert, "class")
        assert Element_downloadLiveAppAlert == True
        self.clickElement(self._downloadLiveAppAlert, "class")

    def setFavLeagure(self, myFavLeague):
        element = self.isDisplayed(myFavLeague, "text")
        assert element == True  # TestParametrizedwithFavLeague
        self.clickElement(myFavLeague, "text")

    def setFavTeam(self, myFavTeam):
        element = self.isDisplayed(myFavTeam, "text")
        assert element == True  # TestParametrizedwithFavTeam
        self.clickElement(myFavTeam, "text")
