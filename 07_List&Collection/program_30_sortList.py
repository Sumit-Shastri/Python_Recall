# Sort List , without using sort()

def Sorting(l):

    dummyList = l
    sorterdList = []

    for i in range(len(l)):

        a = min(dummyList)
        sorterdList.append(a)
        dummyList.remove(a)
    
    print("sorted List : ",sorterdList)

numbers = [34,578,233,68,987,123,35]
print("list : ",numbers)
Sorting(numbers)