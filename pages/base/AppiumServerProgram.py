from appium.webdriver.appium_service import AppiumService

from utilities import log as cl

service = AppiumService()
log = cl.customLogger()


class AppiumServerProgram:
    @staticmethod
    def startServer():
        log.info("starting the appium server on http://127.0.0.1:4723/wd/hub")
        service.start(args=['--base-path', '/wd/hub'])
        service.start()
        log.info("Appium Server Running =" + str(service.is_running))
        log.info("Appium Server Listening =" + str(service.is_listening))

    @staticmethod
    def stop():
        print("Stopping the Appium Server")
        service.stop()
