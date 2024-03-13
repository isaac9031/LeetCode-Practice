# Write a function that meets these requirements.
#
# Name:       num_concat
# Parameters: two numerical parameters
# Returns:    the concatenated string conversions
#             of the numerical parameters
#
# Examples:
#     input:
#       parameter 1: 3
#       parameter 2: 10
#     returns: "310"
#     input:
#       parameter 1: 9238
#       parameter 2: 0
#     returns: "92380"

def num_contact(num1,num2):
    string1= str(num1)
    string2= str(num2)
    return string1+string2

print(num_contact(9238,10))
