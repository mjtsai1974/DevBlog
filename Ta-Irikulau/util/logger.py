import os
import time
import logging

class Logger(object):
    def __init__(self, name = 'Uknav', logPath = 'log', console_Level = logging.ERROR, file_Level = logging.INFO):
        if not os.path.exists(logPath):
            os.makedirs(logPath)

        self._filename = time.strftime("%Y-%m-%d-%H-%M-%S")
        self._formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self._path = os.path.join(logPath, self._filename + '.log')
        self._f_handler = logging.FileHandler(self._path)
        self._f_handler.setLevel(file_Level)
        self._f_handler.setFormatter(self._formatter)

        self._c_handler = logging.StreamHandler()
        self._c_handler.setFormatter(self._formatter)
        self._c_handler.setLevel(console_Level)

        self._logger = logging.getLogger(name)  #In name of Taiwan black bear, Tumaz, or Uknav, the Taiwan panther
        self._logger.setLevel(file_Level)
        self._logger.addHandler(self._f_handler)
        self._logger.addHandler(self._c_handler)

    def Debug(self, message):
        self._logger.debug(message)

    def Info(self, message):
        self._logger.info(message)

    def Warning(self, message):
        self._logger.warning(message)

    def Error(self, message):
        self._logger.error(message)

    def Exception(self, message):
        self._logger.exception(message)

    def Critical(self,message):
        self._logger.critical(message)

"""
class PrinterLogger:
    new = lambda *args, **kwargs: 1
    info = print
    warning = print
    error = print


class Logger:
    __logger__ = PrinterLogger

    @staticmethod
    def new(logPath = 'log', filename=time.strftime("%Y-%m-%d-%H-%M-%S")):
        if Logger.__logger__ is PrinterLogger:
            if not os.path.exists(logPath):
                os.makedirs(logPath)

            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            path = os.path.join(logPath, filename + '.log')
            handler = logging.FileHandler(path)
            handler.setFormatter(formatter)

            logger = logging.getLogger('TUMAZ')  #In name of Taiwan black bear
            logger.setLevel(logging.DEBUG)
            logger.addHandler(handler)

            Logger.__logger__ = logger

    @staticmethod
    def info(msg):
        Logger.__logger__.info(msg)

    @staticmethod
    def warning(msg):
        Logger.__logger__.warning(msg)

    @staticmethod
    def error(msg):
        Logger.__logger__.error(msg)
"""