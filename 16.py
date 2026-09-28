from abc import ABC, abstractmethod

# class ATM(ABC):
#     @abstractmethod
#     def payment(self):
#         pass
        
#     def payment(self):
#         print("Payment is paid")
        
# obj = ATM()

# obj.payment()


# class Finance(ABC):
#     @abstractmethod
#     def payment(self, amount):
#         pass
    
#     def payment(self,amount):
#         print(f"Payment done by Credit card of amount {amount}")
        
# class UPI(Finance):
#     def payment(self, amount):
#         print(f"Payment done UPI of amount {amount}")
        
# obj = Finance()
# upiPayment = UPI()

# obj.payment(5000)
# upiPayment.payment(50)


class Employee(ABC):
    def __init__(self, salaryAmount):
        self.salaryAmount = salaryAmount
    
    @abstractmethod
    def salary(self, salaryAmount):
        pass
    
    def __del__(self):
        print("Salary credited to all Employers")
    
class EmployerA(Employee):
    def salary(self, salaryAmount):
        print(f"Salary paid to Employe A is {salaryAmount}")
        
class EmployerB(Employee):
    def salary(self, salaryAmount):
        print(f"Salary paid to Employe B is {salaryAmount}")
        
P1 = EmployerA(500)
P2 = EmployerB(5000)

P1.salary(500)
P2.salary(5000)