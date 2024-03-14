# Complete the sum_of_first_n_numbers function which accepts
# a numerical limit and returns the sum of the numbers from
# 0 up to and including limit.
#
# If the value of the limit is less than 0, then it should
# return None
#
# Examples:
#   * -1 returns None
#   * 0 returns 0
#   * 1 returns 0+1=1
#   * 2 returns 0+1+2=3
#   * 5 returns 0+1+2+3+4+5=15
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def sum_of_first_n_numbers(limit):
    if limit < 0:
        return None
    if limit == 0:
        return 0
    total = 0
    for i in range(limit+1): #need +1 to also cover 5, since range is not inclusive for the stop range(start,stop,step)
        total+=i
    return total

print(sum_of_first_n_numbers(5))


def sum_of_first_n_numbers(limit):
    total = limit
    if limit <0:
        return None
    elif limit == 0:
        return 0
    else:
        for i in range(1,limit):
            total += (limit-i)
        return total



print(sum_of_first_n_numbers(5))
