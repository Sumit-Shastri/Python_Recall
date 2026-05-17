# find common elements in 2 lists

def FindCommon(l1, l2):

    common = []

    for i in l1:
        for j in l2:
            if(i == j):
                if(i not in common):
                    common.append(i)
    
    print("common elements : ", common)

userList1 = [2, 5, 6, 9, 10, 23, 45]
userList2 = [5, 7, 3 ,1, 9, 23, 46]

FindCommon(userList1, userList2)
