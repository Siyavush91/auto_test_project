from allure import step

from helpers.application import Application
from helpers.pages import LoginPage
from utils.logger import Logger

log = Logger('tests.login')

class TestLoginPage:
    def test_user_can_login_with_valid_credentials(self, nopcommerce):
        with step('Open Login page of Cloud Portal'):
            self.open_login_page(nopcommerce)

    @staticmethod
    def open_login_page(app: Application) -> LoginPage:
        log.info_console('--- Open Login page ---')
        lp = app.login_page
        lp.is_loaded()
        log.info_console(f"--- {lp} has been opened successfully ---")
        return lp
