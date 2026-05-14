#check if a number if even or odd

def checkEvenOdd(x) : 

    if(x == 4444):
        print("Exiting...")
        return False
    
    if(x % 2 == 0):
        print("Number is even")
    else:
        print("Number is odd")

while(True):
    a = int(input("Enter a number : "))
    checkEvenOdd(a)
    

