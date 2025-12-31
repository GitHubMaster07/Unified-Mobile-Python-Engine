
from framework.interactions.actions import TouchActions


class BaseScreen:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        
        self.actions = TouchActions(self.driver)