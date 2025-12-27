# Chloe Rapf, 9/18/2025, Section 012

import random

# PART 1: Determine Problem Type
problem_type = input('What type of problem do you want to try? ADDITION, SUBTRACTION, MULTIPLICATION, EXPONENT or RANDOM? ')

# If Statements 
if problem_type == 'ADDITION':
    print('Selection Saved -', problem_type)
    print('Operator to use:', '+')
elif problem_type == 'SUBTRACTION':
    print('Selection Saved -', problem_type)
    print('Operator to use:', '-')
elif problem_type =='MULTIPLICATION':
    print('Selection Saved -', problem_type)
    print('Operator to use:', '*')
elif problem_type == 'EXPONENT':
    print('Selection Saved -', problem_type)
    print('Operator to use:', '**')
# If statement for RANDOM
elif problem_type == 'RANDOM':
    random_choice = random.randint(1,4)
    if random_choice == 1:
        problem_type = 'ADDITION'
        operator = '+'
    if random_choice == 2:
        problem_type = 'SUBTRACTION'
        operator = '-'
    if random_choice == 3:
        problem_type = 'MULTIPLICATION'
        operator = '*'
    if random_choice == 4:
        problem_type = 'EXPONENT'
        operator = '**'
    print('... we randomly selected', problem_type, 'as your random problem type')
    print('Operator to use:', operator, '\n')
# else statement for invalid choice 
else:
    print('Invalid choice, game will end now.')

# PART 2: Generate Random Problem
num1 = random.randint(1,10)
num2 = random.randint(1,10)
add_operator = '+'
sub_operator = '-'
mult_operator = '*'
exp_operator = '**'
if problem_type == 'ADDITION':
    print('Guess #1\nWhat is', num1, add_operator, num2, '?')
    answer = int(input('What is your answer? '))
    if answer == int(num1) + int(num2):
        print('You answered correctly on your first try!')
    else:
        print('You did NOT answer correctly on your first try.')
        # Guess 2 and Hint
        if answer < num1 + num2:
            print('Your answer was too LOW. Try a higher number next time.\n')
        elif answer > num1 + num2:
            print('Your answer was too HIGH. Try a lower number next time.\n')
        print('Guess #2\nWhat is', num1, add_operator, num2)
        answer = int(input('What is your answer? '))
        if answer == int(num1) + int(num2):
            print('You answered correctly on your second try!')
        # Guess 3 and Hint
        else:
            print('You did NOT answer correctly on your second try.')
            if answer < num1 + num2:
                print('Your answer was too LOW. Try a higher number next time.\n')
            elif answer > num1 + num2:
                print('Your answer was too HIGH. Try a lower number next time.\n')
            print('Guess #3\nWhat is', num1, add_operator, num2)
            answer = int(input('What is your answer? '))
            if answer == int(num1) + int(num2):
                print('You answered correctly on your third try!')
if problem_type == 'SUBTRACTION':
    print('Guess #1\nWhat is', num1, sub_operator, num2, '?')
    answer = int(input('What is your answer? '))
    if answer == int(num1) - int(num2):
        print('You answered correctly on your first try!')
    else:
        print('You did NOT answer correctly on your first try.')
        # Guess 2 and Hint
        if answer < num1 - num2:
            print('Your answer was too LOW. Try a higher number next time.\n')
        elif answer > num1 - num2:
            print('Your answer was too HIGH. Try a lower number next time.\n')
        print('Guess #2\nWhat is', num1, sub_operator, num2)
        answer = int(input('What is your answer? '))
        if answer == int(num1) - int(num2):
            print('You answered correctly on your second try!')
        # Guess 3 and Hint
        else:
            print('You did NOT answer correctly on your second try.')
            if answer < num1 - num2:
                print('Your answer was too LOW. Try a higher number next time.\n')
            elif answer > num1 - num2:
                print('Your answer was too HIGH. Try a lower number next time.\n')
            print('Guess #3\nWhat is', num1, sub_operator, num2)
            answer = int(input('What is your answer? '))
            if answer == int(num1) - int(num2):
                print('You answered correctly on your third try!')
if problem_type == 'MULTIPLICATION':
    print('Guess #1\nWhat is', num1, mult_operator, num2, '?')
    answer = int(input('What is your answer? '))
    if answer == int(num1) * int(num2):
        print('You answered correctly on your first try!')
    else:
        print('You did NOT answer correctly on your first try.')
        # Guess 2 and Hint
        if answer < num1 * num2:
            print('Your answer was too LOW. Try a higher number next time.\n')
        elif answer > num1 * num2:
            print('Your answer was too HIGH. Try a lower number next time.\n')
        print('Guess #2\nWhat is', num1, mult_operator, num2)
        answer = int(input('What is your answer? '))
        if answer == int(num1) * int(num2):
            print('You answered correctly on your second try!')
        # Guess #3 and Hint
        else:
            print('You did NOT answer correctly on your second try.')
            if answer < num1 * num2:
                print('Your answer was too LOW. Try a higher number next time.\n')
            elif answer > num1 * num2:
                print('Your answer was too HIGH. Try a lower number next time.\n')
            print('Guess #3\nWhat is', num1, mult_operator, num2)
            answer = int(input('What is your answer? '))
            if answer == int(num1) * int(num2):
                print('You answered correctly on your third try!')
if problem_type == 'EXPONENT':
    num2 = random.randint(1,3)
    print('Guess #1\nWhat is', num1, exp_operator, num2, '?')
    answer = int(input('What is your answer? '))
    if answer == int(num1) ** int(num2):
        print('You answered correctly on your first try!')
    else:
        print('You did NOT answer correctly on your first try.')
        # Guess 2 and Hint
        if answer < num1 ** num2:
            print('Your answer was too LOW. Try a higher number next time.\n')
        elif answer > num1 ** num2:
            print('Your answer was too HIGH. Try a lower number next time.\n')
        print('Guess #2\nWhat is', num1, exp_operator, num2)
        answer = int(input('What is your answer? '))
        if answer == int(num1) ** int(num2):
            print('You answered correctly on your second try!')
        # Guess 3 and Hint
        else:
            print('You did NOT answer correctly on your second try.')
            if answer < num1 ** num2:
                print('Your answer was too LOW. Try a higher number next time.\n')
            elif answer > num1 ** num2:
                print('Your answer was too HIGH. Try a lower number next time.\n')
            print('Guess #3\nWhat is', num1, exp_operator, num2)
            answer = int(input('What is your answer? '))
            if answer == int(num1) ** int(num2):
                print('You answered correctly on your third try!')
if problem_type == 'RANDOM':
    if random_choice == 1:
        operator = add_operator
        print('Guess #1\nWhat is', num1, operator, num2, '?')
        answer = int(input('What is your answer? '))
        if answer == int(num1) + int(num2):
            print('You answered correctly on your first try!')
    else:
        print('You did NOT answer correctly on your first try.')
        # Guess 2 and Hint 
        if answer < num1 + num2:
            print('Your answer was too LOW. Try a higher number next time.\n')
        elif answer > num1 + num2:
            print('Your answer was too HIGH. Try a lower number next time.\n')
        print('Guess #2\nWhat is', num1, operator, num2)
        answer = int(input('What is your answer? '))
        if answer == int(num1) + int(num2):
            print('You answered correctly on your second try!')
        # Guess 3 and Hint
        else:
            print('You did NOT answer correctly on your second try.')
            if answer < num1 + num2:
                print('Your answer was too LOW. Try a higher number next time.\n')
            elif answer > num1 + num2:
                print('Your answer was too HIGH. Try a lower number next time.\n')
            print('Guess #3\nWhat is', num1, operator, num2)
            answer = int(input('What is your answer? '))
            if answer == int(num1) + int(num2):
                print('You answered correctly on your third try!')
    if random_choice == 2:
        operator = sub_operator
        print('Guess #1\nWhat is', num1, operator, num2, '?')
        answer = int(input('What is your answer? '))
        if answer == int(num1) - int(num2):
            print('You answered correctly on your first try!')
        else:
            print('You did NOT answer correctly on your first try')
            # Guess 2 and Hint 
            if answer < num1 - num2:
                print('Your answer was too LOW. Try a higher number next time.\n')
            elif answer > num1 - num2:
                print('Your answer was too HIGH. Try a lower number next time.\n')
            print('Guess #2\nWhat is', num1, operator, num2)
            answer = int(input('What is your answer? '))
            if answer == int(num1) - int(num2):
                print('You answered correctly on your second try!')
            # Guess 3 and Hint
            else:
                print('You did NOT answer correctly on your second try.')
                if answer < num1 - num2:
                    print('Your answer was too LOW. Try a higher number next time.\n')
                elif answer > num1 - num2:
                    print('Your answer was too HIGH. Try a lower number next time.\n')
                print('Guess #3\nWhat is', num1, operator, num2)
                answer = int(input('What is your answer? '))
                if answer == int(num1) - int(num2):
                    print('You answered correctly on your third try!')
    if random_choice == 3:
        operator = mult_operator
        print('Guess #1\nWhat is', num1, operator, num2, '?')
        answer = int(input('What is your answer? '))
        if answer == int(num1) * int(num2):
            print('You answered correctly on your first try!')
        else:
            print('You did NOT answer correctly on your first try.')
            # Guess 2 and Hint
            if answer < num1 * num2:
                print('Your answer was too LOW. Try a higher number next time.\n')
            elif answer > num1 * num2:
                print('Your answer was too HIGH. Try a lower number next time.\n')
            print('Guess #2\nWhat is', num1, operator, num2)
            answer = int(input('What is your answer? '))
            if answer == int(num1) * int(num2):
                print('You answered correctly on your second try!')
            # Guess 3 and Hint
            else:
                print('You did NOT answer correctly on your second try.')
                if answer < num1 * num2:
                    print('Your answer was too LOW. Try a higher number next time.\n')
                elif answer > num1 * num2:
                    print('Your answer was too HIGH. Try a lower number next time.\n')
                print('Guess #3\nWhat is', num1, operator, num2)
                answer = int(input('What is your answer? '))
                if answer == int(num1) * int(num2):
                    print('You answered correctly on your third try!')
    if random_choice == 4:
        operator = exp_operator
        num2 = random.randint(1,3)
        print('Guess #1\nWhat is', num1, operator, num2, '?')
        answer = int(input('What is your answer? '))
        if answer == int(num1) ** int(num2):
            print('You answered correctly on your first try!')
        else:
            print('You did NOT answer correctly on your first try.')
            # Guess 2 and Hint
            if answer < num1 ** num2:
                print('Your answer was too LOW. Try a higher number next time.\n')
            elif answer > num1 ** num2:
                print('Your answer was too HIGH. Try a lower number next time.\n')
            print('Guess #2\nWhat is', num1, operator, num2)
            answer = int(input('What is your answer? '))
            if answer == int(num1) ** int(num2):
                print('You answered correctly on your second try!')
            # Guess 3 and Hint
            else:
                print('You did NOT answer correctly on your second try.')
                if answer < num1 ** num2:
                    print('Your answer was too LOW. Try a higher number next time.\n')
                elif answer > num1 ** num2:
                    print('Your answer was too HIGH. Try a lower number next time.\n')
                print('Guess #3\nWhat is', num1, operator, num2)
                answer = int(input('What is your answer? '))
                if answer == int(num1) ** int(num2):
                    print('You answered correctly on your third try!')
            
        


