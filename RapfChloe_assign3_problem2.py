# Chloe Rapf, 09/24/2025, Section 012

# First, ask user to supply a date
date = int(input('Enter a date (MMDDYYYY): '))

# Extract year, month, and date
year = date % 10000
month = date // 1000000
day = (date // 10000) % 100


# Determine if leap year
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, 'is a leap year')
elif year % 100 == 0:
        print(year, 'is NOT a leap year')
else:
    print(year, 'is NOT a leap year')

    
# Determind if combo valid
if month == 9 or month == 4 or month == 6 or month == 11:
    if 0 < day <= 30:
        valid_date = True 
# Attach English label
        if day == 1 or day == 21 or day == 31:
            day = f'{day}st'
        elif day == 2 or day == 22:
            day = f'{day}nd'
        elif day == 3 or day == 23:
            day = f'{day}rd'
        else:
            day = f'{day}th'

# Assign Month Variables
        if month == 9:
            month = 'September'
        elif month == 4:
            month = 'April'
        elif month == 6:
            month = 'June'
        elif month == 11:
            month = 'November'
            
        print(month, day, year, 'is a valid date')
    else:
        print('This is not a valid date in', year)
        valid_date = False
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if 0 < day <= 31:
        valid_date = True 
# Attach english label
        if day == 1 or day == 21 or day == 31:
            day = f'{day}st'
        elif day == 2 or day == 22:
            day = f'{day}nd'
        elif day == 3 or day == 23:
            day = f'{day}rd'
        else:
            day = f'{day}th'
# Assign month variables
        if month == 1:
            month = 'January'
        elif month == 3:
            month = 'March'
        elif month == 5:
            month = 'May'
        elif month == 7:
            month = 'July'
        elif month == 8:
            month = 'August'
        elif month == 10:
            month = 'October'
        elif month == 12:
            month = 'December'
        print(month, day, year, 'is a valid date')
    else:
        print('This is not a valid date in', year)
        valid_date = False
elif month == 2:
    if year % 4 == 0 or year % 400 == 0:
            if 0 < day <= 29:
                valid_date= True 
# Attach english label
                if day == 1 or day == 21 or day == 31:
                    day = f'{day}st'
                elif day == 2 or day == 22:
                    day = f'{day}nd'
                elif day == 3 or day == 23:
                    day = f'{day}rd'
                else:
                    day = f'{day}th'
# Assign month variables
                if month == 2:
                    month = 'February' 
                print(month, day, year, 'is a valid date')
            else:
                print('This is not a valid date in', year)
                valid_date = False
    else:
        if 0 < day <= 28:
            valid_date = True 
# Attach english label
            if day == 1 or day == 21 or day == 31:
                day = f'{day}st'
            elif day == 2 or day == 22:
                day = f'{day}nd'
            elif day == 3 or day == 23:
                day = f'{day}rd'
            else:
                day = f'{day}th'
# Attach month variables
            if month == 2:
                month = 'February'
            print(month, day, year, 'is a valid date')
        else:
            print('This is not a valid date in', year)
            valid_date = False
else:
    print('This is not a valid date in', year)
    valid_date = False

# Re-assign day variable to numeric value for determining season
day = (date // 10000) % 100

# Re-assign month variables back to numbers
month = date // 1000000

# Determine season
if valid_date:
    location = input('Where are you located (N)orthern Hemisphere, (S)outhern Hemisphere or (E)quatorial Area? ')
    # Northern Hem
    if location == 'N' or location == 'n':
        if month == 12 or month == 1 or month == 2:
            if month == 2:
                if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                    if 0 < day <= 29:
                        print('The season on this date is WINTER')
                else:
                    if 0 < day <= 28:
                    
                        print('The season on this date is WINTER')
            else:
                if 0 < day <= 31:
                
                    print('The season on this date is WINTER')
        elif month == 3 or month == 4 or month == 5:
            if 0 < day <= 31:
            
                print('The season on this date is SPRING')
        elif month == 6 or month == 7 or month == 8:
            if 0 < day <= 31:
            
                print('The season on this date is SUMMER')
        elif month == 9 or month == 10 or month == 11:
            if 0 < day <= 30:
            
                print('The season on this date is FALL')
# Southern Hem
    elif location == 'S' or location == 's':
        if month == 12 or month == 1 or month == 2:
            if month == 2:
                if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                    if 0 < day <= 29:
                        season = 'SUMMER'
                        print('The season on this date is', season)
                else:
                    if 0 < day <= 28:
                        season = 'SUMMER'
                        print('The season on this date is', season)
            else:
                if 0 < day <= 31:
                    season = 'SUMMER'
                    print('The season on this date is', season)
        elif month == 3 or month == 4 or month == 5:
            if 0 < day <= 31:
                season = 'FALL'
                print('The season on this date is', season)
        elif month == 6 or month == 7 or month == 8:
            if 0 < day <= 31:
                season = 'WINTER'
                print('The season on this date is', season)
        elif month == 9 or month == 10 or month == 11:
            if 0 < day <= 30:
                season = 'SPRING'
                print('The season on this date is', season)

# Equatorial Area
    elif location == 'E' or location == 'e':
        if month == 12 or month == 1 or month == 2 or month == 6 or month == 7 or month == 8:
            if month == 2:
                if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                    if 0 < day <= 29: 
                        season = 'WET SEASON'
                        print('The season on this date is', season)
                else:
                    if 0 < day <= 28:
                        season = 'WET SEASON'
                        print('The season on this date is', season)
            else:       
                 if 0 < day <= 31:
                     season = 'WET SEASON'
                     print('The season on this date is', season)
        elif month == 3 or month == 4 or month == 5 or month == 9 or month == 10 or month == 11:
            if 0 < day <= 31:
                season = 'DRY SEASON'
                print('The season on this date is', season)

    else:
        print("Invalid entry, cannot determine season")




