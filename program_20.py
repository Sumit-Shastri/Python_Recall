# count vowels
# A a E e I i O o U u

def countVowels(str):

    list = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    count = 0

    for c in str:
        for i in list:
            if(c == i):
                count = count + 1
    
    return count

while(True):
    userStr = input("Enter String : ")
    vowelCount = countVowels(userStr)
    print(f"Total vowels in {userStr} are : {vowelCount}")