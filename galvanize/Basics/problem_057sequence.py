# Write a function that meets these requirements.
#
# Name:       sum_fraction_sequence
# Parameters: a number
# Returns:    the sum of the fractions of the
#             form 1/2+2/3+3/4+...+number/number+1
#
# Examples:
#     * input:   1
#       returns: 1/2
#     * input:   2
#       returns: 1/2 + 2/3
#     * input:   3
#       returns: 1/2 + 2/3 + 3/4

def sum_fraction_sequence(number):
    i = 1
    x = 1
    new_string = ""
    if number >0:
        while x <= number:
            new_string+= ((str(i) + "/" + str(x+1))+ "+")
            x+=1
            i+=1
        return new_string[:-1]

print(sum_fraction_sequence(3))
