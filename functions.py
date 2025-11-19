# BudgetBuddy_FinalProject/library/functions.py

# ----- Budget class -----
class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, entry):
        """Accepts input like 'Grocery 50'"""
        try:
            category, cost = entry.split()
            cost = float(cost)
            self.expenses.append((category, cost))
        except ValueError:
            print("Invalid format! Use 'Category Amount'.")

    def get_total(self):
        return sum(cost for _, cost in self.expenses)

    def show_expenses(self):
        for category, cost in self.expenses:
            print(f"{category}: ${cost:.2f}")

# ----- Functions -----
def calc_balance(income, expenses):
    return income - sum(expenses)

def financial_status(balance):
    if balance > 0:
        return "Great! You are saving money!"
    elif balance == 0:
        return "You are breaking even."
    else:
        return "WARNING: You are overspending!"

def save_expenses(expenses, filename="data/expenses.csv"):
    with open(filename, "w") as file:
        for category, cost in expenses:
            file.write(f"{category},{cost}\n")

def load_expenses(filename="data/expenses.csv"):
    loaded = []
    try:
        with open(filename, "r") as file:
            for line in file:
                category, cost = line.strip().split(",")
                loaded.append((category, float(cost)))
    except FileNotFoundError:
        pass
    return loaded
