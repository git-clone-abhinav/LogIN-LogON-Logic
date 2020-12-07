from os import path 
import hashlib
id = 0
def passset(id):
    f = open("d:\password.txt","w+")
    if id == 1:
        print("Reset Password initiated ..") 
    else:
        print("No password detected ,set a password for future reference.")
    password = input("Enter a new Password : ")
    with open('d:\password.txt', 'w') as f:
        f.write("%s" % password)

while True:
    if(str(path.exists("d:\password.txt")) == "True"):
        pass_input = input("Enter your password : ")
        with open('d:\password.txt') as f :
            first_line = f.readline()
        if pass_input == first_line != "":
            print("Access Granted.")
            break
        elif pass_input == "resetpassword" :
            id = 1
            passset(id)
        else:
            print("Incorrect Password, please try again.")
            
    else:
        id = 0
        passset(id)