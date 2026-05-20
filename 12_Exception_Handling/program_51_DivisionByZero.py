# handle division by zero

flag = True
def divide(num1, num2):
    
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Number cannot be divided by zero , try again")

userNum1 = int(input("Enter number to divide : "))
userNum2 = int(input("Enter number to divide by : "))

ans = divide(userNum1, userNum2)
if(flag == True):
    print("Answer : ",ans)
else:
    print("")

print("yesss.")