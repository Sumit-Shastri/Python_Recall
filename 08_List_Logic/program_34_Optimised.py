# find common in two lists

def find_common(l1, l2):
    
    return list(set(l1) & set(l2))

user_list1 = [2, 5, 6, 9, 10, 23, 45]
user_list2 = [5, 7, 3, 1, 9, 23, 46]

common = find_common(user_list1, user_list2)
print("Common elements:", common)