from logger_singleton import LoggerSingleton
from logger_factory import LoggerFactory

if __name__ == "__main__":
    # Tạo Logger bằng Factory
    logger = LoggerFactory.get_logger("file")

    # Thiết lập Logger trong Singleton
    log_manager = LoggerSingleton()
    log_manager.set_logger(logger)

    # Ghi log
    log_manager.log("Hệ thống khởi động thành công!")
    log_manager.log("Người dùng đăng nhập vào hệ thống.")

    # Kiểm tra Singleton hoạt động
    another_instance = LoggerSingleton()
    another_instance.log("Kiểm tra Singleton hoạt động!")  # Vẫn dùng FileLogger
