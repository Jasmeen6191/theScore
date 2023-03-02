from Base.LauchApp import Driver
from Utilities import log as debuglog

driver = Driver()
log = debuglog.customLogger()

driver.openApp
log.info("App Launched Successfully")