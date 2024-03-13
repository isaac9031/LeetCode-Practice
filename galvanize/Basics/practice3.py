def sub_total(bill):
    total = 0
    for i in bill:
            subtotal =  i.get("quantity")*i.get("item_cost")
            total += subtotal
    return total

bill = [
    {"description": "Tennis Ball", "quantity": 3,},
    {"description": "3 person tent", "quantity": 1,},
     {"description": "hammock", "quantity": 1,},
]


print(sub_total(bill))
