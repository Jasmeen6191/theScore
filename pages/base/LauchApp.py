from appium import webdriver

class LaunchApp:

    def theScore(self):
        desired_caps = {'platformName': 'Android',
                        # 'automationName': 'UiAutomator2', 'platformVersion': '13',
                        'deviceName': 'Pixel 6 Pro',
                        'resetOnSessionStartOnly': 'true',
                        'appPackage': 'com.fivemobile.thescore',
                        'appActivity': 'com.fivemobile.thescore.ui.MainActivity',
                        "appium:udid": 'emulator-5554'
                        #  'newCommandTimeout': 120, 'adbExecTimeout': 30000
                        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver
