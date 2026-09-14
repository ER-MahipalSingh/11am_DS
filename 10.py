# data = [
#     [10,20,30],
#     {"Python", "Java"},
#     (1.5,5.6,8.6), 
# ]

# print(data)
# print(type(data))

# for row in data:
#     for col in row:
#         print(col, end=" ")
#     print()

# data = [
#     {"tech":"python", "veriosn":3.15},
#     {"tech":"java", "veriosn":13},
#     {"tech":"javascript", "veriosn":19},
# ]

# print(data)
# print(type(data))

# for row in data:
#     for key, val in row.items():
#         print(key,val)
#     print()

data = {
    1:{"name":"Jhon", "age":20},
    2:{"name":"Jhon", "age":20},
    3:{"name":"Jhon", "age":20},
}

# print(data)
# print(type(data))

for id, row in data.items():
    print(id)
    for key, val in row.items():
        print(key, val)
    print()
    
    
    
    
