# Now, define a __str__ method on each of the classes.
# For the Person class, have it return the name of the person.
# For the Employee class, have it use the super method to call the __str__ method of Person, then add the string " #«employee_id»" to it.
# employee = Employee(1232, "Noor")
# print(str(employee))  # Will print "NOOR #1232"


class Person:
    def __init__(self, name): #called automatically when a new instance of the class is created. used to initialize the object's attributes
        self.name = name.upper()

    def __str__(self): # called automatically when an object is converted to a string
        return self.name


class Employee(Person):
    def __init__(self, employee_id, name):
        super().__init__(name)
        self.employee_id = employee_id

    def __str__(self):
        return super().__str__() + " #" + str(self.employee_id) #used the str function in order to canconate now that both will be a string
# or    return super().__str__() + f" #{self.employee_id}"



employee = Employee(1232, "Noor")
print(str(employee))

# Could have also done:
employee = Employee(1232, "Noor")
print(employee.__str__())

# In Python, when defining a method within a class, the first parameter is
# always a reference to the instance of the class, conventionally named self.
# ensurs that the method operates on the specific instance it's called upon


# super().__str__() call to invoke the __str__ method of the Person class
# (its parent class), that's where we get the name(Noor), and then appends the employee_id to the resulting string.

# So, employee.__str__() applies the __str__ method to the employee instance,
# providing you with a string representation of that instance. We only applied the __str__ function to name in the super class Person.
#that is why we use the function str() for employee_id
