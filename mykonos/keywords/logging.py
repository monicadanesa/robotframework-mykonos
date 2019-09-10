from robot.api import logger

class LoggingKeywords(object):

    @property
    def _debug(self, message):
        logger.debug(message, True, True)

    def _info(self, message):
        logger.info(message, True, True)

    def _info_html(self, message):
        logger.info(message, True, False)

    def _warn(self, message):
        logger.warn(message, True, True)

    def _error(self, message):
        logger.error(message, True, True)

    def _log(self, message, level='INFO', also_console=True):
        level = level.upper()
        if (level == 'INFO'):
            self._info(message)
        elif (level == 'INFO_HTML'):
            self._info(message)
        elif (level == 'DEBUG'):
            self._debug(message)
        elif (level == 'WARN'):
            self._warn(message)
        elif (level == 'ERROR'):
            self._error(message)
