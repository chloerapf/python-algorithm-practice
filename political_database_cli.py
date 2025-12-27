# lists
politicians = ["Joe Biden", "Diane Feinstein", "Anthony Blinken", "Kevin McCarthy"]
position = ["President", "Senator", "Secretary of State", "Representative"]
donations = [50000000, 10000000, 0, 20000000]
elections_won = [
  [2020, 2012, 2008, 2002, 1996, 1990, 1984, 1978, 1972],
  [2018, 2012, 2006, 2000, 1994, 1992],
  [],
  [2022, 2020, 2018, 2016, 2014, 2012, 2010, 2008, 2006]
]

while True: # enter a while loop, this will be the main loop
    print('\nWelcome to the Political Database!')
    user_input = input('(a)dd, (r)emove, (s)earch by name, search by (t)ype, (l)ist or (q)uit: ').lower() # ask user input

    if user_input == 'q': # if user wants to quit, then break out of the loop
        print('See you next time!')
        break
    
    elif user_input == 's': # if user wants to search
        user_search = input('Name of politician to search for: ').lower() # ask which politician to search for 

        found = False # initiate as false until politician is found
        for i in range(len(politicians)): # iterate through the indices
            if user_search == politicians[i].lower(): # if user's input matches one of the politicians
                print(f'{position[i]} {politicians[i]}') # then print the politician being search 
                print(f'{politicians[i]} has {donations[i]:,.2f} in donations.') # and their donations
                print(f'{politicians[i]} has won the following elections: ', end="") # and their elections

                years = elections_won[i] # index into the inner election list for that politician
                for j in range(len(years)): # iterate through the indices of that list
                    if j == len(years) - 1: # for the last year
                        print(years[j]) # dont print a comma, just the year
                    else:
                        print(f'{years[j]}, ', end='') # otherwise, print a comma after
                    
                found = True # found is now true, so break
                break

        if not found: # if we haven't found that politician, print this message
            print(f'We do not have any {user_search} in the Political Database')

    elif user_input == 'a': # if the user wants to add 
        temp_elections = [] # create empty list to store new elections 
        while True: # enter loop 
            new_politician = input('Enter name of new politician: ') # ask user for the name 
            parts = new_politician.split() # split the name into parts
            normalized = "" # create empty string 

            for i in range(len(parts)): # iterate through the indices of the parts of the name 
                word = parts[i] # set word equal to individual letters
                fixed = word[0].upper() + word[1:].lower() # the fixed name will capitalize the first letter
                
                if i == 0: # if it's the first part of the name 
                    normalized = fixed # normalized just becomes the fixed name   
                else: # if it's the last part of the name, just concatenate it onto the first part 
                    normalized += " " + fixed  

            new_politician = normalized # assign the revised name to the new politician var
            if new_politician in politicians: # check if the new guy is in the list already 
                print('Duplicate name, add operation cancelled') # if they are, print this message 
                continue # skip through the rest and go back up to top of loop 
            else: # if they're not, append and break
                politicians.append(new_politician)
                break

        while True: # enter a new loop to ask for new position
            new_position = input('What is the position of this politician: ')
            parts = new_position.split() # break into parts, same logic used for new politician
            normalized = "" # create empty string 
            if len(parts) >= 2 and parts[0].lower() == 'vice' and parts[1].lower() == 'president': # capitalize first and last for VP
                                                                                              
                normalized = 'Vice President'
            elif parts[0].lower() == 'president': # normalize for single words 
                normalized = 'President'
            elif parts[0].lower() == 'senator':
                normalized = 'Senator'
            elif parts[0].lower() == 'representative':
                normalized = 'Representative'
            elif parts[0].lower() == 'secretary': # "secretary", or secretary of <something>                                
                normalized = 'Secretary'
            if normalized == "": # if we never set normalized i.e. if the position is invalid, print this message
                print('Invalid, please try again.')
            else:
                position.append(new_position) # otherwise, append new name to position list and break
                break
            
        while True: # enter loop for donations
            new_donation = int(input('How many donations does the politician have, in dollars: '))
            if new_donation < 0: # validate data
                print('Invalid, please try again.')
            else:
                donations.append(new_donation) # if it's valid, append to donation list andbreak
                break
            
        while True: # enter loop for election
            new_elections = input('What elections has the politican won (type "end" to stop entering types): ')
            if new_elections.lower() == 'end': # if user types end, then break
                print('Added new politician!')
                break
            new_elections = int(new_elections) # convert to int 
            if new_elections > 2025: # must be less than or equal to current year
                print('Invalid - you cannot win elections in the future')
            else:
                temp_elections.append(new_elections) # append years to empty list 

        elections_won.append(temp_elections) # append empty list to election list 
                
    
    elif user_input == 'l': # if user types list 
        print(f'{"Name":<20}{"Position":>20}{"Donation Amount":>20}{"Elections Won":>20}') # print collumns 
        for i in range(len(politicians)):
            name = politicians[i] # set vars equal to the indices
            pos = position[i]
            don = f'{donations[i]:,.2f}'
            election = len(elections_won[i]) # set var equal to num of elections won 
            print(f'{name:<20}{pos:>20}{don:>20}{election:>20}') # print collumns 

    elif user_input == 't': # if user types 'type'
        user_year = input('Enter Election Year: ') # ask for election yr 
        year = int(user_year) # convert to int 
        
        matching_indices = [] # create empty list 
        for i in range(len(elections_won)): # iterate through 
            if year in elections_won[i]: # if year appears in elections won
                matching_indices.append(i) # append that indice to matching indice empty list 

        if len(matching_indices) == 0: # if there are no matches, print this message and continue 
            print('We have no politician that ran in that year in our database.')
            continue
        # otherwise print the chart using same logic as above 
        print(f'{"Name":<20}{"Position":>20}{"Donation Amount":>20}{"Elections Won":>20}') 
        for i in matching_indices:
            name = politicians[i]
            pos = position[i]
            don = f'{donations[i]:,.2f}'
            election = len(elections_won[i])
            print(f'{name:<20}{pos:>20}{don:>20}{election:>20}')

    elif user_input == 'r': # if user wants to remove 
        user_remove = input('Enter name of politician to remove: ')
        parts = user_remove.split() # split into parts create empty string 
        normalized = ""

        for i in range(len(parts)): # this is same logic as above 
            word = parts[i]
            fixed = word[0].upper() + word[1:].lower()
            
            if i == 0:
                normalized = fixed      
            else:
                normalized = normalized + " " + fixed  

        user_remove = normalized
        
        if user_remove in politicians: # check if the politician is in the list 
            index = politicians.index(user_remove) # find the index position of the politician to remove 
            del politicians[index] # delete politican from the list at their index
            del position[index] # same for position
            del donations[index] # same for their donations 
            del elections_won[index] # same for their elections
            print('Politician Removed.') # print this 
            
        else: # if politician is not in the list, print this 
            print('Politician not found, cannot remove.')
            

        
            
   
    else: # if user types anything other than: 'a', 'r', 't', 'l', 's', or 'q'
        print('Unknown command, please try again')

