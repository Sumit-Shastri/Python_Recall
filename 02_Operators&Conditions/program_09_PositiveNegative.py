def checkPNZ(num):
    if(num > 0):
        print(num," is positive.")
    elif(num < 0):
        print(num," is negative.")
    else:
        print(num," is zero")

while(True):
    user_num = int(input("Enter a number : "))
    checkPNZ(user_num)