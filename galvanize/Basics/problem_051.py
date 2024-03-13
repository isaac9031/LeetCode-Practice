# Write a function that meets these requirements.
#
# Name:       safe_divide
# Parameters: two values, a numerator and a denominator
# Returns:    if the denominator is zero, then returns math.inf.
#             otherwise, returns numerator / denominator
#
# Don't for get to import math!

import math

def safe_divide(num, den):
    if den ==0:
        return math.inf
    else:
        return num/den




print(safe_divide(5,2))
