import logging
from allure import attach, attachment_type

from settings import Settings


class Logger:

    def __init__(self, logger_name, level=Settings.LOG_LEVEL):
        self.log = logging.getLogger(logger_name)
        self.log.setLevel(level)

    def info_console(self, message: str):
        self.log.info(message)

    def debug_console(self, message: str):
        self.log.debug(message)

    def warning_console(self, message: str):
        self.log.warning(message)

    def error_console(self, message: str):
        self.log.error(message)

    @staticmethod
    def _attach_to_report(*args):
        for item in args:
            if isinstance(item, bytes):
                attach(body=item, name='screenshot', attachment_type=attachment_type.PNG)
            if isinstance(item, str):
                if is_html_code(item):
                    attach(body=item, name='html code', attachment_type=attachment_type.HTML)
                else:
                    attach(body=item, name='log', attachment_type=attachment_type.TEXT)

    def error_console_and_report(self, message: str, console_log=None, image=None, html_code=None):
        self.error_console(message)
        self._attach_to_report(console_log, image, html_code)

    def info_console_and_report(self, message: str, console_log=None, image=None, html_code=None):
        self.info_console(message)
        self._attach_to_report(console_log, image, html_code)

    def warning_console_and_report(self, message: str, console_log=None, image=None, html_code=None):
        self.warning_console(message)
        self._attach_to_report(console_log, image, html_code)
