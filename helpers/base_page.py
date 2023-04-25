import datetime
from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver

from settings import TIMEOUTS
from utils.logger import Logger

log = Logger('helpers/base_page.py')


def timeout(seconds, message, polling_interval=1):
    def _check(func):
        def wrap(*args, **kwargs):
            start = datetime.datetime.now()
            timeout_sec = datetime.timedelta(seconds=seconds)
            while datetime.datetime.now() - start < timeout_sec:
                result = func(*args, **kwargs)
                if result:
                    return result
                sleep(polling_interval)
            raise AssertionError(message)

        return wrap

    return _check


class BasePage:
    """
    Represent a page of the Cloud Portal.

    The class introduces the basic logic for working with a page instance.

    Parameters
    ----------
    driver : WebDriver
    """
    page_name: str

    def __init__(self, driver):
        self.__driver = driver

    @property
    def driver(self):
        return self.__driver

    @staticmethod
    def enter_value(input_field, value):
        """
        Send a specified value to the input field.

        Parameters
        ----------
        input_field : src.selenium_wrappers.base_element.Input
            Input field element.
        value : str
            Value to be sent to the input.
        """
        input_field.clear()
        input_field.set_value(value)

    @timeout(seconds=TIMEOUTS.page_load, message=f'Page was not loaded in {TIMEOUTS.page_load} seconds')
    def is_loaded(self):
        """
        Check if the page is loaded.

        The method uses JS ``document.readyState`` property to check the loading state of a page.

        Returns
        -------
        bool
            True if the page was loaded, False otherwise.
        """
        log.info_console(f"Checking if {self} is loaded")
        return self.driver.execute_script("return document.readyState == 'complete'")  # improvement: return obj, er_msg

    def __str__(self):
        return f"{self.page_name.upper()} page"
