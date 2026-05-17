# remove duplicates using sets

list = []

for i in range(10):
    a = int(input("Enter element : "))
    list.append(a)

print("Normal list : ",list)
print("Removed duplicates : ", set(list))