# count words in file

file = "file_46.txt"
count = 0

with open(file, "r") as f:
    data = f.read()
    for word in data.split():
        count = count + 1

print("Total words in data : ", count)