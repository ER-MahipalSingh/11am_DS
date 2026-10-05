import uuid
import math
import random
from functools import reduce

# id = uuid.uuid4()
# srtID = str(uuid.uuid4())
# print(type(srtID))
# print(srtID)

# res = math.pow(5, 1)
# res = math.factorial(5)
# res = math.sqrt(5)
# res = math.ceil(5.8)
# res = math.floor(5.8)
# res = math.fabs(-10)
# print(res)

# name = ["david","python","java"]
# res = random.choices(name)
# res = random.randint(2,20)
# res = random.randrange(10,100)
# print(res)

# num = [1,2,3]
# res = reduce(lambda a, b: a * b, num)

# def sum(a,b):
#     return a + 10

# res = reduce(sum, num)
# print(res)

# num = [10,50,20,80,11]
# res = filter(lambda a: a > 20, num)
# res = filter(lambda a, b:a if a > b else b, num)
# resList = list(res)
# print(list(res))
# print(res)

# num = [10,50,20,80,11]
# res = map(lambda a: a * 10, num)
# print(list(res))

num = [100,50,200,80,11]
# num.sort()
# print(num)

res = sorted(num)
print(res)
