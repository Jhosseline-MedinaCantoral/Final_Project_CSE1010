# Mini Project 10 Sample Version + Delete Feature
import os
os.system('cls' if os.name == 'nt' else 'clear')
import Functions
import Classes

username = input("Please enter your name: ")
print("Hello " + username + ", this is Budget-Buddy! Your personal budgeting assistant.")
print(f"Lets get started {username}!\n")

while True:
    try:
        income = float(input("Please enter your monthly income (NUMBERS ONLY): "))
        break
    except:
        print("***THERE WAS AN ERROR***\nPLEASE ENTER NUMBERS ONLY")

# ----------------------------------------

grocery = Classes.Budget('grocery')
grocery_expenses = grocery.add_expense()

car = Classes.Budget('car')
car_expenses = car.add_expense()

print()
grocery.get_expenses()
car.get_expenses()

grocery.expense_list()
car.expense_list()

grocery.delete_expense()
car.delete_expense()

grocery.write_to_file()
car.write_to_file()

total_expenses = grocery_expenses + car_expenses
balance = Functions.Calc_balance(income, total_expenses)
print(f"\nYour balance is ${balance:.2f}")
Functions.financial_status(balance)