# factorial of a number

def Factorial(n):
    sum = 1

    for i in range(1,n+1):
        sum = sum * i
    
    return sum

num = int(input("Enter number : "))
fact = Factorial(num)
print(fact)

