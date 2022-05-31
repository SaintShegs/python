# Chain Conditional (and  / or)

x = 2
y = 3

if x == y and x+y == 5 :
    print('Worked')

if x == y or x+y == 5 :
    print('Workkkkkked')

if x == 3 and x+y == 5 :
    print('Working')

    if x == 3 or x+y == 5 :
        print('Working')


if not(x == y and x+y == 5) :
    print("worknot")

else:
    print('G😏😏d Morning')



# Example 2

if x==2:
    print("correct")
    if y == 3:
        print("x=2, y=3")
    else:
        print('x=2 , y!=3')
else:
    print("x!=2")


# List
list1= ["apple", "sansung", "infinix","infinix", "Tecno", "Redmi"]
# Set
set1= {"apple", "sansung", "infinix", "Tecno", "Redmi"}
# dictionary
thisdict={
    "brand":"Ford",
    "model": "Mustang",
    "year": 1964
}

# Turple
tup_1=("apple", "samsung", "infinix","infinix", "Tecno", "Redmi")

print(type(tup_1))
print(type(list1))
print(type(set1))
print(type(thisdict))


# for loops (start, stop, step default +1)
for x in range (0,10, 3):
    print(x)

print(len(tup_1))

conver = list(tup_1)
print(conver)

(conver.remove("apple"))
(conver.remove("samsung"))

print(conver)

conver.insert(2, "Samsung")

print(conver)



print("Faith" in conver)

#String methods

string1= "Temiloluwa"

print(string1.find("l"))
print(string1.count("l"))

# EXAMPLE
password= input ("Please type in your password:  ")
if password.isupper():
    print("You have entered a strong password")
else:
    print("TRy agaim")




#seT
set1 = {"shege", "MAriam", "David", "Damola"}
set2 = {"shege", "David"}

print(set1)

name=list(set1)
print(name)

print(len(set1))

set1.add("oba")
print(set1)

set1.discard("oba")

print(set1)

newSet= set1.difference(set2)
newSet4= set1.intersection(set2)
print(newSet)
print(newSet4)




# Dictionary
thisdict={
    "brand":"Ford",
    "model": "Mustang",
    "year": 1964
}


put=thisdict["model"]
put= thisdict.get("model")
print(put)
print(thisdict)
print(thisdict["brand"])
print(thisdict["model"])
print(thisdict["year"])

mariam=thisdict.keys()
print(mariam)

mariam=thisdict.values()
print(mariam)

# to add a new item to the ariginal dict

thisdict["wheels"] = "4 wheel drive"
thisdict["color"] = "red"

print(thisdict)

thisdict.pop("color")

print(thisdict)


#to get the key and value pairs
temi= thisdict.items()
print(temi)


#To check if a key exists
if 'model' in thisdict:
    print("Yes, 'model' is one of the keys in thisdist")