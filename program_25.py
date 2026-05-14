# check if 2 strings are anagrams

def checkAnagram(str1, str2):
    
    #check length
    str1List = []
    str2List = []

    if(len(str1) == len(str2)):

        str1List = sorted(str1)
        str2List = sorted(str2)

        if(str1List == str2List):
            print("They are anagrams.")
        else:
            print("They are not anagrams")
  
    else:
        print("They are not anagrams")

userStr1 = input("Enter string 1 : ")
userStr2 = input("Enter string 2 : ")

checkAnagram(userStr1, userStr2)