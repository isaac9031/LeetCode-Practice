class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.children = []

    def add_child(self, person):
        self.children.append(person)

    def __repr__(self):
        return f"Person({self.first_name}, {self.last_name}, Children: {[child.first_name for child in self.children]})"


def get_person_and_child_names(person):
    child_names = [{
        "first_name": child.first_name,
        "last_name": child.last_name,
    } for child in person.children]

    return {
        "first_name": person.first_name,
        "last_name": person.last_name,
        "children": child_names,
    }

# Example usage:
# Creating instances of the Person class
parent = Person("John", "Doe")
child1 = Person("Alice", "Doe")
child2 = Person("Bob", "Doe")

print()

print("Initial Parent State:")
print(parent)

# Adding children to the parent
parent.add_child(child1)
print("\nParent State after adding child1:")
print(parent)

parent.add_child(child2)
print("\nParent State after adding child2:")
print(parent)

# Getting information about the parent and children
person_info = get_person_and_child_names(parent)

# Displaying the result
print("\nPerson Information:")
print(person_info)
