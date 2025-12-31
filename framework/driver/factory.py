from appium import webdriver
from appium.options.android import UiAutomator2Options

class DriverFactory:
    @staticmethod
    def get_driver(settings):
        options = UiAutomator2Options()
        
        
        bstack_options = {
            "userName": settings.user_name,
            "accessKey": settings.access_key,
            "deviceName": settings.device_name,
            "osVersion": "14.0",
            "projectName": "Python Appium Project",
            "buildName": "browserstack-build-1",
            "sessionName": "Cloud Test Session"
        }
        
        options.set_capability('bstack:options', bstack_options)
        options.set_capability('app', settings.app or "bs://sample.app")
        
        
        url = "https://hub-cloud.browserstack.com/wd/hub"
        
        print(f"\n[INFO] Connecting to BrowserStack: {url}")
        return webdriver.Remote(command_executor=url, options=options)