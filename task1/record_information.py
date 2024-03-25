def record_info(latest_balance, date_of_transaction, time_of_transaction, type_of_transaction, transaction_category, transaction_amount):
    budget_tracker = []
    final_balance = latest_balance + transaction_amount    

    budget_tracker.append(date_of_transaction)
    budget_tracker.append(time_of_transaction)
    budget_tracker.append(type_of_transaction)
    budget_tracker.append(transaction_category)
    budget_tracker.append(transaction_amount)
    budget_tracker.append(final_balance)
    
    return budget_tracker