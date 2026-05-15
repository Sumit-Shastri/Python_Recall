# merge 2 lists

def mergeList(l1, l2):
    mergedList = l1 + l2
    print(mergeList)

list1 = [14,6,7,99,9]
list2 = [45,67,98,12,34]


print("List 1 : ",list1)
print("list 2 : ",list2)
print("list 3 (merged) : ",mergeList(list1, list2))

print(list1 + list2)