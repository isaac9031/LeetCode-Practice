# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    max_value = values[0]
    for i in values:
        if i > max_value:
            max_value = i
    return max_value
print(max_in_list([110,10,5,30]))


# or

def max_in_list(values):
    maximum = float("-inf")
    for n in values:
        if n > maximum:
            maximum = n
    return maximum
print(max_in_list([110,10,5,30]))

# or
def max_in_list(values):
    return max(values)
print(max_in_list([110,10,5,30]))
