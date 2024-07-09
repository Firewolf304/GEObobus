import logging
import json

class CustomFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%'):
        super().__init__(fmt, datefmt, style)
        # need full config
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    FORMATS = {
        logging.DEBUG: grey,
        logging.INFO: grey,
        logging.WARNING: yellow,
        logging.ERROR: red,
        logging.CRITICAL: bold_red
    }



    def format(self, record):
        #log_fmt = self.FORMATS.get(record.levelno)
        #formatter = logging.Formatter(log_fmt)
        #return formatter.format(record)
        log_fmt = self.FORMATS.get(record.levelno)
        record.msg = f"{log_fmt}{record.msg}{self.reset}"
        return super().format(record)


# by chatgpt
class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[94m',  # Синий
        'INFO': '\033[92m',   # Зеленый
        'WARNING': '\033[93m',# Желтый
        'ERROR': '\033[91m',  # Красный
        'CRITICAL': '\033[95m' # Фиолетовый
    }
    RESET = '\033[0m'  # Сброс цвета

    def __init__(self, fmt=None, datefmt=None, style='%'):
        super().__init__(fmt, datefmt, style)

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, self.RESET)
        record.msg = f"{log_color}{record.msg}{self.RESET}"
        return super().format(record)