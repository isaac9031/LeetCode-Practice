# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

def calculate_grade(values):
    grades_in_range = []
    for value in values:
        if value >= 0 and value<=100:
            grades_in_range.append(value)
    average = sum(grades_in_range)/len(grades_in_range)
    if average >= 90:
        return "A"
    elif average >=80 and average <90:
        return "B"
    elif average >=70 and average <80:
        return "C"
    elif average >=60 and average <70:
        return "D"
    else:
        return "F"
print(calculate_grade([90,90,100,100]))

####questions on test
def partition(list, size):
    chunks = []
    in_progress = []
    for item in list:
        if len(in_progress) == size:
            chunks.append(in_progress)
            in_progress = []
        in_progress.append(item)
    return chunks

input = [0, 1, 2, 3, 4, 5, 6]

result = partition(input, 2)
print(result)

def count_matches(items, param2=None):
    matches = []
    for item in items:
        if(item.get("color") == param2):
            matches.append(item)
    return len(matches)

input = [
    {"background": "green",  "size": 5,  "color": "blue"},
    {"background": "yellow", "size": 5,  "color": "green"},
    {"background": "blue",   "size": 25, "color": "green"},
    {"background": "yellow", "size": 5,  "weight": "light"},
]

result = count_matches(input)
print(result)



from datetime import datetime
class Invoice:
    def __init__(self, customer_name, amount, invoice_date):
        self.customer_name = customer_name
        self.amount_due = amount
        self.invoice_date = invoice_date

def amount_due(invoices, days=30):
    past_due = 0
    for invoice in invoices:
        if (datetime.now() - invoice.invoice_date).days > days:
            past_due += invoice.amount_due
    return past_due

invoices = [
    Invoice("Raul", 25.00, datetime(2010, 4, 15)),
    Invoice("Poli", 50.00, datetime(2029, 11, 5)),
    Invoice("Don", 75.00, datetime(2012, 7, 21)),
    Invoice("Anne", 100.00, datetime(2035, 6, 17))
]

result = amount_due(invoices, 90)
print(result)


def divide_bill(bill, num_diners, tip):
    total_no_tip = bill
    total = bill*.01*tip + bill
    if tip >0:
        return total/num_diners
    else:
        return total_no_tip

print(divide_bill(30, 5, .1))
