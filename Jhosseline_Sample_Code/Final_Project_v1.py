#First version of Final project. 
# Jhosseline Medina's Version of Mini Project 10
#This is mereley for reference. 

import os
os.system('cls' if os.name == 'nt' else 'clear')
import Functions

username = input("Please enter your name:") 
print("Hello " + username + ", this is Budget-Buddy! Your personal budgeting assistant.") 
print(f"Lets get started {username}!\n")
while True:
    try:
        income = float(input ("Please enter your montlhy income (NUMBERS ONLY): "))
        break
    except:
        print("**THERE WAS AN ERROR***\nPLEASE ENTER NUMBERS ONLY")

#------------------------------------------------------------------------------#
import Classes

grocery = Classes.Budget('grocery')
grocery_expenses = grocery.add_expense()

car = Classes.Budget('Car')
car_expenses = car.add_expense()

print()
grocery.get_expenses()
car.get_expenses()

grocery.expense_list()
car.expense_list()

grocery.write_to_file()
car.write_to_file()

total_expenses = grocery_expenses + car_expenses
balance = Functions.Calc_balance(income,total_expenses)
print(f"\nYour balance is ${balance:.2f}")
Functions.financial_status(balance)