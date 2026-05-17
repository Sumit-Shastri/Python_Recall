# find factorial


def Factorial(n):
    if n == 1:
        return 1
    
    return n * Factorial(n-1)

ans = Factorial(5)
print(ans)
