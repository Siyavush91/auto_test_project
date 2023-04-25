import pytest

from dataclasses import asdict

from helpers.driver_manager import DriverManager
from helpers.application import Application
from settings import Settings, BROWSER


@pytest.fixture(scope='function')
def browser():
    browser_manager = DriverManager(**asdict(BROWSER))
    yield browser_manager.open()
    browser_manager.quit()


@pytest.fixture
def nopcommerce(browser):
    app = Application(browser)
    yield app.run()


