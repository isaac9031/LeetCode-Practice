# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]
def halve_the_list(list):
    list1 = (len(list)//2)
    list2=(len(list)//2) +1
    list1_final = []
    list2_final=[]


    if len(list)%2 == 0:
        list1_final = list[0:(len(list) // 2)]
        list2_final =list[len(list)//2 : (len(list)+1) ]
        return list1_final, list2_final
    else:
        list1_final = list[0:((len(list) // 2)+1)]
        list2_final =list[((len(list) // 2)+1) : (len(list)+1) ]
        return list1_final, list2_final

print(halve_the_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))



