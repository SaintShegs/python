# from random import randint
# number= randint(1,10)

# # print(number)

# player_name=input("Hi, what's your name?\n")

# print(f"Okay!, {player_name} i am guessing aa number between 1 and 10")

# no_of_guesses= 0

# trialsleft=5

# while no_of_guesses < 5:
#     guess=input("Guess the number:\n")
#     no_of_guesses+=1
#     trialsleft-=1
#     # print(guess)

#     if (guess.isdigit()):
#         if int(guess) == number:
#             print("You guessed right")
#             print("you guessed the number in",no_of_guesses, "trials")
#             break
#         elif int(guess) > number:
#             print("You guess is too high")
#             if trialsleft==0:
#                 print(f"Game Over")
#             else:
#                 print(f"You have {trialsleft} trials left ")
#         elif int(guess) < number:
#             print("Your guess is too low")
#             if trialsleft==0:
#                 print(f"Game Over")
#             else:
#                 print(f"You have {trialsleft} trials left ")
#     else:
#         print("Invalid entry")
#         if trialsleft==0:
#             print(f"Game Over")
#         else:
#             print(f"You have {trialsleft} trials left ")
# else:
#     print("You did not guess right, the number was ",number)




class Female(object):
    def __init__(self,name,language, skin, skill):
        self.name = name
        self.language = language 
        self.skin = skin
        self.skill =skill
        print('Nice you made a female')
        # pass
    def speak(self):
        print('My name is', self.name, 'i am', self.skin, 'in complexion')
        # pass
    def lang(self):
        print('I speak', self.language, 'and i am', self.skin, 'skinned')
    def hobby(self):
        print("i love", self.skill)


class Male(Female):
    def __init__(self, name, language, skin,skill, age):
        super().__init__(name, language, skin, skill)
        self.age = age
        print("You have a male")
    def speak(self):
        print("Hi, i am",self.name," an intro tech teacher and i am " , self.age, "years old")

   
steph = Female('Stephanie','Hausa','fair', "sewing")
tosin = Female('Tosin', 'YORUBA', 'caramel',"coding")
mariam = Female('Maria', 'IGBO', 'dark',"Talking to david")
steph.speak()
tosin.speak()
mariam.speak()
tosin.lang()
steph.hobby()
mariam.hobby()
tosin.hobby()

Prof = Male('Sege','Hausa','fair', "Coding", 1)
Prof.speak()
Prof.lang()