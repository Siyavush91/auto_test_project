from settings import Settings
from helpers import BasePage
from utils.logger import Logger

log = Logger('helpers.pages.login_page')


class LoginPage(BasePage):

    _login = '//*[@id="Email"]'
    _password = '//*[@id="Password"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = 'Login'
        self.url = Settings.AUTH_URL
