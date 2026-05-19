# Copy content from one file to another file


file1 = "file_46.txt"
file2 = "file_49.txt"

with open(file1, "r") as f1:
    print(f"Copying content from {file1}")
    data = f1.read()
    print("Copy complete.")

with open(file2, "w") as f2:
    print(f"pasting content to {file2}")
    f2.write(data)
    print("Paste complete")