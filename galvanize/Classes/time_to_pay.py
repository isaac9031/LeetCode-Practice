from datetime import datetime
class Invoice:
    def __init__(self, customer_name, amount, invoice_date): #setting up properties that represent the state
        self.customer_name = customer_name
        self.amount_due = amount
        self.invoice_date = invoice_date

def amount_due(invoices, days=30):
    past_due = 0
    for invoice in invoices:
        print(datetime.now())
        if (datetime.now() - invoice.invoice_date).days > days: #invoice.invoice_date accesses the datetime inside Invoice. thend it gets the difference by using .days
            past_due += invoice.amount_due #accesses amount_due thru invoice object
    return past_due

invoices = [
    Invoice("Raul", 25.00, datetime(2010, 4, 15)), #this are  the parameters of Invoice class
    Invoice("Poli", 50.00, datetime(2029, 11, 5)),#will not add this to past_due since its yr 2029
    Invoice("Don", 75.00, datetime(2012, 7, 21)),
    Invoice("Anne", 100.00, datetime(2035, 6, 17)) #will not add this to past_due since its yr 2035
]

result = amount_due(invoices, 90)
print(result)

 #in the for loop for invoice it goes to invoices[0] then it sends those parameters to the class Invoice
 #then it uses that data in the for loop to get the difference in days and adds the amount due
