# split list into even and odd

even_list = []
odd_list = []

def split_list_eo(l):
    
    for i in l:
        if(i % 2 == 0):
            even_list.append(i)
        else:
            odd_list.append(i)

UserList = [2,5687,22,45,78,12,11,345,67]
split_list_eo(UserList)
print("List : ",UserList)
print("Even list : ",even_list)
print("Odd list : ",odd_list)