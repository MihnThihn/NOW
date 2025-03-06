from abc import ABC, abstractmethod

# Interface cho các phương thức thanh toán
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Các phương thức thanh toán cụ thể
class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Thanh toán {amount} bằng tiền mặt.")

class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Chuyển khoản ngân hàng {amount} VND.")

class MomoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Thanh toán {amount} qua Momo.")

class VNPayPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Thanh toán {amount} qua VNPay.")

# Context sử dụng Strategy
class Order:
    def __init__(self, amount, payment_method: PaymentStrategy):
        self.amount = amount
        self.payment_method = payment_method

    def process_payment(self):
        self.payment_method.pay(self.amount)

# Test các phương thức thanh toán
if __name__ == "__main__":
    order1 = Order(500000, CashPayment())
    order2 = Order(750000, MomoPayment())
    order3 = Order(1200000, VNPayPayment())

    order1.process_payment()
    order2.process_payment()
    order3.process_payment()
