def process_transaction(type_of_transaction):
    if type_of_transaction.lower() == "income":
        print("Please State Your Source Of Income")
        transaction_category = input()
        
        print("Enter Income Amount in ETB e.g(1000)")
        transaction_amount = int(input())
    else:
        print("Please State Where Your Expenditure Went")
        transaction_category = input()
        
        print("Enter Income Amount in ETB e.g(1000)")
        transaction_amount = -1 * int(input())
        
    return (transaction_category.lower(), transaction_amount)