# file = open("text.txt", "w")
# file.write("Hello Student's")
# file.write("\nWelcome to class")

# file = open("text.txt", "r")
# data = file.read()
# data = file.read(10)
# print(file)
# print(data)

# file = open("text.txt", "a")
# file.write("\nML Engineer")


# file.close()

# with open("text.txt", "r") as file:
#     data = file.read()
#     print(data)


# a = 10
# b = 2
# e = 0
# c = a / e
# print(c)

# try:
#     a = 10
#     e = 0
#     c = a / e
#     print(c)
# except ZeroDivisionError:
#     print("Can not devided by 0")

# try:
#     age = int(input("Enter you age: "))
#     if age >= 18:
#         print("You can do vote")
#     else:
#         raise ValueError ("Your not eligible")
# except ValueError as error:
#     print(error)
# finally:
#     print("Thanks for useing services")

balance = 5000
try:
    amount = int(input("Enter withdraw amount:"))
    if amount > balance:
        raise ValueError ("Insuficuent balance")
    
    balance -= amount
except ValueError as error:
    print(error)
else:
    print("Withdraw amount is: ",amount)
    print("Remaning balance is: ",balance)
finally:
    print("Thanks for visit")