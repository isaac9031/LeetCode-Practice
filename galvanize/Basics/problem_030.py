# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def find_second_largest(values): #using sort, which modifies original list in place
    if len(values) == 0 or len(values)==1:
        return None
    values.sort()
    return values[-2]

print(find_second_largest([40,30,100,80]))

def find_second_largest(values): #using sorted, which creates a new sorted list
    new_list = sorted(values)
    if len(values) == 0 or len(values) == 1:
        return None
    else:
        return new_list[-2]


print(find_second_largest([40,30,100,80]))



# DIFFERENCE BETWEEN SORT() AND SORTED()
# sort()” modifies the original list in place,
# while “sorted()” creates a new sorted list.

# list = [4,8,2,1]
# list.sort()
# #--> list = [1,2,4,8] now

# list = [4,8,2,1]
# new_list = sorted(list)
# #--> list = [4,8,2,1], but new_list = [1,2,4,8]
