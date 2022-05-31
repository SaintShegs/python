#MATH MODULE
#Math.name of the function or class

# import math
import inspect
from queue import Queue

# print(math.pi)
# print(math.degrees(30))
# print(math.radians(1718.873))
# print(math.degrees(math.pi))


# def func(x):
#     if x == 1:
#         def rv():
#             print('x is equal to 1')
#     else:
#         def rv():
#             print('x is not equal to 1')
#     return rv

# newfunc = func(1)
# newfunc()
# print(newfunc)
# print(id(newfunc)) #to get the memory address
# print(inspect.getmembers(newfunc)) ## you have to import inspect module 
# print(inspect.getsource(newfunc)) ## you have to importinspect module

# print(inspect.getsource(Queue)) ## from the queue import queue(shows codes used in creating objects or classes )

# #other more complicated examples of optional parameters depending on inheritance.

# #CLASS AND OBJECT(introducing objects)
# #An object: in python, an object is pretty much anything built into a class and has an instance of a variable. eg RUN this


x = 3
y= 'string'
print(type(x))
print(type(y))

print(x-7)

import myModule

faith = myModule.myFunc(3)
print(faith)

onome = myModule.anotherFunc(8)
print(onome)

# help(str)


# import turtle

# x = 4
# y = 'string'

# rhema = turtle.Turtle()

#How we can import our modules into our function(import myModule)
#step 1: create a new file in the directory called myModule.py


#for  a method: it is anything you call on an object.
#it is what you call with a dot operator(.).
#e.g ".Turtle()" is a method that creates a new turtle object,

# x = 5
# y = "melts"

# print(y.upper())
# print(y.replace('m', 'i'))

#CLASSES AND OBJECTS 2 ()


#STEPS TO REGISTER INSTANCES IN CLASSES

# Step 1: In your def _init_ state the parameter e.g def_init_(self, name)
# step 2: (on the next line) register or qualify the parameter. - self.name = name, self.age = age or self.parameter = parameter
# step 3: use the qualified parameter within another method e.g ('Hi, I am "self.name = method below' )
# step 4: input the argument which is a value for the parameter - e.g roman = Dog('Roman)
# step 5: call the method on the object that has the positional argument e.g roman.speak()

# from turtle import color


class Dog():
    def __init__(self, name, age, gender, color):
        self.name = name
        self.age = age
        self.gender = gender
        self.color = color
        print('Nice you mad a dog')

    def speak(self):
        print('Hi, I am', self.name,  'I am', self.age,  'years old.' 'I am', self.gender)
    
    def skin(self):
        print('The color of my skin is', self.color)


henry = Dog('roman', 45, 'male','yellow')
roman = Dog('Henry', 45, 'male', 'black')
roman.speak()
roman.skin()
henry.speak()
henry.skin()