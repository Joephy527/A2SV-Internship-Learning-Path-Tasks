from current_balance import get_current_balance
from transaction_type import handle_transaction_type
from process_transaction import process_transaction
from record_information import record_info
from check_budget_goals import analize_budget
from save_information import write_info
from transaction_time import get_time_of_transaction
from show_budget_chart import show_expenditure

def main():
    # Welcome Screen
    print("Welcome To Your Budget Tracker")
    print()
    
    # Declare Useful Variables
    list_of_transaction_types = ["income", "expense"]
    budget_goal = 200
    
    # Get Transaction Time
    date_of_transaction, time_of_transaction = get_time_of_transaction()
    
    # Get Needed Information From Modules
    latest_balance = get_current_balance()
    type_of_transaction = handle_transaction_type(list_of_transaction_types)
    transaction_category, transaction_amount = process_transaction(type_of_transaction)
    budget_tracker = record_info(latest_balance, date_of_transaction, time_of_transaction, type_of_transaction, transaction_category, transaction_amount)
    remaining_budget = int(budget_tracker[-1])
    
    # Save Transaction To Local File
    write_info(budget_tracker)
    
    # Analize Budget Goals
    analize_budget(remaining_budget, budget_goal, type_of_transaction)
    
    # Show Expenditure Chart
    if type_of_transaction == "expense":
        show_expenditure()

if __name__ == "__main__":
    main()