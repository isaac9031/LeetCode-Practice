class Point ():
    def __init__ (self, x=0, y=0) :
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move (self, x, y) :
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p): #returning scalar value, ex p1+p2 is 3*3 + 4*2 =15
        return self.x * p.x + self.y * p.y

    def __str__(self): #__str__() method returns a human-readable, or informal, string representation of an object
        return '('+str(self.x)+ ','+str(self.y)+')'

p1 = Point (3,4)
p2 = Point (3,2)
p3 = Point (1,3)
p4 = Point (0,1)

# p1 + p2   #p2 become the parameter p in __add__ and p1 becomes self
p5 = p1+p2
p6 = p4-p1
p7 = p2*p3

print(p5,p6,p7)


CONTINUE AT 3:14
