class Budget:
    def __init__(self, expense_type):
        self.expense_type = expense_type
        self.expenses = {}      # dictionary required by project instructions

    def add_expenses(self):
        """Collect expenses and store in dictionary format."""
        while True:
            try:
                num = int(input(f"How many {self.expense_type} expenses do you want to add? "))
                if num <= 0:
                    raise ValueError("Number of expenses must be greater than zero.")
                break
            except ValueError:
                print("Wrong! Please enter a valid positive integer.")

        for i in range(num):
            while True:
                try:
                    entry = input(
                        f"Enter {self.expense_type} expense #{i+1} "
                        f"(name and cost, e.g. 'gas 50'): "
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
                    self.expenses[name] = cost

                    print(f"Added → {name}: ${cost:.2f}")
                    break

                except ValueError as e:
                    print(f"! {e}")

        # after all expenses entered → write to file immediately
        self.write_to_file()

    def write_to_file(self):
        """Write expense data to a file named after the category."""
        filename = f"{self.expense_type.lower()}_expenses.txt"

        with open(filename, "w") as f:
            f.write(f"{self.expense_type}\n")
            for name, cost in self.expenses.items():
                f.write(f"{name} : ${cost:.2f}\n")

        print(f"\n✔ File saved: {filename}\n")

    def get_total(self):
        return sum(self.expenses.values())

    def get_expense_details(self):
        """Prints sorted or unsorted details to screen (not file)."""
        if not self.expenses:
            print(f"No {self.expense_type} expenses recorded.")
            return

        print("\nHow would you like to sort your expenses?")
        print("1. By cost (ascending)")
        print("2. By name (A–Z)")
        print("3. No sorting (as entered)")

        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            sorted_items = sorted(self.expenses.items(), key=lambda x: x[1])
            print(f"\n{self.expense_type} Expense Details (sorted by cost):")
        elif choice == "2":
            sorted_items = sorted(self.expenses.items(), key=lambda x: x[0].lower())
            print(f"\n{self.expense_type} Expense Details (sorted by name):")
        else:
            sorted_items = list(self.expenses.items())
            print(f"\n{self.expense_type} Expense Details (unsorted):")

        for i, (name, cost) in enumerate(sorted_items, start=1):
            print(f"{i}. {name} - ${cost:.2f}")

