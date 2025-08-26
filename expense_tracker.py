import csv
from functools import reduce
from typing import List, Tuple


class ExpenseTracker:
    def __init__(self):
        self.expenses: List[Tuple[str, float]] = []

    def add_expense(self, expense_type: str, amount: float):
        self.expenses.append((expense_type, amount))

    def get_expenses(self) -> List[Tuple[str, float]]:
        return self.expenses

    def calculate_total(self) -> float:
        return reduce(lambda acc, exp: acc + exp[1], self.expenses, 0.0)

    def find_highest_expense(self) -> Tuple[str, float]:
        if not self.expenses:
            return ("", 0.0)
        return max(self.expenses, key=lambda x: x[1])

    def find_lowest_expense(self) -> Tuple[str, float]:
        if not self.expenses:
            return ("", 0.0)
        return min(self.expenses, key=lambda x: x[1])

    def calculate_average(self) -> float:
        if not self.expenses:
            return 0.0
        return self.calculate_total() / len(self.expenses)

    def category_totals(self) -> dict:
        totals = {}
        for category, amount in self.expenses:
            totals[category] = totals.get(category, 0) + amount
        return totals

    def print_summary(self):
        total = self.calculate_total()
        highest = self.find_highest_expense()
        lowest = self.find_lowest_expense()
        average = self.calculate_average()
        category_totals = self.category_totals()

        print("\nExpense Summary:")
        print(f"Total Expense: ${total:.2f}")
        print(f"Average Expense: ${average:.2f}")
        print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
        print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")
        print("Expenses by Category:")
        for cat, amt in category_totals.items():
            print(f"  {cat}: ${amt:.2f}")

    def export_to_csv(self, filename: str):
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Expense Type", "Amount"])
                for expense in self.expenses:
                    writer.writerow(expense)
            print(f"\nExpenses exported to '{filename}' successfully.")
        except Exception as e:
            print(f"Error writing to CSV file: {e}")


def get_user_date() -> str:
    while True:
        try:
            year = int(input("Enter the year (e.g., 2025): "))
            month = int(input("Enter the month (1-12): "))
            day = int(input("Enter the day (1-31): "))
            return f"{year:04d}-{month:02d}-{day:02d}"
        except ValueError:
            print("Invalid input. Please enter numeric values for year, month, and day.")


def get_user_expenses(tracker: ExpenseTracker):
    while True:
        expense_type = input("Enter the type of expense (or 'done' to finish): ").strip()
        if expense_type.lower() == 'done':
            break
        try:
            amount_str = input(f"Enter the amount for {expense_type}: ").strip()
            amount = float(amount_str)
            if amount < 0:
                print("Amount cannot be negative. Try again.")
                continue
            tracker.add_expense(expense_type, amount)
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")


def main():
    tracker = ExpenseTracker()
    date_str = get_user_date()
    get_user_expenses(tracker)

    if not tracker.get_expenses():
        print("No expenses entered.")
        return

    tracker.print_summary()

    filename = f"expenses_{date_str}.csv"
    tracker.export_to_csv(filename)


if __name__ == "__main__":
    main()