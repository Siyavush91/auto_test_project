import os
from dataclasses import dataclass

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


@dataclass
class BrowserSettings:
    name: str
    # moon_host: str
    moon_port: str
    width: int
    height: int
    enable_video: bool
    session_timeout: str


@dataclass
class TimeoutSettings:
    page_load: int
    element_wait_default: int
    element_wait_long: int


class Settings:
    BASE_URL = "https://admin-demo.nopcommerce.com/"
    CLOUD_PORTAL_URL = f"{BASE_URL}/admin/"
    AUTH_URL = f"{BASE_URL}/login?ReturnUrl=%2Fadmin%2F"
    USER_LOGIN: str = 'admin@yourstore.com'
    USER_PASSWORD: str = 'admin'
    # LOCAL_DEBUG: bool = os.getenv('LOCAL_DEBUG', 'False') == 'True'  # https://stackoverflow.com/questions/63116419/evaluate-boolean-environment-variable-in-python
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')

    # Remote browser defaults section
    APP_BROWSER: str = os.getenv('APP_BROWSER', 'Chrome')
    # MOON_HOST: str = f"moon-{JenkinsNamespace[ENVIRONMENT]}"
    MOON_PORT: str = '4444'
    SESSION_TIMEOUT: str = os.getenv('SESSION_TIMEOUT', '15m')
    BROWSER_WIDTH = 1920
    BROWSER_HEIGHT = 1080
    BROWSER_ENABLE_VIDEO = False

    # Timeouts section
    PAGE_LOAD_TIMEOUT = 15
    ELEMENT_DEFAULT_TIMEOUT = 5
    ELEMENT_LONG_TIMEOUT = 60


BROWSER = BrowserSettings(name=Settings.APP_BROWSER,
                          # moon_host=Settings.MOON_HOST,
                          moon_port=Settings.MOON_PORT,
                          width=Settings.BROWSER_WIDTH,
                          height=Settings.BROWSER_HEIGHT,
                          enable_video=Settings.BROWSER_ENABLE_VIDEO,
                          session_timeout=Settings.SESSION_TIMEOUT)

TIMEOUTS = TimeoutSettings(page_load=Settings.PAGE_LOAD_TIMEOUT,
                           element_wait_default=Settings.ELEMENT_DEFAULT_TIMEOUT,
                           element_wait_long=Settings.ELEMENT_LONG_TIMEOUT)
