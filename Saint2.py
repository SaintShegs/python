print (2>4)

print(2==2)

print(len('segun'))

print('segun' == 'SEgun')

print(len('david')==len('mariam'))

# file = open('text.txt', 'r')

# f = file.readlines()

# newList = []
# for line in f:
#     if line[-1] =='\n':
#      newList.append(line[:-1])
#     else:
#      newList.append(line)

# print(newList)

file = open('text.txt', 'r')
f = file.readlines()
newList = []
for line in f:
     newList.append(line.strip())
print(newList)




shola=72
funke=22

if funke > shola:
    print("Funke is greater that shola")
else:
    print("Funke isnt greater than shola")



print(bool('Hello'))
print(bool('15'))
print(bool(-15))
print(bool(""))

onome="MacBook"

print(bool(onome))
print(str(onome))

# #DEcisions

# if condition == True:
#     do this


Buharicontext= 'President'

if Buharicontext:
    print("JAPA")


Buharicontext= ''

if Buharicontext == True:
    print("JAPA")
else:
    print("JAPA STILL")


# buhari=input("IS buhari contesting ")

# if buhari == "Yes" or buhari == "YES":
#     print("JAPAaaaaaaaaaaaaaaaaaaaaaaaa")
# else:
#     print("JAPA STILLlllllllllllllllllllllllll")




# saint = input("Input your height ")

# if float(saint)==6.0:
#     print("You are qualified")
# elif float(saint) > 6.0:
#     print("ok, you are good to go")
# else:
#     print("Bye Bye")



age =input('input your age: ')

if int(age) == 15:
    print('you are eligible for the youth team')

    if int(age) > 18:
        print('go back home')

        if int(age) > 15:
            print('Bro you are older than 15')

else:
    print('you are younger than 15')



file = open('text.txt', 'w')

file.write('hey\n')
file.write('hey\n')
file.write('hey\n')
file.write('hey\n')
file.write('hey\n')
file.write('hey\n')

file.close()
        


