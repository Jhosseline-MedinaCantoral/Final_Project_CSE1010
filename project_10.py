print("Hi there, this is BudgetBuddy! Your personal budget assistant.\n")

user_name = input("Enter your name: ")
print(f"{user_name}, welcome to BudgetBuddy!\n")

from library.classes_10 import Budget

# Income input
while True:
    try:
        income = float(input("Enter your total monthly income: "))
        if income <= 0:
            raise ValueError("Income must be positive.")
        break
    except ValueError:
        print("Wrong! Please enter a valid positive number for income.")

# Categories
car = Budget("Car")
car.add_expenses()

grocery = Budget("Grocery")
grocery.add_expenses()

# Display on screen
car.get_expense_details()
grocery.get_expense_details()

# Totals
total_spent = car.get_total() + grocery.get_total()
balance = income - total_spent

print(f"\nTotal Income: ${income:.2f}")
print(f"Total Spent: ${total_spent:.2f}")
print(f"Remaining Balance: ${balance:.2f}")

if balance > 0:
    print("Great! You are saving money!")
elif balance == 0:
    print("You are breaking even.")
else:
    print("**WARNING** You are overspending!")


