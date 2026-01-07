from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseScreen:
    """
    Base class for all Screen Objects in the framework.
    Provides common interactions and explicit wait logic.
    """

    def __init__(self, driver: WebDriver):
        """
        Initializes the base screen with the Appium driver.
        :param driver: Instance of the Appium WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10) # Default wait of 10 seconds

    def find_element(self, locator: tuple):
        """
        Finds an element on the screen using explicit waits.
        :param locator: Tuple containing (By.ID, "value") or similar
        :return: WebElement
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator: tuple):
        """
        Waits for an element to be clickable and performs a click.
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()