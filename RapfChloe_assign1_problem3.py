# Problem 3
# Language: Python
# This code asks the user to enter three names.
# It then displays those names back in several different formats and orders.
# Chloe, 09/06/2025, 012, RapfChloe_assign1_problem3.py


# Inputs
name_1 = input("Please enter name #1: ")
name_2 = input("Please enter name #2: ")
name_3 = input("Please enter name #3: ")

# Opening Print Statement
print("\nHere are your names in every possible order:")
print('-' * 44, "\n")

# First Print Statement
print("1. ", end='')
print(name_1, name_2, name_3, sep=', ', end='\n\n')

# Second Print Statement
print("2. ", end='***')
print(name_2, name_3, sep='*** ***', end='*** ***')
print(name_1, '\n', sep='***')

# Third Print Statement
print("3. ", end='')
print(name_2, name_1, name_3, sep='--', end='\n\n')

# Fourth Print Statement
print("4.", name_1)
print(name_3, name_2, sep='\n', end='\n\n')

# Fifth Print Statement
print("5.", name_3)
print("   ", name_2, "!!", sep='')
print('  ', name_1, "\n")

# Sixth Print Statement
print("6. ", name_3, sep='--')
print("   ", "----", name_1, sep='')
print("   ", "------", name_2, sep='')
