# Write a class that meets these requirements.
#
# Name:       Person
#
# Required state:
#    * name, a string
#    * hated foods list, a list of names of food they don't like
#    * loved foods list, a list of names of food they really do like
#
# Behavior:
#    * taste(food name)  * returns None if the food name is not in their
#                                  hated or loved food lists
#                        * returns True if the food name is in their
#                                  loved food list
#                        * returns False if the food name is in their
#                                  hated food list
#
class Person:
    def __init__(self, name, hated_food_list, loved_food_list):
        self.name = name
        self.hated_food_list = hated_food_list
        self.loved_food_list = loved_food_list
    def taste(self, food):
        self.food = food
        if food in self.loved_food_list:
            return True
        elif food in self.hated_food_list:
            return False
        else:
            return None

person = Person("Hai", ["pozole", "papaya"], ["pho", "steak"])
print(person.taste("pozole"))
print(person.taste("pho"))


# Example:
#    person = Person("Malik",
#                    ["cottage cheese", "sauerkraut"],
#                    ["pizza", "schnitzel"])
#
#    print(person.taste("lasagna"))     # Prints None, not in either list
#    print(person.taste("sauerkraut"))  # Prints False, in the hated list
#    print(person.taste("pizza"))       # Prints True, in the loved list
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.
