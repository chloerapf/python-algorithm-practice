# Chloe Rapf, 9/16/25, Section 012
# RapfChloe_assign2_problem1.py
# This code takes in a loan amount that will be repaid in 3 years. It then asks the user for the interest rate,
# and ticket sales details, then calculates how much principal and interest
# they pay each year and how much to charge per seat to cover costs. It outputs a formatted table and totals at the end.

# Initial Print Statements 
print('*' * 53)
print("     ", "3 Year Renovation Loan Repayment Forecast")
print('*' * 53)
print('This program will project how much to charge each year to pay down your loan.')
print('\n')

# Initial Inputs
cost_of_renovations = float(input('What is the cost of renovations (loan amount), in USD (i.e. 500000): '))
interest_rate = float(input("Next, enter the interest rate for the loan. For example, enter 5 for 5%: "))
num_seats = float(input("Next, enter the number of seats your theater has: "))
num_shows = float(input("Finally, enter the number of shows you will host this year: "))
print('\n')
year1_contribution = float(input("Enter your year 1 contribution towards your principal, in USD: "))
year2_contribution = float(input("Enter your year 2 contribution towards your principal, in USD: "))
year3_contribution = float(input("Enter your year 3 contribution towards your principal, in USD: "))
print('\n\n')

print('--- YOUR FORECAST ---')
print('\n')

# Calculations year1
year1_interest = interest_rate * cost_of_renovations / 100
year1_fee = (year1_interest + year1_contribution) / (num_seats * num_shows)

# Calculations year2
year2_starting_balance = cost_of_renovations - year1_contribution
year2_interest = interest_rate * year2_starting_balance / 100
year2_fee = (year2_interest + year2_contribution) / (num_seats * num_shows)

# Calculations year3
year3_starting_balance = cost_of_renovations - year1_contribution - year2_contribution
year3_interest = interest_rate * year3_starting_balance / 100
year3_fee = (year3_interest + year3_contribution) / (num_seats * num_shows)

# Balance & Total Interest
balance_3years = year3_starting_balance - year3_contribution
total_interest_paid = year1_interest + year2_interest + year3_interest

# Final Output
print("Year  Starting Balance   Principal Payment  Interest Payment  Fee per Sale")
print("1", "   ", f"{cost_of_renovations:,.2f}       {year1_contribution:,.2f}          {year1_interest:,.2f}         {year1_fee:,.2f}")
print("2", "   ", f"{year2_starting_balance:,.2f}         {year2_contribution:,.2f}          {year2_interest:,.2f}         {year2_fee:,.2f}")
print("3", "   ", f"{year3_starting_balance:,.2f}         {year3_contribution:,.2f}          {year3_interest:,.2f}         {year3_fee:,.2f}")
print('\n')
print(f"Balance after 3 years: {balance_3years:,.2f} USD")
print(f"Total Interest paid: {total_interest_paid: ,.2f} USD")
     
