import json

EXPENSE_FILE = "expenses.json"

def load_expenses():
    try:
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(description, amount, category):
    expenses = load_expenses()
    expenses.append({"description": description, "amount": amount, "category": category})
    save_expenses(expenses)
    print("Expense added!")

if __name__ == "__main__":
    desc = input("Enter expense description: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    add_expense(desc, amount, category)
