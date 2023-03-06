from pages.theScorePages.BottomNavigationBars import BottomNavigationBars
from pages.theScorePages.Welcome import Welcome
from pages.base.BasePage import BasePage
from pages.base.InitialAppSetup import InitialAppSetup
from utilities.log import customLogger

logObject = customLogger()


class GetStartedWithoutLogin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def stepsForAppSetUp(self, FavLeague, setFavTeam):
        WelcomeObj = Welcome(self.driver)
        InitialAppSetupObj = InitialAppSetup(self.driver)
        basePageObj = BasePage(self.driver)
        BottomNavigationBarsObj = BottomNavigationBars(self.driver)
        WelcomeObj.verifyWelcomeButton()
        logObject.info("App Launched Successfully")
        WelcomeObj.clickOnGetStarted()
        InitialAppSetupObj.setFavLeagure(FavLeague)
        InitialAppSetupObj.clickOnContinueButton()
        InitialAppSetupObj.locationPermissions()
        InitialAppSetupObj.setFavTeam(setFavTeam)
        InitialAppSetupObj.clickOnContinueButton()
        InitialAppSetupObj.neverMissAGame()
        InitialAppSetupObj.notificationPermssion()
        InitialAppSetupObj.wantToDownloadLiveapp()
        BottomNavigationBarsObj.BottomNavigationBarsIsPresent()
        basePageObj.screenShot("HomePage")
