# data = {10,20.5,"python",10}
# user = {}
# tech = set()
# print(type(user))
# print(type(tech))
# print(type(data))

# data.add(50)
# data.update({100,"java"})
# data.remove(20.5)
# val = data.pop()
# print(val)
# data.clear()

# print(data)

# for i in data:
#     print(i)


data = {"tech":"python", "year":1991}

# print(type(data))
# data["year"] = 2001
# data["version"] = 3.15
# data.update({"author":"guido", "name":"monthy"})
# data.pop("tech")
# data.clear()
# del data
# print(data)

# for val in data.values():
#     print(val)
    
# for key in data.keys():
#     print(key)
    
for key,val in data.items():
    print(f"{key} = {val}")