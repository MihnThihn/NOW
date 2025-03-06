from abc import ABC, abstractmethod
from logger_factory import ConsoleLogger, FileLogger, DatabaseLogger

# Abstract Factory
class AbstractLoggerFactory(ABC):
    @abstractmethod
    def create_logger(self):
        pass

# Concrete Factory cho ConsoleLogger
class ConsoleLoggerFactory(AbstractLoggerFactory):
    def create_logger(self):
        return ConsoleLogger()

# Concrete Factory cho FileLogger
class FileLoggerFactory(AbstractLoggerFactory):
    def create_logger(self):
        return FileLogger()

# Concrete Factory cho DatabaseLogger
class DatabaseLoggerFactory(AbstractLoggerFactory):
    def create_logger(self):
        return DatabaseLogger()
