import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# -------------------------
# Utility Functions
# -------------------------

def initialize_file():
    """Create CSV file if it doesn't exist"""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Name", "Amount", "Category"])

def add_expense():
    print("\nAdd New Expense")
    
    name = input("Expense name: ")
    
    try:
        amount = float(input("Amount (R): "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    category = input("Category (Food, Transport, Bills, etc.): ")
    date = datetime.now().strftime("%Y-%m-%d")
    
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, name, amount, category])
    
    print("Expense added successfully!")

def view_expenses():
    print("\nAll Expenses")
    
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return
    
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        
        expenses = list(reader)
        
        if not expenses:
            print("No expenses recorded yet.")
            return
        
        for i, row in enumerate(expenses, start=1):
            print(f"{i}. {row[0]} | {row[1]} | R{float(row[2]):.2f} | {row[3]}")

def total_spending():
    total = 0
    
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        
        for row in reader:
            total += float(row[2])
    
    print(f"\nTotal Spending: R{total:.2f}")

def monthly_summary():
    summary = {}
    
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        
        for row in reader:
            month = row[0][:7]  # YYYY-MM
            amount = float(row[2])
            
            if month in summary:
                summary[month] += amount
            else:
                summary[month] = amount
    
    print("\nMonthly Summary:")
    for month, total in summary.items():
        print(f"{month}: R{total:.2f}")

# -------------------------
# Main Menu
# -------------------------

def main():
    initialize_file()
    
    while True:
        print("\n====== Expense Tracker Pro ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spending")
        print("4. View Monthly Summary")
        print("5. Exit")
        
        choice = input("Choose option (1-5): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spending()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()