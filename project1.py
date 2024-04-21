import os 
# import sys 

global adad
def exitProgram():
    os.system('clear')
    
    print("GOOD BYE " + username + " ................................")
    while True:
        input()

def signupProgram():
        global username, password, usernameLogin, passwordLogin, name, lastName, confirmPassword 
        print("welcome to sign up...")
        print("")
        print("name: ")
        name = input()
        print("last name: ")
        lastName = input()
        print("username: ")
        username = input()
        print("password: ")
        password = input()
        print("confirm password: ")
        confirmPassword = input()
        os.system('clear')

def loginProgram():
        global username, password, usernameLogin, passwordLogin,adad 
        print("welcome to login...")
        print("")
        print("user name:")
        usernameLogin = input()
        print("password:")
        passwordLogin = input()
        os.system('clear')
        if(username == usernameLogin and password == passwordLogin):
            adad = 3
        elif(username != usernameLogin or password != passwordLogin):
            print("username ya password ghalate, mojadad emtehan kon :) ")
            loginProgram()



def isalpha(string): 
    checkStr = string.isalpha()
    if(checkStr == False):
        print("faghat harfe alefba estefade kon...")

os.system('clear')
print("1. sign up")
print("2. login")
print("3. Exit")
adad = input("lotfan adad 1 ya 2 ya 3 ra vared konid: ")
os.system('clear') 
# while True: 
if(adad == "3"):
    exitProgram()
    # sys.exit() 
while(adad == "1" or adad == "2"): 
    if(adad == "1"):
        signupProgram()
        adad = "2"
        
    elif(adad == "2"):
        loginProgram()

    if(adad == 3):
        print("welcome to " + usernameLogin + " account...")
        print("")
        print("1. sabte daramad")
        print("2. sabte hazine")
        print("3. sabte daramad")
        print("1. sabte daramad")
        print("1. sabte daramad")
        print("1. sabte daramad")
        print("1. sabte daramad")
        while True:
            input()


