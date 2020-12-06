from os import path


    
while True:
    if(str(path.exists("d:\password.txt")) == "True"):
        pass_input = input("Enter your password : ")
        with open('d:\password.txt') as f:
            first_line = f.readline()
        if pass_input == first_line != "":
            print("Menu")
            break
        else:
            print("Incorrect Password, please try again.")
            

    else:
        f = open("d:\password.txt","w+")
        print("No password detected ,set a password for future reference.")
        password = input("Enter a new Password : ")
        with open('d:\password.txt', 'w') as f:
            f.write("%s" % password)