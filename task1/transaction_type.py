def handle_transaction_type(list_of_transaction_types):
    print("Choose What Type Of Transaction You Want To Make")
    
    for idx, type in enumerate(list_of_transaction_types):
        print(f"{idx + 1}: {type[:1].upper() + type[1:]}")
    
    type_of_transaction = input()
    
    while type_of_transaction.lower() not in list_of_transaction_types:
        print("Invalid Transaction")
        print("Here Is A List Of Available Transactions")
        
        for idx, type in enumerate(list_of_transaction_types):
            print(f"{idx + 1}: {type[:1].upper() + type[1:]}")
            
        type_of_transaction = input()
        
    return type_of_transaction.lower()