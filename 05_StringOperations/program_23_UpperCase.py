# convert to upper case without using upper()

def Upper(str):
    result = ""

    for char in str:
        if('a' <= char <= 'z'):
            result = result + chr(ord(char) - 32)
        else:
            result = result + char

    print("Result : ",result)

userStr = input("Enter the string : ")
Upper(userStr)