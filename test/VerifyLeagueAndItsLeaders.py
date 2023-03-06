from pages.theScorePages.BottomNavigationBars import BottomNavigationBars
from pages.theScorePages.Leaders import Leaders
from pages.theScorePages.League import League
from pages.theScorePages.LeagueSubTabTopBars import LeagueSubTabTopBars
from pages.base.BasePage import BasePage
from pages.base.LauchApp import LaunchApp
from pages.steps.GetStartedWithoutLogin import GetStartedWithoutLogin
from utilities.log import customLogger

LaunchAppObj = LaunchApp()
logObject = customLogger()
driver = LaunchAppObj.theScore()
basePageObj = BasePage(driver)
GetStartedWithoutLoginObj = GetStartedWithoutLogin(driver)  #
BottomNavigationBarsObj = BottomNavigationBars(driver)
LeagueObj = League(driver)
LeagueSubTabTopBarsObj = LeagueSubTabTopBars(driver)
LeadersObj = Leaders(driver)

# if user is using the app as guest user (using get started link)the
# then here user is setting favleague and team  as part of initial setup for the app
GetStartedWithoutLoginObj.stepsForAppSetUp("NHL Hockey", "Toronto Maple Leafs")

BottomNavigationBarsObj.ClickOnLeagues()
LeagueObj.myLeagues()
basePageObj.screenShot("MyLeagues")

# Open NCAA Football league"
LeagueObj.selectALeague("NCAA Football")
# Verify that league page opens correctly.
LeagueObj.myLeagues()
# tap on sub-tab leaders
LeagueSubTabTopBarsObj.clickOnLeaders()
# Verify that you are at correct page and NCAA Football leaders are displayed correctly
LeadersObj.verifyLeaders(setVariable={"A. Reed", "C. Williams"})
basePageObj.screenShot("Leaders")
# Verify that back navigation returns you to the previous page
driver.back()
LeagueObj.myLeagues()


basePageObj.screenShot("BackToMyLeagues")
logObject.info("test completed successfully")
# TearDown
driver.quit()
