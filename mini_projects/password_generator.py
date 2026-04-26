import random
import string

length = int(input("Enter the password length:"))

use_letters = input("Do you want to use letters? (y/n):")
use_numbers = input("Do you want to use numbers? (y/n):")
use_symbols = input("Do you want to use symbols? (y/n):")

characters = ""

if use_letters == "y":
    characters += string.ascii_letters
elif use_numbers == "y":
    characters += string.digits
elif use_symbols == "y":
    characters += string.punctuation
elif characters == "":
    print("You must select at least one option!")
    exit()

password = ""

for i in range(length):
    password += random.choice(characters)

print("Your password is:", password)
