from os import path
print("")
    #print(path.isfile("password.txt"))

username = input("Please enter your username")
password = input("Please enter your password")
for line in open("passwords.txt", "r").readlines():
    login_info = line.split(";") 
    if username == login_info[0] and password == login_info[1]:
        print("welcome")
    elif username == login_info[0] or password == login_info[1]:
        print("wrong username or password")
    else:
        print("no such username and password")




'''
def isAuthorized():
  username = input("Enter your username: ").strip()
  password = input("Enter your password: ").strip()

  with open("users.txt", "r") as f:
    for line in f:
      loginInfo = line.strip().split(",")
      if username == loginInfo[0] and password == loginInfo[1]:
        return True
    return False

if isAuthorized():
  input("Authorized \t Press any key to continue: ")
else:
  input("no auth")


if path.isfile("password.txt"):
    #password input will be taken here
    print("File is here")

if str(path.isfile("password.txt")) == "False" :
    #password will be set here
    print("File is not here")

    passkey = input("Enter new password : ")
    f = open("password.txt", "w")
    f.write(passkey)
    f.close()
    exit()
'''