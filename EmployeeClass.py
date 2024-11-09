from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        print("abstract function")


class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name)
        self.weekly_salary = weekly_salary
        

    def calculate_payroll(self):
        return self.weekly_salary

 
class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, emp_id, name, weekly_salary, commission):
        super().__init__(emp_id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return self.weekly_salary + self.commission 
        
        


 
salary_emp = SalaryEmployee(30, "kev", 20000)
hourly_emp = HourlyEmployee(40, "BIMA", 20, 40)
commission_emp = CommissionEmployee(50, "Tim", 1000,500)


print(f"{salary_emp.name} has  a Payroll of: ${salary_emp.calculate_payroll():.2f}")
print(f"{hourly_emp.name}  has a Payroll of: ${hourly_emp.calculate_payroll():.2f}")
print(f"{commission_emp.name} has a Payroll of: ${commission_emp.calculate_payroll():.2f}")