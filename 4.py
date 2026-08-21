# num_01 = int(input("Enter number: "))
# num_02 = int(input("Enter number: "))

# op = input("Enter operator (+, -, *, //): ")

# match op:
#     case "+":
#         print("num_01 + num_02 = ", num_01 + num_02)
#     case "-":
#         print("num_01 - num_02 = ", num_01 - num_02)
#     case "*":
#         print("num_01 * num_02 = ", num_01 * num_02)
#     case "/":
#         if num_02 != 0:
#             print("num_01 / num_02 = ", num_01 // num_02)
#         else:
#             print("can not divisible by 0")
#     case _:
#         print("Invalid operator")
        

# days = 5

# match days:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekdays")
#     case 6 | 7:
#         print("Weekend")


accBalance = 5000

print("-----Welcome to ATM----")
print("01. View Account balance")
print("02. Withdraw amount")
print("03. Deposit amount")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Account balalnce is: ", accBalance)
        
    case 2:
        withdrolAmount = int(input("Enter withdral amount: "))
        
        if withdrolAmount > accBalance:
            print("Insuficuent fund")
        else:
            accBalance = accBalance - withdrolAmount
            print("Amount withdrawl successfully")
            print("Remaning amount is: ", accBalance)
            
    case 3:
        depositeAmount = int(input("Enter deposit amount: "))
        
        accBalance = depositeAmount + accBalance
        print("Amount credited in your account successfully")
        print("Total account balance: ", accBalance)
    case _:
        print("Invaid choice")