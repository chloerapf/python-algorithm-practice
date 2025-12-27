# Chloe Rapf, 9/16/2025, Section 012
# RapfChloe_assign2_problem0.py
# This code prompts the user for the total amount won, then performs a number
# of calculations returning the total amount won, the amount each person is due,
# the taxes dues on each share, and how much each person takes home

# Initial Input 
total_amount_won = float(input("How much money did you win? "))
winnings_split = float(input("How many people are splitting the winnings? "))
tax_rate = float(input("What is the tax rate on lottery winnings? (i.e. 25 means 25%)"))
print('\n')
# Calculations
split_winnings = total_amount_won / winnings_split
taxes_owed = total_amount_won * tax_rate / 100 / winnings_split
post_taxes = split_winnings - taxes_owed
# Output
print(f"Your total winnings are {total_amount_won:,.2f} USD")
print(f"Split between 4 people, that amounts to {split_winnings:,.2f} USD each")
print(f"Taxes owed per person: {taxes_owed:,.2f} USD")
print(f"Post-tax winnings per person: {post_taxes:,.2f} USD")
