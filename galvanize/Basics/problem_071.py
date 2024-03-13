# Write a class that meets these requirements.
#
# Name:       Employee
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_fullname(self):
        return self.first_name +" " +self.last_name
    def get_email(self):
        return self.first_name.lower() + "." + self.last_name.lower() + "@company.com"

employee = Employee("Isaac","Olivares")
print(employee.get_fullname())
print(employee.get_email())



# Required state:
#    * first name, a string
#    * last name, a string
#
# Behavior:
#    * get_fullname: should return "«first name» «last name»"
#    * get_email:    should return "«first name».«last name»@company.com"
#                    all in lowercase letters
#
# Example:
#    employee = Employee("Duska", "Ruzicka")
#
#    print(employee.get_fullname())  # prints "Duska Ruzicka"
#    print(employee.get_email())     # prints "duska.ruzicka@company.com"
#
# You may want to look at the ".lower()" method for strings to
# help with this code.
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.
