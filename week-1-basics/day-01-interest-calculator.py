# Day 1: Simple and Compound Interest Calculator
# Problem: Calculate simple and compound interest for a given principal,
# rate and time period.

principal = 100000   # amount in rupees
rate = 8             # annual interest rate in percent
years = 5

simple_interest = (principal * rate * years) / 100
compound_amount = principal * (1 + rate / 100) ** years
compound_interest = compound_amount - principal

print(f"Principal: ₹{principal:,.2f}")
print(f"Simple Interest: ₹{simple_interest:,.2f}")
print(f"Compound Interest: ₹{compound_interest:,.2f}")
print(f"Difference: ₹{compound_interest - simple_interest:,.2f}")

# Learned: compound interest grows faster because interest is earned on interest.
