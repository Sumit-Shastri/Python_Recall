# check palindrome

def checkPalindrome(str):
    if(str == str[::-1]):
        print(str," is a palindrome.")
    else:
        print(str," is not a palindrome.")

while(True):
    userStr = input("Enter string or number : ")
    checkPalindrome(userStr)