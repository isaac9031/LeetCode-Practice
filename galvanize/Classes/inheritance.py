
class Dog(object): #a class that inherits from object and has some methods
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hi I am", self.name, 'and I am', self.age, 'years old')

    def talk(self):
        print('Bark')

class Cat(Dog): #Cat is inheriting from dog, dog is the parent class and cat is the child
    def __init__(self, name, age, color):
        super().__init__(name, age) #super calls the initialization of Dog first  automatically...
        self.color = color          #..adds self.name and self.age to our Cat object. Super class just means Dog
        #self.name = "tech" #... this shows us that we can also override attributes inherited from the Dog class. uncomment if want to see how the name changes

    def talk(self): #we are overriding the talk method that comes from Dog class
        print('Meow')


isaac = Cat('ISAAC', 5, 'blue') #isaac is an object of type Cat
jim = Dog('JIM', 80)
isaac.speak()  #this will call the speak method because Cat is inheriting from Dog. so it will print: Hi I am ISAAC and I am 5 years old
isaac.talk()

jim.speak() #will call the speak method from Dog class and print: => Hi I am JIM and I am 80 years old
jim.talk() #will print Bark
