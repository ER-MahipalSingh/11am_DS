# class Demo:
#     def display(self):
#         self.name = "Python"
#         self.version = 3.16
#         print(f"{self.name} {self.version}")
        
# obj = Demo()
# obj.display()

# class Students:
#     def setData(self,name,age):
#         self.name = name
#         self.age = age
        
#     def getData(self):
#         print(f"Name is {self.name} and age is {self.age}")
        
# stu = Students()
# stu1 = Students()

# stu.setData("Jhon", 20)
# stu1.setData("David", 20)

# stu.getData()
# stu1.getData()


class Car:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        
    def Honda(self):
        print(f"{self.__name} and price {self.__price}")
    
    def __del__(self):
        print("Tahnks for visit")
        
honda = Car("City", 500)
honda.__name = "Maruti"
honda.Honda()