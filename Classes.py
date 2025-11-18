class Budget:
    def __init__(self, expense_type):
        self.expense_type = expense_type
        self.type_expense_dict = {}

    def add_expense(self):
        while True:
            try:
                num_expenses = int(input(f"\nHow many expenses do you want to enter for {self.expense_type}? (INTEGER ONLY): "))
                break
            except:
                print("***ERROR*** Please enter an integer value.")

        print("\nEnter your expenses in 'Item Cost' format (Example: Milk 4.50)")
        for i in range(num_expenses):
            while True:
                try:
                    entry = input(f"Enter expense #{i+1}: ").split()
                    item = entry[0]
                    cost = float(entry[1])
                    self.type_expense_dict[item] = cost
                    break
                except:
                    print("***ERROR*** Please use this format: Item 4.50")

        return sum(self.type_expense_dict.values())

    def get_expenses(self):
        total = sum(self.type_expense_dict.values())
        print(f"\nTotal spent on {self.expense_type}: ${total:.2f}")

    def expense_list(self):
        if not self.type_expense_dict:
            print(f"\nNo expenses found in {self.expense_type}.")
            return

        print(f"\nExpenses in {self.expense_type}:")
        for item, amount in self.type_expense_dict.items():
            print(f"- {item}: ${amount:.2f}")

    #NEW — delete entire category
    def delete_category(self):
        if not self.type_expense_dict:
            print(f"\nNo expenses found in the {self.expense_type} category.")
            return

        print(f"\nWARNING: This will delete ALL expenses in '{self.expense_type}'!")

        confirm = input("Type 'YES' to delete everything, or anything else to cancel: ")

        if confirm.upper() == "YES":
            self.type_expense_dict.clear()
            print(f"\nAll expenses in '{self.expense_type}' have been deleted.")
        else:
            print("\nDeletion cancelled.")

    def write_to_file(self):
        with open("data.txt", "a") as data:
            data.write(f"\nEXPENSE CATEGORY: {self.expense_type}\n")
            for item, cost in self.type_expense_dict.items():
                data.write(f"{item}: ${cost:.2f}\n")
            data.write("----------------------------\n")