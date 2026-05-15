# Find second largest number

def FindSecondLargest(l):
    maximum = max(l)
    l.remove(maximum)

    maximum = max(l)
    return maximum

list = [25,67,89,234,678,345,467]
maxOfList = FindSecondLargest(list)
print("Second largest : ", maxOfList)
