# Handle file not found error

def extractData(file):

    try:
        with open(file, "r") as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        print("File is not available , please check file name and try again.")

user_file_name = input("Enter file name : ")
extractData(user_file_name)

print("Thankyou !")