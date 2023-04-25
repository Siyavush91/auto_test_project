from allure import step
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from utils.logger import Logger

log = Logger('src.selenium_wrappers.driver_manager')


class DriverManager:
    """
    A class to define which browser to use in tests.

    Provides browser instance for Application class. Currently, only Chrome browser is supported.

    Parameters
    ----------
    name : str
    moon_host : str, optional
    moon_port : str, optional
    session_timeout : str, optional
    width : int, optional
    height : int, optional
    enable_video : bool, optional
    local_run : bool, default False
        If set to True then instance of the browser will be started locally.
    """
    @step('Start browser "{name}"')
    def __init__(self,
                 name,
                 moon_host=None,
                 moon_port=None,
                 session_timeout=None,
                 width=None,
                 height=None,
                 enable_video=None,
                 local_run: bool = True):
        self.type = name
        self.driver = None
        self.browser = None
        log.info_console(f"Open '{self.type}' browser...")
        options = webdriver.ChromeOptions()
        if local_run:
            options.add_argument('--start-maximized')
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            self.browser = driver
        elif 'chrome' in name:
            browser_name = str(name).split('_')[0]
            browser_version = str(name).split('_')[-1]
            capabilities = {
                "browserName": browser_name,
                "browserVersion": browser_version,
                "moon:options": {
                    "enableVideo": enable_video,
                    "sessionTimeout": session_timeout,
                    "screenResolution": f"{width}x{height}x24"
                }
            }
            for capability, value in capabilities.items():
                options.set_capability(capability, value)
            driver = webdriver.Remote(command_executor=f"http://{moon_host}:{moon_port}/wd/hub", options=options)
            driver.set_window_size(width, height)
            self.browser = driver
        else:
            raise NotImplementedError(f"Browser '{name}' is not supported yet")
        log.info_console(f"Browser '{self.type}' has been opened")

    def open(self):
        """
        Get a WebDriver instance.

        Returns
        -------
        WebDriver
        """
        return self.browser

    @step('Close browser')
    def quit(self):
        """
        Close current browser instance.

        Returns
        -------
        None
        """
        log.info_console(f"Close '{self.type}' browser...")
        self.browser.quit()
        log.info_console(f"Browser '{self.type}' has been closed")
