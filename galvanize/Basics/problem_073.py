# Write a class that meets these requirements.
#
# Name:       Student
#
# Required state:
#    * name, a string
#
# Behavior:
#    * add_score(score)   # Adds a score to their list of scores
#    * get_average()      # Gets the average of the student's scores
class Student:
    def __init__(self, name):
        self.name = name
        self.total = []

    def  add_score(self, score):
        self.total.append(score)

    def get_average(self):
        if len(self.total) == 0:
            return None
        else:
            return sum(self.total)/len(self.total)

student = Student("Isaac")

student.add_score(80)
student.add_score(100)
print(student.get_average())


# Example:
#    student = Student("Malik")
#
#    print(student.get_average())    # Prints None
#    student.add_score(80)
#    print(student.get_average())    # Prints 80
#    student.add_score(90)
#    student.add_score(82)
#    print(student.get_average())    # Prints 84
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.
