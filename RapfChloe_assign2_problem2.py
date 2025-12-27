# Chloe Rapf, 9/17/2025, Section 012
# RapfChloe_assgin2_problem2.py
# The program takes two 4-digit numbers, breaks them into digits,
# displays the digits and a simple visual graph of repeated digits
# in four columns, and then performs a few concatenations and addition operations

# Initial Input 
first_num = int(input("Enter a 4 digit number between 0000 and 9999: "))
second_num = int(input("Enter a 4 digit number between 0000 and 9999: "))

# Isolation
first_num_ones = first_num % 10
first_num_tens = (first_num // 10) % 10
first_num_hundreds = (first_num // 100) % 10
first_num_thousands = (first_num // 1000) % 10

second_num_ones = second_num % 10
second_num_tens = (second_num // 10) % 10
second_num_hundreds = (second_num // 100) % 10
second_num_thousands = (second_num // 1000) % 10

print()

# Returning Digits
print("Digits in the 1's places:     ", first_num_ones, "and", second_num_ones)
print("Digits in the 10's places:    ", first_num_tens, "and", second_num_tens)
print("Digits in the 100's places:   ", first_num_hundreds, 'and', second_num_hundreds)
print("Digits in the 1000's places:  ", first_num_thousands, 'and', second_num_thousands)

print()

# Graphical Representation
print("    Graphical representation of your numbers")
print()
print("Thousands    Hundreds     Tens         Ones")


# Thousands
if first_num_thousands > 0:
    print(str(first_num_thousands) * first_num_thousands, end=" " * (12 - first_num_thousands))
else:
    print(" " * 12, end="")

# Hundreds
if first_num_hundreds > 0:
    print(str(first_num_hundreds) * first_num_hundreds, end=" " * (12 - first_num_hundreds))
else:
    print(" " * 12, end="")

# Tens
if first_num_tens > 0:
    print(str(first_num_tens) * first_num_tens, end=" " * (12 - first_num_tens))
else:
    print(" " * 12, end="")

# Ones
if first_num_ones > 0:
    print(str(first_num_ones) * first_num_ones)
else:
    print(" " * 12)

# Second Number 
# Thousands
if second_num_thousands > 0:
    print(str(second_num_thousands) * second_num_thousands, end=" " * (12 - second_num_thousands))
else:
    print(" " * 12, end="")

# Hundreds
if second_num_hundreds > 0:
    print(str(second_num_hundreds) * second_num_hundreds, end=" " * (12 - second_num_hundreds))
else:
    print(" " * 12, end="")

# Tens
if second_num_tens > 0:
    print(str(second_num_tens) * second_num_tens, end=" " * (12 - second_num_tens))
else:
    print(" " * 12, end="")

# Ones
if second_num_ones > 0:
    print(str(second_num_ones) * second_num_ones)
else:
    print(" " * 12)

print()
# Super Number
print("Computing Your Super Number!")
print()
print('Step #1: Add Each Place Value')
thousands = first_num_thousands + second_num_thousands
hundreds = first_num_hundreds + second_num_hundreds
tens = first_num_tens + second_num_tens
ones = first_num_ones + second_num_ones
print('- Thousands:', first_num_thousands, '+', second_num_thousands, '=', thousands)
print('- Hundreds: ', first_num_hundreds, '+', second_num_hundreds, '=', hundreds)
print('- Tens:     ', first_num_tens, '+', second_num_tens, '=', tens)
print('- Ones:     ', first_num_ones, '+', second_num_ones, '=', ones)
print()
# Combine New Values
print('Step #2: Combine New Values')
print('-', thousands, '+', hundreds, '+', tens, '+', ones, '=',
      str(thousands)+str(hundreds)+str(tens)+str(ones))
new_values = str(thousands)+str(hundreds)+str(tens)+str(ones)
print()
# Sum of All Digits
print('Step #3: Compute The Sum of ALL Digits in First Number')
print('-', first_num_thousands, '+', first_num_hundreds, '+', first_num_tens, '+',
     first_num_ones, '+', '=', first_num_thousands + first_num_hundreds + first_num_tens
     + first_num_ones)
print()
print('Step #4: Compute The Sum of ALL Digits in Second Number')
print('-', second_num_thousands, '+', second_num_hundreds, '+', second_num_tens, '+',
     second_num_ones, '+', '=', second_num_thousands + second_num_hundreds + second_num_tens
     + second_num_ones)
sum_of_all_second_digits = second_num_thousands + second_num_hundreds + second_num_tens + second_num_ones
sum_of_all_first_digits = (first_num_thousands + first_num_hundreds + first_num_tens + first_num_ones)
print()
# Combine Numbers in Order
print('Step #5: Combine The Numbers In This Order -- Step 4 + Step 2 + Step 3')
print('-', str(sum_of_all_second_digits) + str(new_values) + str(sum_of_all_first_digits))

