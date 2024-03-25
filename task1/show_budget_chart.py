import matplotlib.pyplot as plt

from get_expenses import get_all_expenses

def show_expenditure():
    # Get Plot Data
    expenses, expense_amount = get_all_expenses()
    
    plt.style.use("_mpl-gallery")
    
    fig, ax = plt.subplots()
    
    ax.bar(expenses, expense_amount, width=1, edgecolor="white", linewidth=0.7)
    
    ax.set(xlim=(0, len(expenses) + 10), ylim=(0, max(expense_amount) + 2000))
    
    plt.show()
    
if __name__ == "__main__":
    show_expenditure()