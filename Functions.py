def Calc_balance(income, expenses):
    print(f"\nThank you.\nYour total expenses are: ${expenses:.2f}")
    balance = income - expenses
    return balance

def financial_status(balance):
    if balance > 0:
        print("Great! You are saving money!\n:D")
    elif balance == 0:
        print("You are breaking even.\n:/")
    else:
        print("***WARNING***\nYou are overspending!!!\n:(")