from os import path 
import hashlib


id = 0
salt = "RKh?^rLYSBf#nD-2tGzjx^zXy+q#Ph=^kb^r6&A_9NAhdh7r7k%H!d%-k%5D@C5-ysn=dd-rwKMR6#y_yR@Ds^#4-Wc-hy3&aKT&"

def hashing(key):
    salted = salt + key
    temp = bytes(salted, 'utf-8') 
    obj = hashlib.sha1(temp)
    hex_dig = obj.hexdigest()
    return hex_dig


def passset(id):
    f = open("d:\password.txt","w+")


    if id == 1:
        print("Reset Password initiated ..") 
    else:
        print("No password detected ,set a password for future reference.")

    
    password = input("Enter a new Password : ")
    
    with open('d:\password.txt', 'w') as f:
        f.write("%s" % hashing(password))

while True:
    if(str(path.exists("d:\password.txt")) == "True"):
        pass_input = input("Enter your password : ")
        a = hashing(pass_input)

        with open('d:\password.txt') as f :
            first_line = f.readline()
        b = first_line

        if a == b != "":
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