# BudgetBuddy_FinalProject/main/project_final.py

from library.functions import Budget, financial_status, save_expenses, load_expenses
import matplotlib.pyplot as plt  # For visualizations

print("Welcome to BudgetBuddy!\n")

# Step 1: Get income
income = float(input("Enter your monthly income: "))

# Step 2: Load old expenses
budget = Budget()
loaded = load_expenses()
for item in loaded:
    budget.expenses.append(item)

# Step 3: Collect new expenses
while True:
    entry = input("Enter expense (Category Amount) or 'done' to finish: ")
    if entry.lower() == "done":
        break
    budget.add_expense(entry)

# Step 4: Show all expenses
print("\nYour expenses:")
budget.show_expenses()

# Step 5: Calculate balance
balance = income - budget.get_total()
print(f"\nYour total balance: ${balance:.2f}")
print(financial_status(balance))

# Step 6: Save expenses
save_expenses(budget.expenses)
print("\nExpenses saved to file.")

# Step 7: Optional visualization
if budget.expenses:
    categories = [cat for cat, _ in budget.expenses]
    amounts = [cost for _, cost in budget.expenses]

    plt.bar(categories, amounts, color="skyblue")
    plt.title("Monthly Expenses")
    plt.ylabel("Amount ($)")
    plt.show()
