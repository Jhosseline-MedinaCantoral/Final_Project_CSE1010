# This is the See Expenses Option.
class See_Expenses_Option:
# Class for the "See Expenses" option
    def __init__(self, filename):           
    # initialize function with filename as parameter. Filename is the file where expenses are stored.
        self.expenses_file = filename
        # stores the expenses file as a variable to be used throughout the class.
    def display_expenses(self):
    # function to display expenses from the file
        try: 
        # try loop to prevent error message if file does not exist.
            with open(self.expenses_file, 'r') as file:
            # with loop to open the file in read mode only and to automaticly close file. 
                expenses_saved = file.read()
                #saves the entire txt file in one string variable
                print(expenses_saved)
                # prints the saved expenses to the user.
        except:
        # if an expenses file doesn't exist, this will run.
            print("!!ERROR!!\n No Saved Expenses Found")
        # after this it will hopefully terminate the code and return to main menu.

if __name__ == "__main__":

    option_chosen = See_Expenses_Option("test_data.txt")
    #tests file that exists
    option_chosen.display_expenses()

    option_chosen = See_Expenses_Option("data.txt")
    #tests file that doesn't exist
    option_chosen.display_expenses()

    # test to check if functions and class are working properly