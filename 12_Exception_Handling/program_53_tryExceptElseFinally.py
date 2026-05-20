# use try except else finally

def extractData(file):

    try:
        f = open(file, "r")
        data = f.read()

    except FileNotFoundError:
        print("File is not available , please check file name and try again.")

    else:
        print("File found succesfully.")
        print("File content : ", data)

    finally:
        print("Closing resources")

user_file_name = input("Enter file name : ")
extractData(user_file_name)

print("Thankyou !")