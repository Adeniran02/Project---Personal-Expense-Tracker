# Importing our important libraries for this projejct
import csv
import os
from tabulate import tabulate

# creating our csv text file to store user's expense inputs for this program
file_name = "expenses.csv"

# Let's create a structure to store user's expense inputs in the expense file created
if not os.path.exists(file_name):
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Description"])


# This is a function that let users add and store expenses into the expense csv file
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    amount = input("Enter an amount: ")
    category = input("Enter category (Food, Data, Transport, Bills, etc): ")
    description = input("Enter description: ")

    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("Expense added successfully!\n")

# This is the function that let users review or check their expense sheet.
def view_expenses():
    with open(file_name, mode="r") as file:
        reader = csv.reader(file)
        data = list(reader)
        if len(data) > 1:
            print(tabulate(data, headers="firstrows", tablefmt="grid"))
        else:
            print("No expenses recorded yet.\n")

# This is the function that let users update or edit an expense incase of an error
def edit_expense():
    view_expenses() # This shows the user's current data
    try:
        edit_row = int(input("Enter the row number to edit (starting from 1): "))
    except ValueError:
        print("Invalid Input. Must be a number")
        return
    
    with open(file_name, mode="r") as file:
        reader = list(csv.reader(file))
    
    if 1 <= edit_row < len(reader):
        print("Current Data", reader[edit_row])
        new_date = input("Enter a new date (leave blank to keep current): ")
        new_amount = input("Enter a new amount (leave blank to keep current): ")
        new_category = input("Enter a new category (leave blank to keep current): ")
        new_description = input("Enter a new description (leave blank to keep current): ")

        if new_date:
            reader[edit_row][0] = new_date
        if new_amount:
            reader[edit_row][1] = new_amount
        if new_category:
            reader[edit_row][2] = new_category
        if new_description:
            reader[edit_row][3] = new_description

        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(reader)
        
        print("Expense Updated Successfully!\n")
    else:
        print("Invalid row selected.\n")

# This is the function that let users delete or remove a wrong or an outdated expense
def delete_expense():
    view_expenses() # This shows the user's current expenses/data

    try:
        delete_row = int(input("Enter row to delete (starting from 1): "))
    except ValueError:
        print("Invalid input. Must be a number")
        return
    
    with open(file_name, mode="r") as file:
        reader = list(csv.reader(file))

    if 1<= delete_row < len(reader):
        deleted = reader.pop(delete_row)
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(reader)
        print(f"Deleted Expense: {deleted}\n")
    else:
        print("Invalid row selected.\n")


# This is the main function of the code where we embed all of the functions above to put into use.
def main():
    while True:
        print("\nExpense Tracker") 
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Exit Program")


        try:
            choice = int(input("Select an Option: "))

            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expenses()
            elif choice == 3:
                edit_expense()
            elif choice == 4:
                delete_expense()
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid Selection, Please try again\n")
        except ValueError:
            print("Invalid Input. Please enter a number (1,2,3,4 or 5).\n")

if __name__ == "__main__":
    main()



