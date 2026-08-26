# i = 1
# while i <= 5:
#     i += 1
#     j = 1
#     while j <= 5:
#         print(j, end=" ")
#         j += 1
#     print()
    
print("---------")

for i in range(1,6):
    for j in range(1,6):
        print(j, end=" ")
    print()
    
print("---------")

for i in range(1,6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
    
print("---------")

for i in range(1,6):
    for j in range(5, i-1, -1):
        print(j, end=" ")
    print()
    
print("---------")

for i in range(1,6):
    for k in range(5, i, -1):
        print(" ", end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("---------")
    
for i in range(1,6):
    for k in range(5, i, -1):
        print(" ", end=" ")
    for j in range(1, i*2):
        print(j, end=" ")
    print()