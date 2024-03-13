# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
def calculate_sum(values):
    total = 0
    if len(values)>=1:
        total = sum(values)
        return total

print(calculate_sum([20,20,20,40]))
