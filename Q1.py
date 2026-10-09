resources = [
  {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
  {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
  {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]

fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []

print("welcome to Learn2earn lend")

def view_resource():
    for resource in resources:
        print()
        print(f'ID: {resource["id"]}')
        print(f'Name: {resource["name"]}')
        print(f'Category: {resource["category"]}')
        print(f'Total: {resource["total"]}')
        print(f'available: {resource["available"]}')

def add_resource():
    resource_id = input("Enter Resource ID of what you need: ").upper()
    for resource in resources:
        if resource_id == resource["id"]:
            print("ID FOUND")
            return
    name = input("Enter Resource name: ").title()
    category = input("Enter Resource Category: ").title()
    try:
        total = int(input("Enter Resource total: "))
        if total <= 0:
            print("Total must be greater than 0")
        else:
            available = total
            new_resource = {
                "id": resource_id,
                "name": name,
                "category": category,
                "total": total,
                "available": available
            }
            resources.append(new_resource)
            print("Resource added successfully!")
            print(new_resource)
    except ValueError:
        print("Please enter a valid number")

def borrow_resource():
    fellow_id = input("Enter Fellow ID: ").upper()
    if fellow_id in fellows:
        print(f"Welcome {fellows[fellow_id]}")
        resource_id = input("Enter Resource ID: ").upper()
        for resource in resources:
            if resource_id == resource["id"]:
                print(f'Available resource: {resource["name"]}, Quantity: {resource["available"]}')
                try:
                    quantity = int(input("Enter quantity to borrow: "))
                except ValueError:
                    print("Please enter a valid whole number!")
                    return
                if quantity <= 0 or quantity > resource["available"]:
                    print("Not available")
                else:
                    resource["available"] -= quantity
                    print(f'Quantity left: {resource["available"]}')
                    borrow_record = {
                        "fellow_id": fellow_id,
                        "resource_id": resource_id,
                        "stock": resource["name"],
                        "quantity": quantity
                    }
                    borrow_records.append(borrow_record)
                    print("Borrowing successful!")
                    print(borrow_record)
                break
        else:
            print("Resource ID not found")
    else:
        print("Fellow ID not found!")

def return_resource():
    fellow_id = input("Enter fellow ID: ").upper()
    if fellow_id in fellows:
        resource_id = input("Enter resource ID of what you want to return: ").upper()
        for record in borrow_records:
            if record["fellow_id"] == fellow_id and record["resource_id"] == resource_id:
                print("Borrowing record found")
                try:
                    quantity = int(input("Enter quantity to return: "))
                except ValueError:
                    print("Please enter a valid whole number!")
                    return
                if quantity <= 0 or quantity > record["quantity"]:
                    print("Invalid return quantity")
                else:
                    record["quantity"] -= quantity
                    remaining = record["quantity"]
                    for resource in resources:
                        if resource["id"] == resource_id:
                            resource["available"] += quantity
                            print("Return successful")
                            print(f"Quantity still borrowed: {remaining}")
                            break
                    if remaining == 0:
                        borrow_records.remove(record)
                return
        else:
            print("No borrowing record found")
    else:
        print("Fellow ID not found")

def search_resource():
    resource_name = input("Enter resource name: ").lower()
    for resource in resources:
        if resource_name == resource["name"].lower():
            print(f'ID: {resource["id"]}')
            print(f'Name: {resource["name"]}')
            print(f'Category: {resource["category"]}')
            print(f'Total: {resource["total"]}')
            print(f'Available: {resource["available"]}')
            break
    else:
        print("Resource not found!")

def filter_category():
    category_name = input("Enter category: ").lower()
    found = False
    for resource in resources:
        if category_name == resource["category"].lower():
            print(f'ID: {resource["id"]}')
            print(f'Name: {resource["name"]}')
            print(f'Available: {resource["available"]}')
            found = True
    if not found:
        print("Category not found!")

def reports():
    total_units = sum(resource["total"] for resource in resources)
    available_units = sum(resource["available"] for resource in resources)
    borrowed_units = total_units - available_units
    print("\n--- INVENTORY REPORT ---")
    print(f"Total units: {total_units}")
    print(f"Available units: {available_units}")
    print(f"Currently borrowed: {borrowed_units}")
    print("\nResources with fewer than 3 available:")
    found = False
    for resource in resources:
        if resource["available"] < 3:
            print(f'{resource["name"]}: {resource["available"]} available')
            found = True
    if not found:
        print("No resources have fewer than 3 available.")
    borrowed_by_resource = {}
    for record in borrow_records:
        resource_id = record["resource_id"]
        borrowed_by_resource[resource_id] = borrowed_by_resource.get(resource_id, 0) + record["quantity"]
    if borrowed_by_resource:
        most_borrowed = max(borrowed_by_resource.values())
        print("\nMost borrowed resource(s):")
        for resource_id, quantity in borrowed_by_resource.items():
            if quantity == most_borrowed:
                for resource in resources:
                    if resource["id"] == resource_id:
                        print(f'{resource["name"]}: {quantity} borrowed')
                        break
    else:
        print("\nNo resources have been borrowed yet.")

def main_menu():
    while True:
        print("\n===== LEARN2EARN LEND =====")
        print("1. View resources")
        print("2. Add resource")
        print("3. Borrow resource")
        print("4. Return resource")
        print("5. Search resource")
        print("6. Filter by category")
        print("7. View reports")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_resource()
        elif choice == "2":
            add_resource()
        elif choice == "3":
            borrow_resource()
        elif choice == "4":
            return_resource()
        elif choice == "5":
            search_resource()
        elif choice == "6":
            filter_category()
        elif choice == "7":
            reports()
        elif choice == "8":
            print("Thank you for using Learn2Earn Lend!")
            break
        else:
            print("Invalid choice. Please choose 1-8.")
main_menu()