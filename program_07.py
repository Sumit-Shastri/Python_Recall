# find largest of 3 numbers

def checkLargest(x, y, z):
    if(x > y and x > z):
        print(x, " is largest")
    elif(y > x and y > z):
        print(y, " is largest")
    else:
        print(z, " is largest.")



while(True):
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    num3 = int(input("Enter number 3 : "))
    checkLargest(num1, num2, num3)