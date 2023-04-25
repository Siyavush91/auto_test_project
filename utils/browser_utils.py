from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver

# from .base_element import Element
from utils.logger import Logger

log = Logger('utils.browser_utils')


class BrowserUtils:
    """
    A class to provide interface for browser instance.

    Parameters
    ----------
    driver : WebDriver
        Instance of a selenium WebDriver.
    """
    def __init__(self, driver):
        self.__driver = driver
        self._actions = ActionChains(self.__driver, duration=500)

    @property
    def driver(self):
        """
        Get WebDriver instance.

        Returns
        -------
        WebDriver
        """
        return self.__driver