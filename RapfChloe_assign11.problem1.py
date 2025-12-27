import random # import random to get random nums

from datetime import date # import today's date 

class Passenger: # class

    def __init__(self, first_name, last_name, meal_pref, birth_yr): # takes in these variables 

        self.first_name = first_name # assign to first name
        self.last_name = last_name # assign to last name 
        self.meal_pref = meal_pref # assign to meal pref
        self.birth_yr = int(birth_yr) # assign to birth year 

        passenger_id = '' # create empty string to store randon id numbers 
        for i in range(10): # iterate 10 times for a ten digit id 
            passenger_id += str(random.randint(1,9)) # turn into str so it will be concatenated and not added
            # we choose a random int between 1 and 9 and concatenate it onto the empty str
        passenger_id = int(passenger_id) # convert it to an integer once the iterations are done 

        self.passenger_id = passenger_id # assign to self

    def is_minor(self): # this function will return true if passenger is a minor 
        current_year = date.today().year # assign '2025' to current year 
        return (current_year - self.birth_yr) <= 18 # this is a boolean so it will return either 'True' or 'False'
                                                    # subtract passenger birth year from current year and compare it to int 18

    def get_full_name(self): # this function will concatenate the first and last name into a string and return it 
        return f'{self.first_name} {self.last_name}' # f string 

    def get_initials(self): # this function will index the zeroeth indice of the first and last name and concatenate them and return it 
        return self.first_name[0] + self.last_name[0]

class Coach: # class

    def __init__(self, sequence_num, rows, seats_per_row): # takes in these variables

        self.sequence_num = int(sequence_num) # convert to int
        self.rows = int(rows) # convert to int
        self.seats_per_row = int(seats_per_row) # convert to int 
        self.seating_chart = {} # create empty dic to store seating chart
        self.seat_by_passenger = {} # create another empty dict for passenger id mapping to seats
        self.valid_seats = [] # create list of valid seat letters
        for i in range(self.seats_per_row): # loop through seats
            letter = chr(ord("A") + i) # convert to ord, add i to get correct letter, then convert to chr  to get letter
            self.valid_seats.append(letter) # append to empty list 

    def minor_count(self): # this function will count the num of minors in a coach

        minor_count = 0 # set counter 
        for passenger in self.seating_chart.values(): # loop through passengers using values()
            if passenger.is_minor(): # call is_minor() function
                minor_count += 1 # if ture, increment
        return minor_count # return the value 

    def meal_count(self, meal_type): # this function will count the num of specific meals 

        meal_count = 0 # set counter
        for passenger in self.seating_chart.values(): # loop through passengers 
            if passenger.meal_pref == meal_type: # if passenger's meal pref is the same as the meal that the function takes in 
                meal_count += 1 # increment if true 
        return meal_count # return value 

    def add_passenger(self, passenger, row_num, seat_position): # this function adds a passenger after validating 

        if int(row_num) < 1 or int(row_num) > self.rows: # if row num is invalid 
            raise Exception('Invalid Seat Number') # raise exception 
        
        if seat_position not in self.valid_seats: # if none of the seats are in valid seats list
            raise Exception('Invalid Seat Number') # raise exception

        for p in self.seating_chart.values(): # loop through passengers
            if p.passenger_id == passenger.passenger_id: # check if ids match 
                raise Exception('Passenger already has an assigned seat') # if they do, raise exception
        
        seat = f'{row_num}{seat_position}' # assign to var 
        
        if seat in self.seating_chart: # if seat is in the seating chart
            raise Exception('Seat already occupied') # raise exception
        
        self.seating_chart[seat] = passenger # add to seating chart 
        self.seat_by_passenger[passenger.passenger_id] = seat # add to other seating chart 

    def get_passenger_for_seat(self, row_num, seat_position): # this function takes in seat and returns the passenger 

       if int(row_num) < 1 or int(row_num) > self.rows: # if invalid row num 
            raise Exception('Invalid Seat Number') # raise exception 

       if seat_position not in self.valid_seats: # if seat letter isnt in valid seats list 
           raise Exception('Invalid Seat Number') # raise exception

       seat = f'{row_num}{seat_position}' # assign to var 

       if seat in self.seating_chart: # if the seat is in seating chart
           return self.seating_chart[seat] # return the passenger
       else:
           return # otherwise return none 

    def get_seat_for_passenger(self, passenger_id): # This function takes in a passenger id and returns the seat

        if passenger_id in self.seat_by_passenger: # if passenger id is in this dict
            return self.seat_by_passenger[passenger_id] # return the seat
        else: # otherwise return nothing 
            return

    def get_meal_for_seat(self, row_num, seat_position): # this function takes in a seat and returns the meal 

        seat = f'{row_num}{seat_position}' # make seat 

        if int(row_num) < 1 or int(row_num) > self.rows: # validate row 
            raise Exception('Invalid Seat Number')

        if seat_position not in self.valid_seats: # validate seat letter
            raise Exception('Invalid Seat Number')

        if seat not in self.seating_chart: # if seat not in seating chart 
            return # do nothing 

        return self.seating_chart[seat].meal_pref # if valid, return meal pref for that seat 
        

    def print_seating_chart(self): # this function prints the seating chart 

        print('  ', end='')

        for h in self.valid_seats: # loop through letters 
            print(f'{h:<2}', end = ' ') # print them on the same line 
        print() # new line 
        for i in range(1, self.rows + 1): # iterate 1 through rows (including rows)
            print(i, end=' ') # print number 
            for j in self.valid_seats: # loop through letters again
                seat = f'{i}{j}'  # make seat var
                if seat in self.seating_chart: # if the seat is in seating chart 
                    print (self.seating_chart[seat].get_initials(), end = ' ') # print the initials for the seat
                else: # otherwise print '--'
                    print ('--', end = ' ')
            print() # new line 


class Train: # make class
    
    def __init__(self, first_class_num, standard_class_num, stops,
                 date, start_time): # takes in these vars 

        self.coaches = [] # create empty list for coaches 
        for i in range(1, first_class_num +1): # start from 1 up until last num (inclusive)
            self.coaches.append(Coach(i+1, 10, 3)) # call coach class and append first class coaches
        for i in range(first_class_num + 1, first_class_num + standard_class_num + 1): # do the same for standard 
            self.coaches.append(Coach(i+1, 14, 4))
        self.stops = stops # assign to stops 
        self.date = date # assign to date
        self.start_time = start_time # assign to time 

    
    def get_source(self): # this function takes in nothing but returns the origin 
        return self.stops[0] # index list at position zero

    def get_destination(self): # this functions takes in nothign but returns the destination 
        return self.stops[-1] # index list at last position using -1 

    def book_seat(self, passenger, sequence_num, row_num, seat_position): # this function books a seat for a passenger

        if sequence_num < 1 or sequence_num > len(self.coaches): # validate sequence num 
            raise Exception('Invalid Coach Sequence Number')

        for coach in self.coaches: # loop through coaches in list 
            if passenger.passenger_id in coach.seat_by_passenger: # if passenger's id is in this list 
                raise Exception('Passenger already has a seat') # raise exception

        coach = self.coaches[sequence_num -1] # get correct index by minusing one 

        coach.add_passenger(passenger, row_num, seat_position) # add passenger
        
    def cancel_booking(self, passenger): # this function will cancel a passenger's booking 

        for coach in self.coaches: # loop through the coaches list 

            if passenger.passenger_id in coach.seat_by_passenger: # is passenger's id is in coach 

                seat = coach.seat_by_passenger[passenger.passenger_id] # extract value (seat) using key

                del coach.seat_by_passenger[passenger.passenger_id] # delete seat from this list
                del coach.seating_chat[seat] # delete seat from this list

                return # return  nothing 

        return # return nothing if passenger doesnt exist

    def get_num_minors(self): # this function gets num of minors using the function we defined under coach 

        minors = 0 # set counter 

        for coach in self.coaches: # loop through coaches

            minors += coach.minor_count() # add counter to the num of minors in each coach 

        return minors # return that value 
                    
    def get_num_meals(self, meal_type): # this function gets num of specific meals from the function we defined under coach        

        meals = 0 # counter 

        for coach in self.coaches: # loop through coaches 

            meals += coach.meal_count(meal_type) # add counter to num of specific meals using function
                
        return meals # return that value

            

        

        
        
        

        



