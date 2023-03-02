from appium.webdriver.appium_service import AppiumService

service = AppiumService ( )


class AppiumServer :
    @staticmethod
    def start ( ) :

        print ( "starting the appium server on http://127.0.0.1:4723/wd/hub " )
        service.start ( args = [ '--base-path' , '/wd/hub' ] )
        print ( "Is Appium Server Running ?" + str ( service.is_running ) )
        print ( "Is Appium Server Listening ?" + str ( service.is_listening ) )

    @staticmethod
    def stop ( ) :
        print ( "Stopping the Appium Server" )
        service.stop ( )

