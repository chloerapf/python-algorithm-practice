# keep askimg for valid data input (numpilots > 0)
while True: 
    numpilots = int(input('How many pilots are in your cohort? '))
    if numpilots > 0:
        break
    else:
        print('Invalid input. Please enter a positive integer only.\n')

# check for hyperspace
while True:
    yes_hyper = input('Are you training your pilots in HYPERSPACE NAVIGATION (yes/no)? ')
    if yes_hyper == 'yes' or yes_hyper == 'Yes' or yes_hyper == 'no' or yes_hyper == 'No':
        break
    else:
        print('Invalid input. Please enter "yes" or "no".\n')
        
# bombing runs data validation
while True:
    num_br = int(input('How many training exercises will you have for BOMBING RUNS? '))
    if num_br > 0:
        break
    else:
        print('Invalid input. Please enter a positive integer only.\n')

# space dogfighting data validation
while True:
    num_sd = int(input('How many training exercises will you have for SPACE DOGFIGHTING? '))
    if num_sd > 0:
        break
    else:
        print('Invalid input. Please enter a positive integer only.\n')

# manueverability data validation
while True:
    num_m = int(input('How many training exercises will you have for MANUEVERABILITY? '))
    if num_m > 0:
        break
    else:
        print('Invalid input. Please enter a positive integer only.\n')

# hyperspace data validation if hyperspace is being used
if yes_hyper == 'yes' or yes_hyper == 'Yes':
    while True:
        num_h = int(input('How many training exercises will you have for HYPERSPACE NAVIGATION? '))
        if num_h > 0:
            break
        else:
            print('Invalid input. Please enter a positive integer only.\n')

# check if user wants to drop lowest score
while True:
    yesno_drop = input('\nWould you like to drop the lowest test for each pilot? (yes/no): ')
    if yesno_drop == 'yes' or yesno_drop == 'no': # if yes or no check this condition
        if yesno_drop == 'yes': # if yes check this condition
            if num_br == 1 or num_sd == 1 or num_m == 1 or num_h == 1:
                print('Note that the lowest score will NOT be dropped for the following activities '
                      'because they only have 1 training exercise each:', end = ' ')
                if num_br == 1:
                    print('BOMBING RUNS', end = ' ')
                if num_sd == 1:
                    print('SPACE DOGFIGHTING', end = ' ')
                if num_m == 1:
                    print('MANUEVERABILITY', end = ' ')
                if yes_hyper == 'yes' or yes_hyper == 'Yes' and num_h == 1:
                    print('HYPERSPACE NAVIGATION', end = ' ')
                yesno_drop = 'no' # mode is 'no' for training exercises equal to one
        print('\nThanks, here we go!\n')
        break
    else:
        print('Invalid input. Please enter "yes" or "no".\n')

# cohort accumulator variables
cohort_bombing = 0
cohort_space = 0
cohort_maneuver = 0
cohort_hyper = 0

for pilot in range(1, numpilots + 1):
    print(f'\n*** Pilot #{pilot} ***')

# reset pilot totals
    bombing = 0
    lowest_b = None
    space = 0
    lowest_s = None
    manuever = 0
    lowest_m = None
    hyper = 0
    lowest_h = None

    for i in range(num_br):
        while True:
            bscore = float(input(f'Enter score for BOMBING RUNS exercise #{i + 1}: '))
            if bscore >= 0:
                bombing += bscore
                if lowest_b == None or bscore < lowest_b:
                    lowest_b = bscore
                break
            else:
                print('Score cannot be negative, try again.')
    for i in range(num_sd):
        while True:
            sscore = float(input(f'Enter score for SPACE DOGFIGHTING exercise #{i + 1}: '))
            if sscore >= 0:
                space += sscore
                if lowest_s == None or sscore < lowest_s:
                    lowest_s = sscore
                break
            else:
                print('Score cannot be negative, try again.')
    for i in range(num_m):
        while True:
            mscore = float(input(f'Enter score for MANUEVERABILITY exercise #{i + 1}: '))
            if mscore >= 0:
                manuever += mscore
                if lowest_m == None or mscore < lowest_m:
                    lowest_m = mscore
                break
            else:
                print('Score cannot be negative, try again.')
    if yes_hyper == 'yes' or yes_hyper == 'Yes':
        for i in range(num_h):
            while True:
                hscore = float(input(f'Enter score for HYPERSPACE NAVIGATION exercise #{i + 1}: '))
                if hscore >= 0:
                    hyper += hscore
                    if lowest_h == None or hscore < lowest_h:
                        lowest_h = hscore
                    break
                else:
                    print('Score cannot be negative, try again.')

    # averages
    if (yesno_drop == 'yes' or yesno_drop == 'Yes') and num_br > 1:
        bombing -= lowest_b
        b_average = bombing / (num_br - 1)
    else:
        b_average = bombing / num_br
    if yesno_drop == 'yes' and num_sd > 1:
        space -= lowest_s
        s_average = space / (num_sd - 1)
    else:
        s_average = space / num_sd

    if yesno_drop == 'yes' and num_m > 1:
        manuever -= lowest_m
        m_average = manuever / (num_m - 1)
    else:
        m_average = manuever / num_m

    if yes_hyper == 'yes' or yes_hyper == 'Yes':
        if yesno_drop == 'yes' and num_h > 1:
            hyper -= lowest_h
            h_average = hyper / (num_h - 1)
        else:
            h_average = hyper / num_h
    # add each pilot's averages to the cohort's totals
    cohort_bombing += b_average
    cohort_space += s_average
    cohort_maneuver += m_average
    if yes_hyper == 'yes' or yes_hyper == 'Yes':
        cohort_hyper += h_average

    # separate grades
    if b_average >= 90:
        b_grade = '(A)'
    elif 80 <= b_average < 90:
        b_grade = '(B)'
    elif 70 <= b_average < 80:
        b_grade = '(C)'
    elif 63 <= b_average < 70:
        b_grade = '(D)'
    else:
        b_grade = '(F)'

    if s_average >= 90:
        s_grade = '(A)'
    elif 80 <= s_average < 90:
        s_grade = '(B)'
    elif 70 <= s_average < 80:
        s_grade = '(C)'
    elif 63 <= s_average < 70:
        s_grade = '(D)'
    else:
        s_grade = '(F)'

    if m_average >= 90:
        m_grade = '(A)'
    elif 80 <= m_average < 90:
        m_grade = '(B)'
    elif 70 <= m_average < 80:
        m_grade = '(C)'
    elif 63 <= m_average < 70:
        m_grade = '(D)'
    else:
        m_grade = '(F)'

    if yes_hyper == 'yes' or yes_hyper == 'Yes':
        if h_average >= 90:
            h_grade = '(A)'
        elif 80 <= h_average < 90:
            h_grade = '(B)'
        elif 70 <= h_average < 80:
            h_grade = '(C)'
        elif 63 <= h_average < 70:
            h_grade = '(D)'
        else:
            h_grade = '(F)'

    print(f'\nPilot {pilot} received the following average scores:')
    print(f'BOMBING RUNS:       {b_average:.2f}{b_grade}')
    print(f'SPACE DOGFIGHTING:  {s_average:.2f}{s_grade}')
    print(f'MANUEVERABILITY:    {m_average:.2f}{m_grade}')
    if yes_hyper == 'yes' or yes_hyper == 'Yes':
        print(f'HYPERSPACE NAVIGATION: {h_average:.2f}{h_grade}')

cohort_b_avg = cohort_bombing / numpilots
cohort_s_avg = cohort_space / numpilots
cohort_m_avg = cohort_maneuver / numpilots
if yes_hyper == 'yes' or yes_hyper == 'Yes':
    cohort_h_avg = cohort_hyper / numpilots

# print final cohort report 
print('\n\n----- COHORT REPORT -----')
print('Overall averages for the cohort')
print(f'BOMBING RUNS:       {cohort_b_avg:.2f}')
print(f'SPACE DOGFIGHTING:  {cohort_s_avg:.2f}')
print(f'MANUEVERABILITY:    {cohort_m_avg:.2f}')
if yes_hyper == 'yes' or yes_hyper == 'Yes':
    print(f'HYPERSPACE NAVIGATION: {cohort_h_avg:.2f}')



