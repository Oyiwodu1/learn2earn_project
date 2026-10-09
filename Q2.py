items = [2, 4, 6] 
result = [] 
for item in items: 
    if item % 4 == 0: 
        continue 
    result.append(item * 2) 
print(result)


def borrow(resource, quantity):
    if quantity <= 0:
        return "Quantity must be positive"

    if quantity > resource["available"]:
        return "Not enough stock"

    resource["available"] -= quantity
    return "Success"


transactions = [
    {"fellow": "Ada", "quantity": 2},
    {"fellow": "John", "quantity": 4},
    {"fellow": "Ada", "quantity": 3},
    {"fellow": "Grace", "quantity": 1},
    {"fellow": "John", "quantity": 2}
]

def total_per_fellow(transactions):
    totals = {}
    for transaction in transactions:
        fellow = transaction["fellow"]
        quantity = transaction["quantity"]
        if fellow not in totals:
            totals[fellow] = 0
        totals[fellow] += quantity
    return totals

print(total_per_fellow(transactions))


