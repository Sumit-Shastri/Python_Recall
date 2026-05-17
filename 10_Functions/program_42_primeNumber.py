# fucntion to check prime number


def check_prime(n):

    check = False

    if(n == 1):
        return False
    
    for i in range(2, n):
        if(n % i == 0):
            check = True

    return check

num = int(input("Enter number : "))
ans = check_prime(num)
if(ans == True):
    print(num," is not prime")
else:
    print(num," is prime")
    