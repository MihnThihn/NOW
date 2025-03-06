import threading

class LoggerSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(LoggerSingleton, cls).__new__(cls)
                cls._instance.logger = None  # Placeholder cho Logger cụ thể
        return cls._instance

    def set_logger(self, logger):
        """Thiết lập loại Logger (Console, File, Database)."""
        if self.logger is None:
            self.logger = logger

    def log(self, message):
        """Ghi log bằng Logger đã được thiết lập."""
        if self.logger:
            self.logger.log(message)
        else:
            print("[ERROR] Logger chưa được thiết lập!")
