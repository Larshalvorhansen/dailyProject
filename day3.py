# Build a simple budget tracker that categorizes expenses and generates monthly summaries.
# Allow users to add transactions and view spending by category.

import csv

def collectExpenses(day):
    thing = input("what thing have you bouth? ")
    price = input("what price was it? ")
    category = input("waht category would you like to place it in? ")
    day = day 
    with open('expenses.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.

for days in range(1,31):
    collectExpenses(day)
