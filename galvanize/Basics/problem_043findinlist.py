# Complete the find_indexes function which accepts two
# parameters, a list and a search term. It returns a new
# list that contains the indexes of the search term in
# the search list.
#
# Remember that indexes in Python are zero-based. That
# means the first element in the list is index 0.
#
# Examples:
#   * search_list:  [1, 2, 3, 4, 5]
#     search_term:  4
#     result:       [3]
#   * search_list:  [1, 2, 3, 4, 5]
#     search_term:  6
#     result:       []
#   * search_list:  [1, 2, 1, 2, 1]
#     search_term:  1
#     result:       [0, 2, 4]
#
# Look up the enumerate function to help you with this problem.

#ENUMERATE CAN ONLY BE USED WITH LISTS
def find_indexes(search_list, search_term):
    new_list = []
    for i, value in enumerate(search_list): # it will iterate thru a table 0 3; 1 2; 1 1;
        if value == search_term:        # it will check if the value(3) is equal 2,
            new_list.append(i)          # will add the index if the value is the same, it will then go back to the for loop and check index value
    return new_list

print(find_indexes([3, 2, 1, 2, 1], 2))
