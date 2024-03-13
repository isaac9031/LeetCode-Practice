# Write four classes that meet these requirements.
#
# Name:       Animal
#
# Required state:
#    * number_of_legs, the number of legs the animal has
#    * primary_color, the primary color of the animal
#
# Behavior:
#    * describe()       # Returns a string that describes that animal
#                         in the format
#                                self.__class__.__name__
#                                + " has "
#                                + str(self.number_of_legs)
#                                + " legs and is primarily "
#                                + self.primary_color
class Animal:
    def __init__(self, number_of_legs,primary_color):
        self.number_of_legs = number_of_legs
        self.primary_color = primary_color

    def describe(self):
        return (f"{self.__class__.__name__} has {str(self.number_of_legs)} legs "
               f"and is primarily {self.primary_color}")


class Dog(Animal):
    def __init__(self):
        super().__init__(6,"black")
    def speak(self):
        return "Bark!"

class Cat(Animal):
    def __init__(self, color): #color parameter will receive arg when its called
        super().__init__(4,color)
    def speak(self):
        return "Miao!"

class Snake(Animal):
    def __init__(self,color):
        super().__init__(0,color)
    def speak(self):
        return "SSSS"


animal = Animal(10,"Green")
print(animal.describe())

my_dog = Dog()
print(my_dog.speak())

my_cat = Cat("Brown")
print(my_cat.speak())

my_snake = Snake("Red and Yellow")
print(my_snake.speak())


# Name:       Dog, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Bark!"
#
#
#
# Name:       Cat, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Miao!"
#
#
#
# Name:       Snake, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Sssssss!"
