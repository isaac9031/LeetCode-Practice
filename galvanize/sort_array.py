def sort(items):
    while True:
        made_a_swap = False
        for i in range(len(items) - 1):
            if items[i] > items[i+1]:
                (items[i], items[i+1]) = (items[i+1], items[i])
                made_a_swap = True
        if made_a_swap == False :
            break
    return items

items = [9,8,7,8,2,5]
print(sort(items))
