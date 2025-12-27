sales_list = [] # create empty list to store values

day = 1 # initialize day var to start at 1

while True: # e=enter while loop to ask an arbitrary amount of times
    
    sale = input(f'Sales for day {day}: ') # ask user for sales and assign to var 'sales'
    
    if sale.lower() == 'done': # if user enters 'done', then break out of the loop 
        break
    
    if not sale.isdigit(): # Reject anything that isn't an integer: if the sale is not a digit, re-ask
        print('Sorry, that is not a valid integer. Please try again.')
        continue # skip rest of loop and go back up to top of loop

    sale = int(sale) # convert sale to an integer
    
    if sale <= 0: # if the integer sale is less than zero, re-ask
        print('Sales must be greater than 0. Please try again.')
        continue # skip rest of loop and go back up to top of loop to re-ask
    
    sales_list.append(sale) # at the end, concatenate all the sales to the empty list
    day += 1 # and increment the day

total = 0 # initialize total 

for i in range(len(sales_list)): # iterate through the sales list
    total += sales_list[i] # add each item in the list to var 'total'

sorted_list = sales_list[:] # create a copy of the list to use later
sorted_list.sort() # sort the list lowest to highest
high = sorted_list[-1] # find the highest value by indexing at the last position of the sorted list
low = sorted_list[0] # do the same for the lowest value 
high_day = sales_list.index(high) + 1 # use the original list to find the day of the highest value 
low_day = sales_list.index(low) + 1 # same for lowest value
# here, I add 1 to it because indexes start at zero. i.e. day 1 value is really at index zero, not index one

if len(sorted_list) % 2 == 0: # check if the list is an even length
    median1 = sorted_list[len(sorted_list) // 2] # if it is, half the length and find the index at that position
    median2 = sorted_list[(len(sorted_list) // 2) - 1] # find the index right next to it
    median = (median1 + median2) / 2 # add them together and divide by two
else: # if it's odd, just find the middle value 
    median = sorted_list[len(sorted_list) // 2]

#print statements
print('\n')
print(f'Total sales: {total}')
print(f'Average sales per day: {total/len(sales_list):.2f}') # format to two decimal places
print(f'Median sales day: {median}')
print(f'Highest sales day: {high} (day {high_day})')
print(f'Lowest sales day: {low} (day {low_day})')

    
