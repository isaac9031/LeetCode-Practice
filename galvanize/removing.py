#Removing duplicate numbers in place
def remove_duplicates_in_place(nums):
    seen = {}
    i = 0
    while i < len(nums):
        if nums[i] not in seen:
            seen[nums[i]] = True
            i += 1 #stays in the same index if an element was deleted in the else statement since the list is getting shorter
        else:
            del nums[i] #deletes that specific element in the specified list. need to be a list or a dic and specify which one
            # we cannot use nums.remove(nums[i]) since it  removes  the first elements in the list that has that value, that's why the 1 at the beginning is removed
    return nums

list1 = [1, 1, 3, 4, 5, 1, 2, 3]
print(remove_duplicates_in_place(list1))  # Output: [1, 3, 4, 5, 2]



def remove_second_small(lista):
    #a variable to have the min value
    #another one for the second smallest
    #a for loop to compare against previous values
    #remove the second smallest
    minimum = min(lista)
    sec_min = float("inf") #still unknown
    for n in lista:
      if n<sec_min and n != minimum:
         sec_min = n
    lista.remove(sec_min)

    return lista


lista = [5, 3, 2, 1, 4]
print(remove_second_small(lista))
