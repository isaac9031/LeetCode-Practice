# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    total = 0
    if len(values)>=1:
        for value in values:
            total += value
        average = total/len(values)
        return average

print(calculate_average([90,90,100,100]))


