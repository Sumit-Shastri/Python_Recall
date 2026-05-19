# Write to a file

file = "file_46.txt"
data = "data to write in file."

with open(file, "w") as f:
    f.write(data)