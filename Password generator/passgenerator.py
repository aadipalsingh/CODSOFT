#Task 03:-password generator(CodSoft)
import random

print("------Get Your Password------")

length= input('Enter the Desired length of Your password: ')

if not length.isdigit():
    print("Invalid input. Please enter a positive integer.")
else:
    length = int(length)
    if length <= 0:
        print("Password length must be greater than 0.")
    else:
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = "0123456789"
        symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

        temp = lower + upper + num + symbols
        password = ''.join(random.choices(temp, k=length))

        print("Generated Password:", password)
