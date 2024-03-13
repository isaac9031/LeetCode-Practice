def can_buy_ticket(age, state):
    if state == "NV" and state == "NJ" or age >= 18:
        return True
    if age >= 21:
        return True
    return False


state = "NV"
age = 21
print(can_buy_ticket(age, state))
