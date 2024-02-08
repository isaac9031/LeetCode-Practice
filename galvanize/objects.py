import math  #x and y are objects
#import turtle

#a method is anything you are calling on an object itself. ex calling .lower method on the y object
#a functions is somthing that will take an object, and apply an operation to it

x = 5.7 #in this case x is an object of type int
y = 'stTTing'

print(type(x))
print(type(y))

print(math.floor(x))
print(y.lower()) #.lower is known as a method

# print(help(int)) this shows all the methods available for int
# print(help(str))

#a function is done with the def key. ex: def newfunc()
def func(x):
    return x+1
print(func(5))

#a class you call with the dot operator. ex:
tim = turtle.Turtle() #in this case we change the instance, creating a new object that will be stored in  the variabletim
