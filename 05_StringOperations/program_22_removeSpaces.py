# remove spaces

def removeAllSpaces(str):
    op = str.replace(" ", "")
    print(op)

def removeLeftRight(str):
    op = str.strip()
    print(op)

def removeLeft(str):
    op = str.lstrip()
    print(op)

def removeRight(str):
    op = str.rstrip()
    print(op)

def removeAllPossible(str):
    op = "".join(str.split())
    print(op)

def removeAndMakePerfect(str):
    op = " ".join(str.split())
    print(op)

while(True):

    userStr = input("Enter string : ")
    print("""1. Remove all spaces
    2. Remove left spaces
    3. Remove right spaces
    4. Remove Left and Right spaces
    5. Remove all Possible (tab, newline, etc)
    6. Remove and make perfect
    7. exit""")
    
    choice = int(input("Choose : "))

    if(choice == 7):
        print("Exiting...")
        break

    match choice:
        case 1:
            removeAllSpaces(userStr)
        case 2:
            removeLeft(userStr)
        case 3:
            removeRight(userStr)
        case 4:
            removeLeftRight(userStr)
        case 5:
            removeAllPossible(userStr)
        case 6:
            removeAndMakePerfect(userStr)
        case _:
            print("fuck !")


    