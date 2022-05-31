# from random import randint

# options = ["Rock", "Paper", "Scissors"] 
# computer = options[randint(0,2)]
# print(computer)
# player = False
# while player == False:
#     player = input("Rock, Paper, Scissors: ")
#     player = player.lower()
#     player = player.capitalize()
#     print(player)
#     if player == computer:
#         print("Tie")

#     elif player == "Rock":
#         if computer == "Paper":
#             print("You loose!", computer, "covers", player)
#         else:
#             print("You win!", player, "smashes", computer)
#     elif player == "Paper":
#         if computer == "Scissors":
#             print("You loose!", computer, "cuts", player)
#         else:
#             print("You win!", player, "covers", computer)
#     elif player == "Scissors":
#         if computer == "Rock":
#             print("You loose!", computer, "smashes", player)
#         else:
#             print("You win!", player, "cut", computer)
#     else:
#         print("Thats not a valid play, Check your spelling!")
    
#     player = False
#     computer = options[randint(0,2)]


# FUNCTions
# definition function(parameter):
#     return statement

def addTwo(x):

    return x+2

print(addTwo(10))



def addTwo(x):

    return x-2

print(addTwo(10))


# for i in range(10):
#     def show():
#         print(i*2)
#     show()

def printString(str):
    return str

printsungba=printString("Table")


print(printsungba)

def force (mass, acce):
    return(mass * acce)

p=force(3,9)

print(p)

def something():
    print ("Hi")

something()


#.#. If we dont want to constantly write parameters(()), 
## we can give a default value for our parameters, i like a dealt value of x
## Then if we want text to be set to something we can do: def.func(x, .text='4)

    


def multi(x, text= '4'):
    print(text)
    if text == '1':
        print('text is 1')
    else:
        print('text is not 1')


multi('owa', '')
multi('owa', '20')
