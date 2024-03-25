def analize_budget(remaining_budget, budget_goal, type_of_transaction):
        off_set = abs(budget_goal - remaining_budget)
        
        if type_of_transaction == "expense":
            if remaining_budget < budget_goal:
                print(f"You've Gone Over Budget By {off_set}")
            else:
                print("Congratulations For Keeping Your Expense Under Budget")
                print(f"You Have A Remaining Balance Of {remaining_budget}")
        else:
            if remaining_budget < budget_goal:
                print(f"You're Still Recovering From Your Last Expenses, Keep Saving")
            else:
                print(f"You Have A Remaining Balance Of {remaining_budget}")