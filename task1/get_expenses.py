import csv
from collections import defaultdict

def get_all_expenses():
    expense_map = defaultdict(int)
    expenses, expense_amount = [], []
    
    with open('budget.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        for row in reader:
            if row[2] == "expense":
                expense_map[row[3]] -= int(row[-2])
                
        for expense in expense_map:
            expenses.append(expense)
            expense_amount.append(abs(expense_map[expense]))

    return (expenses, expense_amount)

if __name__ == "__main__":
    get_all_expenses()