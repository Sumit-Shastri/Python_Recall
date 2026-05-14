# reverse a string

def reverseString(str):
    reversed_str = str[::-1]
    return reversed_str

user_str = input("Enter a string : ")
rev_str = reverseString(user_str)
print(f"Reversed string of '{user_str}' is '{rev_str}'")