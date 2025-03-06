from abc import ABC, abstractmethod

# Interface cho tất cả Logger
class ILogger(ABC):
    @abstractmethod
    def log(self, message):
        pass

# Logger ghi log ra console
class ConsoleLogger(ILogger):
    def log(self, message):
        print(f"[ConsoleLogger] {message}")

# Logger ghi log vào file
class FileLogger(ILogger):
    def __init__(self, filename="log.txt"):
        self.filename = filename

    def log(self, message):
        with open(self.filename, "a") as file:
            file.write(f"[FileLogger] {message}\n")
        print(f"[FileLogger] {message} (Đã ghi vào file)")

# Logger ghi log vào Database (giả lập)
class DatabaseLogger(ILogger):
    def log(self, message):
        print(f"[DatabaseLogger] Lưu log vào database: {message}")

# Factory Method để tạo Logger phù hợp
class LoggerFactory:
    @staticmethod
    def get_logger(logger_type):
        if logger_type == "console":
            return ConsoleLogger()
        elif logger_type == "file":
            return FileLogger()
        elif logger_type == "database":
            return DatabaseLogger()
        else:
            raise ValueError("Unknown logger type")
