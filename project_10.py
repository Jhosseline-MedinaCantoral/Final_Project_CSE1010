import os
os.system('cls' if os.name == 'nt' else 'clear')
import Functions
import Classes

username = input("Please enter your name:") 
print("Hello " + username + ", this is Budget-Buddy! Your personal budgeting assistant.") 
print(f"Lets get started {username}!\n")

while True:
    try:
        income = float(input ("Please enter your montlhy income (NUMBERS ONLY): "))
        break
    except:
        print("**THERE WAS AN ERROR***\nPLEASE ENTER NUMBERS ONLY")

grocery = Classes.Budget('grocery')
car = Classes.Budget('Car')

grocery_expenses = grocery.add_expense()
car_expenses = car.add_expense()

print()
grocery.get_expenses()
car.get_expenses()

grocery.expense_list()
car.expense_list()

grocery.write_to_file()
car.write_to_file()

total_expenses = grocery_expenses + car_expenses

delete_option = input("\nDo you want to DELETE AN ENTIRE CATEGORY? (yes/no): ")

if delete_option.lower() == "yes":
    print("\nWhich category?")
    print("1. Grocery")
    print("2. Car")
    cat = input("Enter category number: ")

    if cat == "1":
        grocery.delete_category()
    elif cat == "2":
        car.delete_category()
    else:
        print("Invalid category selected.")

balance = Functions.Calc_balance(income, total_expenses)
Functions.financial_status(balance)