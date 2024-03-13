# Complete the pairwise_add function which accepts two lists
# of the same size. It creates a new list and populates it
# with the sum of corresponding entries in the two lists.
#
# Examples:
#   * list1:  [1, 2, 3, 4]
#     list2:  [4, 5, 6, 7]
#     result: [5, 7, 9, 11]
#   * list1:  [100, 200, 300]
#     list2:  [ 10,   1, 180]
#     result: [110, 201, 480]
#
# Look up the zip function to help you with this problem.

def pairwise_add(list1, list2):
    new_list = []
    zipped = list(zip(list1,list2))  # a list with tuples is created, [(1,4),(2, 5),(3,6),(4,7)]..
    total = 0                        #..to use at the end in the for loops
    add_tuples = []
    for i in zipped:        #it access the first tuple
        for x in i:         # it acess the first element of the tuple, then on the next loop the second
            total += x      #adds the first and secont element of the tuple 4+1= 5
        add_tuples.append(total) #adds 5 to the list
        total = 0   #resets total to zero, now it will go back to the first for loop and to the second tuple
    return add_tuples




print(pairwise_add([1, 2, 3, 4],[4, 5, 6, 7]))

#Solution
# def pairwise_add(list1, list2):
#     results = []                                        # solution
#     for value1, value2 in zip(list1, list2):            # solution
#         results.append(value1 + value2)                 # solution
#     return results
