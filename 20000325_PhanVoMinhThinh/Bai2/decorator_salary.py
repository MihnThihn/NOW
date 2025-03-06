from abc import ABC, abstractmethod

# Interface cho nhân viên
class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass

# Nhân viên cơ bản với lương cơ bản
class BaseEmployee(Employee):
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def get_salary(self):
        return self.base_salary

# Decorator cho phụ cấp
class SalaryDecorator(Employee):
    def __init__(self, employee):
        self.employee = employee

    def get_salary(self):
        return self.employee.get_salary()

# Các phụ cấp cụ thể
class ManagerAllowance(SalaryDecorator):
    def get_salary(self):
        return super().get_salary() + 5000000  # Phụ cấp trưởng phòng

class DirectorAllowance(SalaryDecorator):
    def get_salary(self):
        return super().get_salary() + 10000000  # Phụ cấp giám đốc

class AccountantAllowance(SalaryDecorator):
    def get_salary(self):
        return super().get_salary() + 3000000  # Phụ cấp kế toán

# Kiểm tra tính lương
if __name__ == "__main__":
    employee1 = BaseEmployee(15000000)  # Lương cơ bản 15 triệu
    manager = ManagerAllowance(employee1)
    director = DirectorAllowance(employee1)
    accountant = AccountantAllowance(employee1)

    print(f"Nhân viên lương: {employee1.get_salary()} VND")
    print(f"Trưởng phòng lương: {manager.get_salary()} VND")
    print(f"Giám đốc lương: {director.get_salary()} VND")
    print(f"Kế toán lương: {accountant.get_salary()} VND")
