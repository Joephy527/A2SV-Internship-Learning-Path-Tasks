import csv

def get_current_balance():
    with open('budget.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        latest_budget = {}
        latest_balance = 0
        
        for row in reader:
            latest_budget = row
        
        if not latest_budget:
            print("Enter Income or Expenses and Start Tracking Your Budget")
        else:
            latest_balance = latest_budget["balance"]
            
            print(f"Your Current Balance is: {latest_balance}")
            
        return int(latest_balance)
    
if __name__ == "__main__":
    get_current_balance()