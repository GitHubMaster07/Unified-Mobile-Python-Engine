import os
from appium import webdriver
from appium.options.common import AppiumOptions
from config.settings import settings # Assuming your Pydantic settings are here

class DriverFactory:
    """
    Service class responsible for initializing the Appium WebDriver 
    based on the environment configuration (Local vs. Cloud).
    """

    @staticmethod
    def create_driver():
        """
        Creates and returns a WebDriver instance.
        Currently configured for BrowserStack (Cloud) execution.
        :return: WebDriver instance
        :raises: ConnectionError if the driver fails to initialize
        """
        try:
            # Set BrowserStack capabilities from your Pydantic settings
            options = AppiumOptions()
            caps = {
                "deviceName": settings.DEVICE_NAME,
                "platformName": settings.PLATFORM_NAME,
                "platformVersion": settings.PLATFORM_VERSION,
                "app": settings.APP_URL,
                'bstack:options' : {
                    "userName": settings.BROWSERSTACK_USERNAME,
                    "accessKey": settings.BROWSERSTACK_ACCESS_KEY,
                    "projectName": "Unified Mobile Engine",
                    "buildName": "Alpha-Build-01",
                    "sessionName": "Smoke Test Execution"
                }
            }
            options.load_capabilities(caps)

            # Initialize the remote WebDriver
            url = f"http://hub.browserstack.com/wd/hub"
            return webdriver.Remote(command_executor=url, options=options)

        except Exception as e:
            # Senior move: Providing a clear error message for debugging
            raise ConnectionError(f"Failed to initialize Appium Driver: {str(e)}")