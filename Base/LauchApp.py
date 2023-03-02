from appium import webdriver

class Driver:

    @property
    def openApp(self):
        # AppiumServer.start ( )
        desired_caps={'platformName':'Android','automationName':'UiAutomator2','platformVersion':'11',
                      'deviceName':'Galaxy Nexus','app':'/Users/jasmeenkaur/Downloads/theScore_Apkpure.apk',
                      'appPackage':'com.fivemobile.thescore',
                      'appActivity':'com.fivemobile.thescore.ui.MainActivity'
                      #  'newCommandTimeout': 120, 'adbExecTimeout': 30000
                      }
        driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        return driver
    #
    # def tearDown(self):
    #     print("Closing the app")
    #     quitdriver= self.openApp().quit()
    #     return quitdriver

