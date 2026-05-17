# Rotate List

def RightRotateList(l, steps):

    rotated_list = l[-steps:] + l[:-steps]
    print("original list : ",l)
    print("Right rotated list : ", rotated_list)

def LeftRotateList(l, steps):

    rotated_list = l[steps:] + l[:steps]
    print("original list : ",l)
    print("Right rotated list : ", rotated_list)

user_list = []

n = int(input("Enter number of elements : "))
i = 0
while(i < n):
    ele = int(input("Number : "))
    user_list.append(ele)
    i = i+1

choice = int(input("1.Right rotate.\n2.Left rotate"))
step = int(input("Steps to rotate : "))

if(choice == 1):
    RightRotateList(user_list, step)

elif(choice == 2):
    LeftRotateList(user_list, step)

else:
    print("Invalid !")
