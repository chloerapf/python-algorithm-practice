##########
# PART 1 #
##########

def minimum(a, b): # define function
    if a < b: # check if first argument is smaller than second
        return a # if condition is true, only return first argument
    else: # otherwise, return second argument
        return b

smallest = minimum(5, 6) # call function
print(smallest) # print result

##########
# PART 2 #
##########

def maximum(a, b): # define function
    small_num = minimum(a, b) # assign var to smallest argument using minimum function
    if small_num < b: # check if var is smaller than second argument
        return b # if condition is true, return second argument
    else: # otherwise return first argument
        return a

biggest = maximum(5, 6) # call
print(biggest) # print

##########
# PART 3 #
##########

def growth(a, b): # define
    growth_percentage = (a * (b/100)) + a # math (find b percent of a and add to a)
    return int(growth_percentage) # return int version

num = growth(100, 8) # call
print(num) # print

##########
# PART 4 #
##########

def calculate_bill(a, b, c): # define function 
    subtotal = 0 # set accumulate vars
    lowvalue = 0
    highvalue = 0
    
    for item in range(1, a + 1): # start for loop, it will go through numbers 1 to number of items(inclusive)
        
        while True: # keep user trapped until data is valid
            
            price = float(input(f'Item {item}: $')) # ask for item price and assign to var 'price'
            if price <= 0: # check for valid data
                print('Sorry, prices must be positive. Please try again.') # print this and then go back to top of while loop and re-ask
            else: # if valid data...
                subtotal += price # update subtotal variable: subtotal is added to price
                if lowvalue == 0: # check if lowvalue is equal to zero (which it is, first round)
                    lowvalue = price # if condition is true, lowvalue becomes price
                else:
                    lowvalue = minimum(lowvalue, price) # otherwise call minimum function to pick lowest value and assign to var 'lowvalue'
                if highvalue == 0: # same procedure for highvalue...
                    highvalue = price
                else:
                    highvalue = maximum(highvalue, price)
                break # break out of loop and move on to next number in range

    subtotaltax_cents = ((subtotal * (b/100)) + subtotal) % 1 # keep cents from subtotal plus tax since growth() will return an int value and cut those off
    subtotaltaxtip_cents = (((subtotal * (b/100)) + subtotal) * (c/100) + ((subtotal * (b/100)) + subtotal)) % 1 # same here

    subtotal_tax = growth(subtotal, b) # calculate subtotal plus tax using growth()
    subtotal_tax_tip = growth(subtotal_tax, c) # calculate subtotal plus tax and top using growth()

    # print statements
    print(f'\nHighest Value Item: ${highvalue:.2f}') 
    print(f'Lowest Value Item: ${lowvalue:.2f}\n')
    print(f'Subtotal: {subtotal:.2f}')
    print(f'After Tax Total: ${subtotal_tax + subtotaltax_cents:.2f}') # concatenate cents from subtotaltax_cents
    print(f'After Tax + Tip Total: ${subtotal_tax_tip + subtotaltaxtip_cents:.2f}') # same here but from subtotaltaxtip_cents

calculate_bill(3, 8, 20) # call function!

        
    

