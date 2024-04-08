categories = ["Groceries", "Utilities", "Entertainment"]

def add_expense():
    try:
        expense = float(input("Enter expense: "))
    except ValueError:
        print("Please enter a number.")
        return
    
    item = input("Enter item name: ")

    print("Select a category:")
    for i, category in enumerate(categories):
        print(f"{i+1}. {category}")
    category_index = int(input("Enter category number: ")) - 1
    category_name = categories[category_index]
    
    with open("expenses.txt", "a") as file:
        file.write(f"{category_name}: ${expense}, {item}\n")

while True:
    add_expense()