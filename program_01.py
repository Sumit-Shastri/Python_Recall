# swap 2 variables without using third variable

a = 20
b = 10

def swapping(x, y):
    x,y = y, x

    print("a : ",x)
    print("b : ",y)

swapping(a,b)