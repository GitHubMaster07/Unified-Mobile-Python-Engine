import pytest
from framework.driver.factory import DriverFactory
from config.settings import ConfigLoader

@pytest.fixture(scope="session")
def driver():
    settings = ConfigLoader.load_config()
    driver = DriverFactory.get_driver(settings) # Передаем объект настроек
    yield driver
    driver.quit()