# Simple Banking system

class PythonBank:

    def __init__(self, name, email, phone, password):
        self.userName = name
        self.userEmail = email
        self.userPhone = phone
        self.userPassword = password

    def createAccount(self):
        print("Create Account")
        print("Account created succesfully")
        print("Account details : ")
        print(f"Username : {userName}")
        print(f"email : {userEmail}")
        print(f"phone : {userPhone}")


while(True):

    print("Welcome to bank")

    choice = int(input("""1. create account
          2. Login
          3. exit
"""))
    
    match (choice):
        case 1:
            print("create account")

            userName = input("Enter User Name : ")
            userEmail = input("Enter User Email : ")
            userPhone = input("Enter your phone : ")
            password = input("Create password : ")
            
            pb = PythonBank(userName, userEmail, userPhone, password)
            pb.createAccount()
        
        case 2:
            print("Login\n")

            checkUserName = input("Enter Username : ")
            checkUserPassword = input("Enter your password : ")

            if(checkUserName == pb.userName and checkUserPassword == pb.userPassword):
                print("Login succesful")
        
        case 3:
            print("Exiting")
            def exit():
                return 1
            exit()

