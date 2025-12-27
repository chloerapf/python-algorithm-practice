



while True: # enter a while loop so that the user is trapped until username is valid
    upper = 0 # initialize 
    lower = 0
    error = 0
    num_digit = 0 
    username = input('Enter a username: ') # prompt user 
    first_char = username[0] # assign first char to var 
    last_char = username[-1] # assign last char to var 
    if 6 <= len(username) <= 12: # check if username is between 6 and 12
        print(f'* Length of username: {len(username)}')
        
   
    else:
        print(f'* Length of username: {len(username)}') # print length
        print('  ERROR - username must be between 6 and 12 characters long')
        error += 1 # if not between 6 and 12, then print error and increment error

    if username.isalnum(): # check if username is alpha-numeric and print result 
        print(f'* All characters are alphabetic or numeric: {username.isalnum()}')
    else:
        print(f'* All characters are alphabetic or numeric: {username.isalnum()}')
        print('  ERROR - must only have digits, or uppercase or lowercase characters')
        error += 1 # if not, print error and increment error 
        
    if first_char.isdigit(): # check if first char is a digit and print result 
        print(f'* First character is a digit: {first_char.isdigit()}')
        print('  ERROR - first character cannot be a digit')
        error += 1 # if it is, print error and increment 
    else:
        print(f'* First character is a digit: {first_char.isdigit()}')
    if last_char.isdigit(): # check if last char is a digit and print result 
        print(f'* Last character is a digit: {last_char.isdigit()}')
        print('  ERROR - last character cannot be a digit')
        error += 1 # if it is, print error and increment 
    else:
        print(f'* Last character is a digit: {last_char.isdigit()}')
    for char in username: # enter for loop to count upper, lower, and digit characters 
        if char.isupper(): # if char is a uppercase, increment upper var by one 
            upper += 1
        if char.isdigit(): # if char is a digit, increment digit var by one 
            num_digit += 1
        if char.islower(): # if char is lowercase, icrement lower var by one 
            lower += 1
    print(f'* # of uppercase characters: {upper}') # print result 
    if upper < 2: # if num of upper char is less than two, print error and increment 
        print('  ERROR - username must contain at least two uppercase characters')
        error += 1
    print(f'* # of lowercase characters: {lower}')
    if lower < 2: # same for lower 
        print('  ERROR - username must contain at least two lowercase characters')
        error += 1
  
    print(f'* # of digit characters: {num_digit}') # print num of dig characters
    if error > 0: # if there are any errors, re-ask the user for a valid username 
        print('Username is not valid, please try again\n')
        continue
    else: # otherwise, tell user that username is a valid and break out of loop 
        print('Username is valid!')
        break

        
while True: # enter a new loop for password 
    p_upper = 0 # initialize new vars 
    p_lower = 0
    p_num_dig = 0
    special_char = 0
    p_error = 0
    invalid_char = 0
    allowed_char = '!@#$%&' # store allowed special chars in a var 
    password = input('\nEnter a password: ') # ask user for password and store in a var 
    if len(password) >= 10: # if its greater than or equal to 10, print result and move on 
        print(f'* Length of password: {len(password)}')
    else: # otherwise print error and increment
        print(f'* Length of password: {len(password)}')
        print('  ERROR - password must be at least 10 characters long')
        p_error += 1

    if username.lower() in password.lower(): # compare lowercase username to lowercase password to compare on same level
        print(f'* Username is part of password: {username.lower() in password.lower()}')
        print('  ERROR - username cannot exist within password')
        p_error += 1 # if they exist within each other, than print error and increment 
    else:
        print(f'* Username is part of password: {username in password}')
    for char in password: # enter a for loop to count upper, lower, digit, special, and invalid chars 
        if char.isupper(): # if char is upper, increment upper var by one 
            p_upper += 1
        if char.islower(): # if char is lower, increment lower var by one 
            p_lower += 1
        if char.isdigit(): # if char is a digit, increment digit var by one 
            p_num_dig += 1
        if '#' in char: # check for special chars in char and increment if they exist 
            special_char += 1
        if '$' in char:
            special_char += 1
        if '%' in char:
            special_char += 1
        if '@' in char:
            special_char += 1
        if '&' in char:
            special_char += 1
        if '!' in char:
            special_char += 1
        if not (char.isalnum() or char in allowed_char): # any other type of char gets filtered through this condition and is marked as invalid 
            invalid_char += 1
    print(f'* # of uppercase characters in the password: {p_upper}') # print result 
    if p_upper < 2:
        print('  ERROR - password must contain at least two uppercase characters') # if num of upper chars is less than two, print and increment 
        p_error += 1
    print(f'* # of lowercase charaters in the password: {p_lower}')
    if p_lower < 2:
        print('  ERROR - password must contain at least two lowercase characters') # same for lower 
        p_error += 1
    print(f'* # of digit characters in the password: {p_num_dig}') # same for digit 
    if p_num_dig < 2:
        print('  ERROR - password must contain at least two digit characters')
        p_error += 1
    print(f'* # of special characters in the password: {special_char}') # same for special chars
    if special_char < 2:
        print('  ERROR - password must contain at least two special characters')
        p_error += 1 
    print(f'* # of invalid characters in the password: {invalid_char}') # same for invalid chars but dont print error 
    if invalid_char >= 1:
        p_error += 1
    if p_error > 0: # if there are any errors, then re-ask and re-enter loop
        print('Password is not valid, please try again')
    else: # otherwise, user is done!
        print('Password is valid!')
        break 
    
    


