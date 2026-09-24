class GrandParent:
    def child(self):
        print("Garnd Parent class")
        
class Parent(GrandParent):
    def child(self):
        super().child()
        print("Parent class")
        
obj = Parent()

obj.child()

print(issubclass(Parent, GrandParent))
print(issubclass(GrandParent, Parent))


# class Calu:
#     def sum(self, a, b, c=0):
#         return a + b + c
    
# add = Calu()

# res = add.sum(10,20,30)
# res1 = add.sum(50,1)
# res2 = add.sum(10,200,30)
# print(res)
# print(res1)
# print(res2)

# class DisplayTotal:
#     def cal(self, *num):
#         total = 0
#         for i in num:
#             total += i
#         print(total)
        
# o1 = DisplayTotal()

# o1.cal(1,2,3)
# o1.cal(1,2,3,5)
# o1.cal(1,2,3,10,20)
# o1.cal(1,2,3,10,20,30)

