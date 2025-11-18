class Menu_Options:

    
    def __init__(self):
     self.expenses_dict = {}      # dictionary required by project instructions
     self.file_exists = False

#----------------------------------------------------------------------------#
    def Add_Expense_Type(self): # Jhoss
        try:
            with open("expense_file.txt", "r") as f:
                self.file_exists = True
        except:
            print("No save file found. A new file will be created upon saving expenses.")
        
        ans = "N"
        while ans == "N":
            # Collect expense category/type from user.
            print("Please enter the type/category of expense you want to add (Ex: Car, Grocery, Entertainment):")

            self.expense_type = input()
            print(f"You entered the expense type/category as: {self.expense_type}\nis that Correct? (Y/N)")

            while True:
                answer = input().upper()
                if answer == "Y":
                    print("Great! Adding Expense...")
                    ans = "Y"
                    break
                    
                
                elif answer == "N":
                    print("Understood,", end=" ")
                    break

                else: 
                    print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        
        with open('expense_file.txt', 'a') as f:
            
            if file_exists == True:
                print(f"{self.expense_type}:\n")
            
            elif file_exists == False:
                f.write(f"{self.expense_type}:\n")
                file_exists = True

#----------------------------------------------------------------------------#  
    def Add_Expense(self):    # Yijia & Jhoss
        try:
            with open("expenses_file.txt", 'r') as expenses_file:
                find_category = (expenses_file.readlines())
                print("Please choose from the following categories:")
                categories = []

            for line in find_category[:]:
                if line.strip().endswith(":"):
                    category = line.strip().rstrip(":")
                    print(f" {category}")
                while True:
                    try: 
                        self.expense_type = input("Please enter the category you want to add expenses to (as listed): ")
                        if self.expense_type not in categories:
                            raise ValueError
                        break
                    except:
                        print("That category was not found. Please try again.\n")
                
        except:
            print("No save file found. Returning to menu")
            return
            

        while True:
            try:
                num = int(input(f"How many {self.expense_type} expenses do you want to add? (Please Enter a Positive Integer) "))
                if num <= 0:
                    raise ValueError("Number of expenses must be greater than zero.")
                break
            except ValueError:
                print("**ERROR**\nPlease enter a valid positive integer.")

        for i in range(num):
            while True:
                try:
                    entry = input(
                        f"Enter {self.expense_type} expense #{i+1} "
                        f"(name and cost, e.g. 'item 50.00'): "
                    ).strip()

                    parts = entry.split()
                    if len(parts) < 2:
                        raise ValueError("Please include a name AND a cost.")

                    # last part is cost, everything before is name
                    *name_parts, cost_str = parts
                    name = " ".join(name_parts)
                    cost = float(cost_str)

                    if cost < 0:
                        raise ValueError("Expense cost cannot be negative.")

                    # Store exactly as dictionary required
                    self.expenses_dict[name] = cost

                    print(f"Added → {name}: ${cost:.2f}")
                    break

                except ValueError:
                    print("**ERROR**\nPlease enter a valid name and cost (e.g. 'item 50.00')")

        # after all expenses entered → write to file immediately
        """Write expense data to a file named after the category."""
        with open("expenses_file.txt", "r") as expenses_file:
            find_category = expenses_file.readlines()   
            for index, line in enumerate(find_category):
                if line.strip().endswith(":"):
                    find_category.insert(index+1, "2 New info here\n")            

        with open("expenses_file.txt", "w") as expenses_file:
            for name, cost in self.expenses_dict.items():                      
                expenses_file.write(f"{name} : ${cost:.2f}\n")

        print(f"\n✔ Changes saved\n")


#----------------------------------------------------------------------------#
    def get_total(self):
        return sum(self.expenses_dict.values())

  #----------------------------------------------------------------------------#  
    def See_Expenses(self): #Yijia
        try:
            with open("expense_file.txt", "r") as f:
                self.file_exists = True
        except:
            print("No save file found. Returning to menu.")
            return

        """Prints sorted or unsorted details to screen (not file)."""
        if not self.expenses_dict:
            print(f"No {self.expense_type} expenses recorded.")
            return

        print("\nHow would you like to sort your expenses?")
        print("1. By cost (ascending)")
        print("2. By name (A–Z)")
        print("3. No sorting (as entered)")

        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            sorted_items = sorted(self.expenses_dict.items(), key=lambda x: x[1])
            print(f"\n{self.expense_type} Expense Details (sorted by cost):")
        elif choice == "2":
            sorted_items = sorted(self.expenses_dict.items(), key=lambda x: x[0].lower())
            print(f"\n{self.expense_type} Expense Details (sorted by name):")
        else:
            sorted_items = list(self.expenses_dict.items())
            print(f"\n{self.expense_type} Expense Details (unsorted):")

        for i, (name, cost) in enumerate(sorted_items, start=1):
            print(f"{i}. {name} - ${cost:.2f}")

#----------------------------------------------------------------------------#
    def delete_expense(self):   #Emmanuel
        try:
            with open("expense_file.txt", "r") as f:
                self.file_exists = True
        except:
            print("No save file found. Returning to menu.")

         # NEW METHOD: DELETE AN EXPENSE
        if len(self.expenses_dict) == 0:
            print("\nThere are no expenses to delete.")
            return

        print(f"\nExpenses for {self.expense_type}:")
        expense_items = list(self.expenses_dict.items())

        for i, (item, cost) in enumerate(expense_items, 1):
            print(f"{i}. {item}: ${cost:.2f}")

        try:
            choice = int(input("Enter the number of the expense to delete: ")) - 1

            if 0 <= choice < len(expense_items):
                item_name = expense_items[choice][0]
                del self.expenses_dict[item_name]
                print(f"\nDeleted '{item_name}' successfully!\n")
            else:
                print("Invalid choice.")
        except:
            print("Please enter a valid number.")
        
        #MAKE SURE THAT CODE DELETS THE EXPENSES FROM THE EXPENESES_FILE AS WELL

#----------------------------------------------------------------------------#
    def delete_expense(self):   #Victoria
        '''Delete a specific expense from the budget category'''
        if not self.type_expense_dict:
            print(f"No expenses found for {self.expense_type}.")
            return
        
        print(f"\nCurrent expenses for {self.expense_type}:")
        for i, (expense_type, individual_expense) in enumerate(self.type_expense_dict.items(), 1):
            print(f"{i}. {expense_type}: ${individual_expense:.2f}")
        
        while True:
            try:
                choice = input("\nEnter the name of the expense you want to delete (or type 'cancel' to exit): ")
                if choice.lower() == 'cancel':
                    print("Deletion cancelled.")
                    return
                
                if choice in self.expenses_dict:
                    deleted_amount = self.expenses_dict[choice]
                    del self.expenses_dict[choice]
                    print(f"Successfully deleted '{choice}' with amount ${deleted_amount:.2f} from {self.expense_type}.")
                    return
                else:
                    print(f"Expense '{choice}' not found. Please enter a valid expense name.")
            except Exception as e:
                print(f"**THERE WAS AN ERROR**\nError: {e}")

             #MAKE SURE THAT CODE DELETES THE EXPENSES FROM THE EXPENESES_FILE AS WELL
