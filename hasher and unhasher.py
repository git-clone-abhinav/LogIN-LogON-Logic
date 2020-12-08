# README
#
# For md5 hashing
#a = hashlib.md5(salted_password.encode())

import hashlib


password = input("Enter the password : ")
salt = "RKh?^rLYSBf#nD-2tGzjx^zXy+q#Ph=^kb^r6&A_9NAhdh7r7k%H!d%-k%5D@C5-ysn=dd-rwKMR6#y_yR@Ds^#4-Wc-hy3&aKT&"

salted_password = password + salt

temp = bytes(password, 'utf-8') 
a = hashlib.sha1(temp)
hex_dig = a.hexdigest()


print(hex_dig)