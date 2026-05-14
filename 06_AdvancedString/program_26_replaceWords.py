# replace words in sentences

def replaceWords(sent, old, new):
    newSent = sent.replace(old, new)
    print(newSent)


userSent = input("Enter the sentence : ")
userOld = input("Enter the word to replace : ")
userNew = input("Enter the new word : ")

replaceWords(userSent, userOld, userNew)
