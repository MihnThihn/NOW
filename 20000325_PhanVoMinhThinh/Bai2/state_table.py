from abc import ABC, abstractmethod

# Interface cho các trạng thái của bàn ăn
class TableState(ABC):
    @abstractmethod
    def handle(self, table):
        pass

# Các trạng thái cụ thể
class FreeState(TableState):
    def handle(self, table):
        print("Bàn đang trống (Màu Xanh).")
        table.set_state(OrderState())

class OrderState(TableState):
    def handle(self, table):
        print("Bàn đã đặt hàng (Màu Cam).")
        table.set_state(DoneState())

class DoneState(TableState):
    def handle(self, table):
        print("Bàn đã thanh toán (Màu Vàng).")
        table.set_state(FreeState())

class FixingState(TableState):
    def handle(self, table):
        print("Bàn đang sửa chữa (Màu Đỏ).")
        table.set_state(DoneState())

# Context chứa trạng thái
class Table:
    def __init__(self):
        self.state = FreeState()  # Bàn bắt đầu ở trạng thái Free

    def set_state(self, state):
        self.state = state

    def handle_request(self):
        self.state.handle(self)

# Kiểm thử quá trình đổi trạng thái
if __name__ == "__main__":
    table = Table()

    table.handle_request()  # Free -> Order
    table.handle_request()  # Order -> Done
    table.handle_request()  # Done -> Free
    table.set_state(FixingState())  # Chuyển sang trạng thái Fixing
    table.handle_request()  # Fixing -> Done
    table.handle_request()  # Done -> Free
