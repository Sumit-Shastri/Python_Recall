class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    def sub(self, num1, num2):
        return num1 - num2
    def mul(self, num1, num2):
        return num1 * num2
    def div(self, num1, num2):
        return num1 / num2

calci = Calculator()


while(True):
    print("---  Menu  ---")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exit")

    choice = int(input("Enter choice : "))
    user_num1 = int(input("Enter 1st number : "))
    user_num2 = int(input("Enter 2nd number : "))

    match choice:
        case 1:
            print(calci.add(user_num1, user_num2))
        case 2:
            print(calci.sub(user_num1, user_num2))
        case 3:
            print(calci.mul(user_num1, user_num2))
        case 4:
            print(calci.div(user_num1, user_num2))
        case _:
            print("Unknown status")

