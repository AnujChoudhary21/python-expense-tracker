"""
Expense Tracker System

A simple expense tracking module that demonstrates:
- Working with lists and dictionaries
- Validation
- Exception handling
- Aggregation logic
"""


# -------------------------------------------------
# Simulated Database
# -------------------------------------------------

expenses = []


# -------------------------------------------------
# Add Expense Function
# -------------------------------------------------

def add_expense(amount: float, category: str, description: str) -> dict:
    """
    Add a new expense to the system.

    Args:
        amount (float): The expense amount (must be positive).
        category (str): The expense category.
        description (str): Short description of the expense.

    Returns:
        dict: The created expense dictionary.

    Raises:
        ValueError: If the amount is not greater than 0.
    """
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    return expense


# -------------------------------------------------
# Calculate Total Expenses
# -------------------------------------------------

def calculate_total_expenses() -> float:
    """
    Calculate the total of all expenses.

    Returns:
        float: Total amount of all expenses.
    """
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


# -------------------------------------------------
# Calculate Total by Category
# -------------------------------------------------

def calculate_total_by_category(category: str) -> float:
    """
    Calculate total expenses for a specific category.

    Args:
        category (str): The category to filter by.

    Returns:
        float: Total amount for that category.
    """
    total = 0

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]

    return total


# -------------------------------------------------
# Show All Expenses
# -------------------------------------------------

def show_expenses() -> None:
    """
    Display all stored expenses.

    Returns:
        None
    """
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nAll Expenses:")
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['category']} - "
            f"{expense['description']} : ${expense['amount']}"
        )


# -------------------------------------------------
# Testing Section
# -------------------------------------------------

def run_tests() -> None:
    """
    Execute example expense scenarios.
    """
    try:
        add_expense(50, "Food", "Groceries")
        add_expense(20, "Transport", "Taxi")
        add_expense(100, "Food", "Restaurant")
        add_expense(0, "Entertainment", "Cinema")  # Invalid example

    except ValueError as error:
        print("Error:", error)

    print("\nTotal Expenses:", calculate_total_expenses())
    print("Total Food Expenses:", calculate_total_by_category("Food"))

    show_expenses()


if __name__ == "__main__":
    run_tests()