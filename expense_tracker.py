import pandas as pd
import matplotlib.pyplot as plt
import os

file_exists = os.path.isfile('expenses.csv')

if file_exists:
    df = pd.read_csv('expenses.csv')
else:
    df = pd.DataFrame(columns=['Date', 'Category', 'Amount'])

def add_expense():
    date = input('Enter the date (YYYY-MM-DD): ')
    category = input('Enter the category: ')
    amount = float(input('Enter the amount: '))
    global df
    df = df.append({'Date': date, 'Category': category, 'Amount': amount}, ignore_index=True)
    df.to_csv('expenses.csv', index=False)
    print('Expense added successfully!')

def view_expenses():
    if df.empty:
        print('No expenses to display.')
    else:
        print(df)

def visualize_expenses():
    if df.empty:
        print('No expenses to visualize.')
    else:
        summary = df.groupby('Category')['Amount'].sum()
        summary.plot(kind='bar')
        plt.title('Expenses by Category')
        plt.xlabel('Category')
        plt.ylabel('Total Amount')
        plt.tight_layout()
        plt.show()

def main_menu():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Visualize Expenses")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            visualize_expenses()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main_menu()
