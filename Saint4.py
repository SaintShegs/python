list1 = ['mariam', True, 'damola', 'david', 1, 'temi']
list2 = ['rhema', 'eggy', 'mummy']

tuple_faith = ('onome', 'segun')

list1[1] ='faith'

print(len(list1))
print(type(list1))
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[-1])


# Slice operator

print(list1[2:6])
print(list1[:4]) #OR Print(list1[0:4])
print(list1[2:])


if 'mariam' in list1:
    print("Yes, 'mariam' is in list1")

list1[1] = 'faith'
print(list1)

list1[5:7] = ['salim', 'prof']
print(list1)


list1[-2] = 2
print(list1)

list1.insert(4, 'ade')
print(list1)

list1.extend(list2)
print(list1)

list1.extend(tuple_faith)
print(list1)

for i in range(len(list1)):
    print(list1[i])

[print(x) for x in list1]

# whileloop
i = 0
while i < 10:
    print(i)
    i+=1

# BASIC STRIGS METHOD
inp=input("Please enter a text ")

print(inp.strip())
print(inp.split("."))
print(inp.upper())
print(inp.capitalize())
print(inp.lower())

