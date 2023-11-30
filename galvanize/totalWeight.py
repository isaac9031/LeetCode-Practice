# shipment = [
#     {
#         "product_name": "beans",
#         "product_weight_pounds": 2,
#         "quantity": 5,
#     },
#     {
#         "product_name": "rice",
#         "product_weight_pounds": 1.5,
#         "quantity": 7,
#     },
# ]
# The total weight for this shipment is: (2 x 5) + (1.5 x 7) = 20.5
# If the shipment list is empty, then the function should return 0.



def find_shipment_weight(shipment):
    total = 0
    for n in shipment:
        total+=n["product_weight_pounds"]*n["quantity"] # n[] accesses the specific key
    return total
shipment = [
    {
        "product_name": "beans",
        "product_weight_pounds": 2,
        "quantity": 5,
    },
    {
        "product_name": "rice",
        "product_weight_pounds": 1.5,
        "quantity": 7,
    },
]

print(find_shipment_weight(shipment))
