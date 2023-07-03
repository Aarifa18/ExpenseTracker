expenses =[]

def addExpense(amount, category):
    expense = {'amount':amount, 'category':category}
    expenses.append(expense)

def listExpenses():
    print("\nHere is a list of your expense:")
    print("---------------------")
    counter = 0
    for expense in expenses:
        print("#", counter," - ",expense['amount'], " - ", expense['category'])
        counter += 1
    print("\n\n")

def removeExpense():
    while True:
        listExpenses()
        print("What expense would you like to remove?")
        try:
            expenseToRemove = int(input("> "))
            del expenses[expenseToRemove]
            break
        except:
            print("Error. Please, try again")

def printMenu():
    print("Expense Tracker")
    print("Please choose from one of the option")
    print("1. Add a New Expense")
    print("2. Remove an Expense")
    print("3. List All Expense")
    print("4. Exit")

if __name__ == "__main__":
    while True:
        printMenu()
        option = input("> ")
        if (option == "1"):
            print("How much was this expense?")
            while True:
                try:
                    amount = input("> ")
                    break
                except:
                    print("Error")
            
            print("What category was this expense?")
            while True:
                try:
                    category = input("> ")
                    break
                except:
                    print("Error")
            addExpense(amount,category)
        elif (option == "2"):
            removeExpense()
        elif (option == "3"):
            listExpenses()
        elif (option == "4"):
            exit()
        else:
            print("Error")