# Classes.py

class Budget:
    def __init__(self, expense_type):
        self.expense_type = expense_type
        self.type_expense_dict = {}

    def add_expense(self):
        while True:
            try:
                num_expenses = int(input(f"\nHow many expenses do you wish to enter for {self.expense_type}? (INTEGER ONLY): "))
                break
            except:
                print("***THERE WAS AN ERROR***\nPLEASE ENTER INTEGERS ONLY.")

        print("Enter your expenses in 'Type Cost' format (EXAMPLE: Item 10.00)")
        for i in range(num_expenses):
            while True:
                try:
                    type_expense, individual_expense = input(f"Enter expense #{i+1}: ").split()
                    self.type_expense_dict[type_expense] = float(individual_expense)
                    break
                except:
                    print("***THERE WAS AN ERROR***\nPLEASE ENTER IN THE INSTRUCTED FORMAT.")

        return sum(self.type_expense_dict.values())

    def get_expenses(self):
        print(f"\nTotal money you spent on ({self.expense_type}) is ${sum(self.type_expense_dict.values()):.2f}")

    def expense_list(self):
        print(f"\nThe items you spent money on ({self.expense_type}) are:")
        for expense_type, individual_expense in self.type_expense_dict.items():
            print(f"{expense_type}: ${individual_expense:.2f}")

    # NEW METHOD: DELETE AN EXPENSE
    def delete_expense(self):
        if len(self.type_expense_dict) == 0:
            print("\nThere are no expenses to delete.")
            return

        print(f"\nExpenses for {self.expense_type}:")
        expense_items = list(self.type_expense_dict.items())

        for i, (item, cost) in enumerate(expense_items, 1):
            print(f"{i}. {item}: ${cost:.2f}")

        try:
            choice = int(input("Enter the number of the expense to delete: ")) - 1

            if 0 <= choice < len(expense_items):
                item_name = expense_items[choice][0]
                del self.type_expense_dict[item_name]
                print(f"\nDeleted '{item_name}' successfully!\n")
            else:
                print("Invalid choice.")
        except:
            print("Please enter a valid number.")

    def write_to_file(self):
        with open("data.txt", "a") as data:
            data.write(self.expense_type)
            data.write("\n")
            for expense_type, individual_expense in self.type_expense_dict.items():
                data.write(f"{expense_type}: ${individual_expense:.2f}\n")
            data.write("\n")