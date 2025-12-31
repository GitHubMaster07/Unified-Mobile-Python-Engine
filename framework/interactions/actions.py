from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

class TouchActions:
    """
    Класс для реализации сложных жестов (свайпы, зум, долгие нажатия).
    Соответствует принципу DRY: логика жестов инкапсулирована в одном месте.
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def swipe_percentage(self, start_x_pct: float, start_y_pct: float, end_x_pct: float, end_y_pct: float, duration: int = 600):
        """
        Универсальный свайп по процентам экрана. 
        KISS: Избавляет от необходимости вычислять пиксели под разные разрешения устройств.
        """
        
        size = self.driver.get_window_size()
        
        
        start_x = int(size['width'] * (start_x_pct / 100))
        start_y = int(size['height'] * (start_y_pct / 100))
        end_x = int(size['width'] * (end_x_pct / 100))
        end_y = int(size['height'] * (end_y_pct / 100))

        
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(duration / 1000) # Пауза для стабильности жеста
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def scroll_down(self):
        """Быстрый свайп вниз (из центра экрана вверх)."""
        self.swipe_percentage(50, 80, 50, 20)

    def scroll_up(self):
        """Быстрый свайп вверх (из центра экрана вниз)."""
        self.swipe_percentage(50, 20, 50, 80)