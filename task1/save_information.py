import csv

def write_info(budget_tracker):
    with open('budget.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(budget_tracker)