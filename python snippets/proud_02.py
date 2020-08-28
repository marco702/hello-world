'''
gather input from user
and inpout between two options
'''

age = input("What is your age? ")
name = input ("And what is your name? ")

print("Hi " + name + "! \nYou are still so young with your " + age + " years!")

friend = ""
while friend != "boyfriend" and friend != "girlfriend":
    friend = input("Enter boyfriend or girlfriend: ")
    if friend != "boyfriend" and friend != "girlfriend":
        print("You must type boyfriend or girlfriend"),

if friend == "boyfriend":
    age_friend = input("How old is he? ")
else:
    age_friend = input("How old is she? ")

result = int(age) + float(age_friend)

print("Together you are fantastic ",result," years young!! \nCongratulations")
