import random
import string

captcha = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
print("CAPTCHA",captcha)
user_input = input("Enter the CAPTCHA: ")

if user_input == captcha:
    print(" Verified! Access granted.")
else:
    print("Incorrect. Try again.")
