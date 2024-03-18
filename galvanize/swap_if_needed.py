# Replace the comment "swap the items" with code that will swap the first two items if the first item in the list is greater than the second item in the list.
# For example:
# If the input is [1, 2], it should return [1, 2].
# If the input is [4, 2], then it should return [2, 4].


def sort(items):
    while True:
        swapped = False
        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                items[i+1], items[i]  = items[i], items[i+1]
                swapped = True
        if swapped == False:
            break
    return items

items = [2,1, 4, 5, 3, 2]
print(sort(items))


def sort(items):
    while True:
        made_a_swap = False
        for i in range(len(items) - 1):
            if items[i] > items[i+1]:
                (items[i], items[i+1]) = (items[i+1], items[i])
                made_a_swap = True
        if not made_a_swap: # not means that it will change whatever is after to the opposite. in this case False becomes true
            break
    return items
items = [2,1, 4, 5, 3, 2]
print(sort(items))
