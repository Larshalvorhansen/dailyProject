# Write a function that calculates compound interest over time with configurable rates and periods.
# Include options for different compounding frequencies (daily, monthly, yearly).

# A = P(1 + r/n)^nt


def compoundInterest(principal, rate, period, option):
    n = 1
    if option == "daily":
        n = 365.25
    elif option == "monthly":
        n = 12
    elif option == "yearly":
        n = 1
    else:
        return "please insert a valid option either daily, monthly or yearly"
    return principal * (1 + (rate / n)) ** (n * period)


print(compoundInterest(1, 1, 1, "jdfks"))
print(compoundInterest(1, 1, 1, "daily"))
print(compoundInterest(1, 1, 1, "monthly"))
print(compoundInterest(1, 1, 1, "yearly"))

# All cases pass. Complete;)
