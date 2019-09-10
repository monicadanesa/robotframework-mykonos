from robot.api import logger

class LoggingKeywords(object):

    @property
    def debug(self, message):
        logger.debug(message, True, True)

    def info(self, message):
        logger.info(message, True, True)

    def info_html(self, message):
        logger.info(message, True, False)

    def warn(self, message):
        logger.warn(message, True, True)

    def error(self, message):
        logger.error(message, True, True)

    def log(self, message, level='INFO', also_console=True):
        level = level.upper()
        if (level == 'INFO'):
            self.info(message)
        elif (level == 'INFO_HTML'):
            self.info(message)
        elif (level == 'DEBUG'):
            self.debug(message)
        elif (level == 'WARN'):
            self.warn(message)
        elif (level == 'ERROR'):
            self.error(message)
