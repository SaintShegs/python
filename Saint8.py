# args and kwargs

# *args

def adder (*num):
    # sum =0
    # for n in num:
    sum=num[1]-num[0]
    print("Diff", sum)
adder(9,4)




def adder (*num):
    tot=0
    sum = num[0]
    for n in num:
        sum=sum-n
    print("Diff", tot)
adder(2,4,5)





# def adder (*num):
#     sum =0
#     for n in num:
#         sum=sum - n
#     print("Sum", sum)
# adder(2,4,6,9)


# kwargs

def intro(**data):
    print("\nData types of arguememt:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))

intro(firstname="rhema",lastname="sharma",age="14", email="sitasharma@gmail.com")
intro(firstname="faith",lastname="pygoddess",age="4", email="faithpy@gmail.com")
intro(firstname="rhema",lastname="sharma",age="14", email="sitasharma@gmail.com")



#CLASSES AND OBJECT(Contd)
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)
        print('First point')
    def __add__(self, p):
        return Point(self. x+p.x, self.y+p.y)
    def __sub__(self, p):
        return Point(self. x-p.x, self.y-p.y)
    def __mul__(self, p):
        return Point(self. x*p.x + self.y*p.y)
    def __division__(self, p):
        return Point(self. x/p.x - self.y/p.y)
    
    def __str__(self):
        return "(" + str(self.x) + '.' + str(self.y) + ")"

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(1, 3)
p4 = Point(0, 1)
p5 = p2 + p1
p6 = p3 - p1
p7 = p3 * p1
p8= p1/p3
print(p5)
print(p6)
print(p7)
print(p8)

