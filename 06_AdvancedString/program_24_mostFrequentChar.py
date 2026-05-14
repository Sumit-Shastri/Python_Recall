# find the most frequent character

dict = {}

def MostFrequent(str):

    for char in str:

        count = 0

        for check in str:

            if(char == check):
                count = count+1
            else:
                count = count + 0

        dict.update({char:count})
    
    mostFrequent = max(dict, key = dict.get)
    print(mostFrequent)


userStr = input("Enter string : ")
MostFrequent(userStr)
