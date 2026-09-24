# class Parent:
#     def show(self):
#         print("Class Parent")
        
# class Child(Parent):
#     def display(self):
#         print("Child class")
        
# c = Child()

# c.display()
# c.show()

# class FamaiyTree:
#     def tree(self):
#         print("FamaiyTree")
        
# class GrandParents(FamaiyTree):
#     def garnd(self):
#         print("Grand")
        
# class Parents(GrandParents):
#     def parents(self):
#         print("Parents")
        
# tree = Parents()

# tree.parents()
# tree.garnd()
# tree.tree()

# class Car:
#     def engine(self):
#         print("Car Engin type")
        
# class Honda(Car):
#     def petrol(self):
#         print("petrol")
        
# class Maruti(Car):
#     def diseal(self):
#         print("Disel")
        
# marutiObj = Maruti()
# hondaObj = Honda()

# marutiObj.diseal()
# marutiObj.engine()

# hondaObj.petrol()
# hondaObj.engine()

class A:
    def aFun(self):
        print("A Class")
        
class B(A):
    def bFun(self):
        print("B Class")
        
class C:
    def CFun(self):
        print("C Class")

class D(A, B):
    def dFun(self):
        print("D Class")
        
objD = D()
objD.dFun()
objD.bFun()