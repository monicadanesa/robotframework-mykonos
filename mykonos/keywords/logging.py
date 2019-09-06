from robot.api import logger
from mykonos.core import Core

class LoggingKeywords(Core):
    LOG_LEVEL_DEBUG = ['DEBUG']
    LOG_LEVEL_INFO = ['DEBUG', 'INFO']
    LOG_LEVEL_WARN = ['DEBUG', 'INFO', 'WARN']
    LOG_LEVEL_ERROR = ['DEBUG', 'INFO', 'WARN', 'ERROR']

    @property
    def _debug(self, message):
        if self._log_level in self.LOG_LEVEL_DEBUG:
            logger.debug(message)

    def _info(self, message):
        if self._log_level in self.LOG_LEVEL_INFO:
            logger.info(message)

    def _warn(self, message):
        if self._log_level in self.LOG_LEVEL_WARN:
            logger.info(message)

    def _err(self, message):
        if self._log_level in self.LOG_LEVEL_ERR:
            logger.err(message)

    def _log(self, message, level='INFO'):
        level = level.upper()
        if (level == 'INFO'):
            self._info(message)
        elif (level == 'DEBUG'):
            self._debug(message)
        elif (level == 'WARN'):
            self._warn(message)
        elif (level == 'ERROR'):
            self._err(message)
