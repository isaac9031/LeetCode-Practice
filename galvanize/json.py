import json
#Converts json string to python object

def convert_json(json_formatted_string):
    # Use json.loads to convert the JSON-formatted string to a Python object
    try:
        python_object = json.loads(json_formatted_string)
        return python_object
    except json.JSONDecodeError as e:
        # Handle JSON decoding errors if necessary
        print(f"Error decoding JSON: {e}")
        return None

# Example usage:
json_string = '{"key": "value", "number": 42, "is_true": true}'
result = convert_json(json_string)

if result is not None:
    print("Converted Python object:", result)





#Converts  python object to json string
import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_to_json(person):
    # If the person is None, then return the JSON-formatted
    # version of None
    if person is None:
        return json.dumps(None)
        # Finish this return statement with json.dumps(None)

    # Create a dictionary from the Person instance
    d = {
        "name": person.name  ,  # Put person.name before the comma
        "age": person.age  ,  # Put person.age before the comma
    }

    # Pass the d variable to json.dumps on the
    # right-hand side of the assignment operator =
    result = json.dumps(d)
    return result

    # Return the value of result in JSON string format


# Example usage:
person_object = Person("John Doe", 30)
json_result = person_to_json(person_object)
print(json_result)
