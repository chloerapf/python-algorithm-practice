# keep asking until input is positive or != 0
while True:
    num = int(input('How many prices would you like to collect? '))
    if num != 0 and 0 < num <= 2147483647: 
        print('\nThanks, here we go!\n')
        break
    else:
        print('Must be positive, try again\n')

# start counters for report later on
subtotal = 0
savings = 0
positive_numbers = 0
negative_numbers = 0
for i in range(1, num + 1): # increment prices based on num above
    while True:
        price = int(input(f'Enter price #{i}: '))
        if price > 0: 
            subtotal += price
            positive_numbers += 1
            break # if valid break out and enter for loop to increment
        if price < 0:
            savings += price
            negative_numbers += 1
            break # if valid break out and enter for loop to increment
        if price == 0: # keep asking, stays in while loop until valid
            print('Prices cannot be zero. They must be positive or negative.\n')
# report
print()
print('--- Report ---')
print(f'Subtotal: {subtotal}') # subtota;
print(f'Savings: {savings * -1}') # savings
print(f'Grand Total: {subtotal - (savings * -1)}\n') # grand total
print(f'Average Item Price: {subtotal/positive_numbers:.2f}') # average price
print(f'Average Discount: {(savings * -1)/negative_numbers:.2f}') # average discount
