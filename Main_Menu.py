import tkinter as tk
from Menu_Options import Menu_Options_Class
import os
os.system('cls' if os.name == 'nt' else 'clear')
import Menu_Options

username = input("Please enter your name:") 
print("Hello " + username + ", this is Budget-Buddy! Your personal budgeting assistant.") 
print(f"Lets get started {username}!\n")
while True:
    try:
        income = float(input ("Please enter your montlhy income (NUMBERS ONLY): "))
        break
    except:
        print("**THERE WAS AN ERROR***\nPLEASE ENTER NUMBERS ONLY")


#katie--------------------------------------------------------------------------
budget_buddy = Menu_Options_Class ()

menu = """
MENU
1 - To add expense
2 - To add expense to a type
3 - To delete expense type
4 - To delete expenses from a type
5 - To see all expenses
6 - Quit 
"""



while True:   
    print(menu)
    option = input("Choose an option:\n").strip()

    if option == "1":
        budget_buddy.Add_Expense_Type()

    elif option == "2":
        budget_buddy.Add_Expense()

    elif option == "3":
        budget_buddy.delete_expense_category()  
    
    elif option == "4":
        budget_buddy.delete_expense()

    elif option == "5":
        budget_buddy.See_Expenses()

    elif option == "6":
        print("Returning to main menu...\n")
        continue

    else:
        print("Invalid option. Please try again.\n")
