# count words in sentence

def CountWords(sent):

    list = sent.split()
    count = len(list)
    print("Count of words : ",count)

userSent = input("Enter a sentence : ")
CountWords(userSent)
