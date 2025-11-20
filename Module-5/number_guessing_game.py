import random
secret_number=random.randint(1,10)
print(secret_number)
guess=int(input("enter a number"))
if guess<secret_number:
    print("you are too low try again")
elif guess >secret_number:
    print("you are too high try again")
else:
    print("congratulations you guessed the number")        