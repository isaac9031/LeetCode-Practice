#EXAMPLE 1:
#classes have attributes and methods
#attributes are variables that belong to a certain object
class Dog(object): #a class that inherits from object and has some methods
    def __init__(self): #init known as the constructor method, it needs to be in most classes
        print('Niche doggo')
    def speak(self):
        pass

tim = Dog() #will allow the init method to automatically run
fred = Dog() #both will print Niche doggo

#EXAMPLE 2:
#creating attributes need the self keyword. ex self.amount = 44
class Cat(object): #a class that inherits from object and has some methods
    def __init__(self, name, age):
        self.name = name
        self.age = age                  ##add the attribute here in order to be able to use
        self.li = [1, 3, 4]               ##in the other methods

    def speak(self): #these are called methods
        print("Hi I am", self.name, 'and I am', self.age, 'years old')

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight


isaac = Cat("Isaac", 33) #isaac is an instance of the class/type Cat, it starts the class Cat immediatly, it calls init
hai = Cat("Hai", 22)
isaac.change_age(25)
isaac.speak()
hai.speak()
isaac.add_weight(55)
print(isaac.weight)
print(isaac.age)
print(isaac.li)
