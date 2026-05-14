# remove duplicates

lis = []

def removeDuplicates(l):
    newset = set(l)
    newl = list(newset)
    print("Before removing duplicates : ",l)
    print("After removing duplicates : ",newl)

n = int(input("Enter number of elements : "))
for i in range(n):
    element = int(input("Enter number : "))
    lis.append(element)

removeDuplicates(lis)