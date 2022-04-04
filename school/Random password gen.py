import random

Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
while 1:
    password_len = int(input("Password Length :"))
    password_count = int(input("Type 1 if someones watching :"))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
           password_char = random.choice(Chars)
           password = password + password_char
    print("Yo password is here bro ----> :", password)