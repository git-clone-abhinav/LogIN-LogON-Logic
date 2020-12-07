import hashlib
password = input("Enter the password : ")
a = hashlib.md5(password.encode())

print(a)