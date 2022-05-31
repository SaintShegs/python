studName=input("Please enter your name\n")
ExamNo=input("Please enter your matric number\n")
mathematics=input("Enter your score for Mathematics: ")
english=input("Enter your score for English: ")
computer=input("Enter your score for Computer: ")
physics=input("Enter your score for Physics: ")

score=[mathematics,english,computer,physics]
subjects=["Mathematics", "English", "Computer","Physics"]

f = open(f"{studName}.txt", "wt")

f.write(f"Name: {studName}\n")
f.write(f"Exam Number: {ExamNo}\n")
print("")
f.write("\n")

for x in range(0,len(score)):

    if (score[x].isdigit()):
        if (int(score[x]) >= 80):
            print(f"Your grade for {subjects[x]} is A")
            f.write(f"Your grade for {subjects[x]} is A\n")
        elif (int(score[x]) >= 65):
            print(f"Your grade for {subjects[x]} is B")
            f.write(f"Your grade for {subjects[x]} is B\n")
        elif (int(score[x]) >= 55):
            print(f"Your grade for {subjects[x]} is C")
            f.write(f"Your grade for {subjects[x]} is C\n")
        elif (int(score[x]) >= 45):
            print(f"Your grade for {subjects[x]} is D")
            f.write(f"Your grade for {subjects[x]} is D\n")
        elif (int(score[x]) >= 40):
            print(f"Your grade for {subjects[x]} is E")
            f.write(f"Your grade for {subjects[x]} is E\n")
        elif (int(score[x]) >= 0):
            print(f"Your grade for {subjects[x]} is F")
            f.write(f"Your grade for {subjects[x]} is F\n")
        f.write("\n")
        print("")

    elif (score[x]==""):
        print(f"Your score for {subjects[x]} is pending")
        print("")
        f.write(f"Your score for {subjects[x]} is pending\n")
        f.write("\n")

    else:
        print(f"Please enter a valid score for {subjects[x]}")
        print("")

f.close()
# Second


# username = 'Faith'

# password = 'Faith123'
 
# User_input = input('What is your name?\n')

# if User_input == username:
#     Login= input('Password:\n')
#     if Login ==password:
#         print('You have login succesfuly')
#     else:
#         print('Username or Password wrongly inputted😞')

# else:
#     print('Username or Password wrongly inputted😞')

    

# Third

import re
re.compile('<title>(.*)</title>')




# while True:
#  password = input ('input your password!: ')

#  is_valid = 0

#  if (len(password)<5):
#     print("Password should have at least 6 characters") 
#  elif (len(password)>12):
#     print("Password should not exceed least 12  characters") 
#  elif not re.search("[A-Z]", password):
#     print("Invalid! Password should contain at least one alphabet in Uppercase")
#  elif not re.search("[a-z]", password):
#     print("Invalid! Password should contain at least one alpahbet in lowercase") 
#  elif not re.search("[0-9]", password):
#     print("Invalid! Password should coantain at least one number")
    
#  else:
#     is_valid = 1
#     print("Valid password")
#     break


# ade = 0
# while ade==True:
#     print("running")
# else:
#     print("stopped")
#     ade==False
