# Sum of first N numbers 

def SumOfN(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i

    return sum

num = int(input("Enter Number : "))
totalSum = SumOfN(num)
print(f"Sum of first {num} numbers is : {totalSum}")