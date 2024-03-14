# Complete the sum_of_squares function which accepts
# a list of numerical values and returns the sum of
# each item squared
#
# If the list of values is empty, the function should
# return None
#
# Examples:
#   * [] returns None
#   * [1, 2, 3] returns 1*1+2*2+3*3=14
#   * [-1, 0, 1] returns (-1)*(-1)+0*0+1*1=2
#
# Write out some pseudocode before trying to solve the
# squared_list = []
# if len(values) == 0 return None for i in values:  square_list.append(i**2)
#
#
# problem to get a good feel for how to solve it.




def sum_of_squares(values):
    total = 0
    if len(values) == 0:
        return None
    for n in values:
        total+= n**2
    return total

print(sum_of_squares([2, 4]))



def sum_of_squares(values):
    square_list = []
    if len(values) == 0:
        return None
    else:
        for n in values:
            square_list.append(n**2)
        return sum(square_list)

print(sum_of_squares([2,4]))


def sum_of_squares(values):
    square_list = [x ** 2 for x in values]
    print(square_list)
    return sum(square_list) if len(square_list) > 0 else None

print(sum_of_squares([2, 4]))
