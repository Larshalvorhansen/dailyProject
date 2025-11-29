# Build a simple budget tracker that categorizes expenses and generates monthly summaries.
# Allow users to add transactions and view spending by category.


class Expense:
    def __init__(self, date, item, price, category):
        self.date = date
        self.item = item
        self.price = price
        self.category = category


def addExpense(day):
    new = input("Input expense: ")
    new = input("Input price: ")
    new = input("Input category: ")
    new = input("Input : ")


e1 = Expense(29, "kaffe", 45, "mat")

print(e1.date)
print(e1.category)
