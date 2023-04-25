from helpers.pages import LoginPage
from utils.browser_utils import BrowserUtils
from selenium.webdriver.remote.webdriver import WebDriver


class Application:
    def __init__(self, driver: WebDriver):
        self.browser = BrowserUtils(driver)
        self.login_page = LoginPage(driver)


    def run(self):
        """
        Open login page of the nopCommerce.

        Returns
        -------
        Application
        """
        self.browser.driver.get(self.login_page.url)
        return self

