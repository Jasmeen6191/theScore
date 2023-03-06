--------Run appium server, emulator setup and apk installation----------------------------
To Run appium, I used cmd with "appium" command
Launch Emulator Pixel 6 Pro, virtual device manager from Android sdk
apk file used can be found under asset folder
install apk using adb install ../PycharmProjects/theScore/asset/theScore_Apkpure.ap
Desired capabilities needs to update in pages/base/LauchApp file if in case different apk used
->to get Emulator uuid run 'adb devices' command
-----------------------------Test Scenario---------------------------------------------------
Open NCAA Football League,
Verify that league page opens correctly.
tap on sub-tab leaders
verify that you are at correct page and NCAA Football leaders are displayed correctly
# Please note I've verified only first two leaders in my test, in case you want to verify other leaders as well
 needs to implement scrolling behaviour and then add more leaders in "set variable"
 Verify that back navigation returns you to the previous page
-----------------------------------------------------------------------------------------------
-----------------------Run test----------------------------------------------------------------
Execute "VerifyLeagueAndItsLeaders.py"
-----------------------------------------------------------------------------------------------
----------------------Explain automation Framework--------------------------------------------
"asset" contains apk file used in this test

There are app "pages" where control elements properties and methods are written for the score app.
base contains launch app and other required classes to simply the framework
#Please note I only specified the controls that I used and try to make the pages app packge independent,
there's only one control LocatorType: resource-id with the locatorValue :com.fivemobile.thescore:id/big_leader_name
which is package dependent right now

steps acts and "reusable blocks".

reports in the form of log and screenshots are stored in corresponding folders,
please note unit-Html reporting or Allure reporting can be implement on top of this framework.

utilities contains logger class

test folder contain actual test file which is test data parametrize.
----------------------------------------------------------------------------------------------
------------Run Report------------------------------------------------------------------------
logReportnew.log inside report folder
screenshots are taken after launching the app, on home page, league and leaders view success
it can be found under screenshots folder
---------------------------------------------------------------------------------------------


