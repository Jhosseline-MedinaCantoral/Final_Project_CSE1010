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

main_menu = Menu_Options.Main_Menu(income)s
