# Password Generator by Asra Fathima
# Beginner level project for Oasis Infobyte Internship

import random
import string

print("Welcome to Asra's Password Generator 🔐")

# Asking user for the length of the password
length = int(input("Enter the desired length of your password: "))

# Creating a set of characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generating a random password
password = ''.join(random.choice(characters) for _ in range(length))

# Displaying the generated password
print("\nYour strong random password is:", password)
print("Keep it safe and don’t share it with anyone!")