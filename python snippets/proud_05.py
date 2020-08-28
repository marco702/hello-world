'''
creating 1st game and
using while loops
'''

secret = "finance"
guess = ""
count = 1
limit = 3
limit_reached = False

print ("Welcome to Marco's first game! It is a guessing game"
       "\nCan you guess the secret!"
       "\n ")

while guess != secret and limit_reached == False:
    guess = input("Please enter your guess: ")
    if guess != secret and count != limit:
        count += 1
    else:
        limit_reached = not limit_reached

if count == limit and guess != secret:
    print("Too bad, you loose. \nLOOSER!")
else:
    print("Yeaaah! \nYOU WIN!")