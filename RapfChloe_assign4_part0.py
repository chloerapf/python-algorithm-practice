# Ensure first number is positive 
num1 = int(input("Number 1: "))
while num1 <= 0:
    print("Invalid, try again")
    num1 = int(input("Number 1: "))

# Ensure second number is positive and larger than the first
num2 = int(input("Number 2: "))
while num2 <= 0 or num2 <= num1:
    print("Invalid, try again")
    num2 = int(input("Number 2: "))

# Top half of star formation, increasing
for i in range(num1, num2 + 1):
    spaces = num2 - i
    print(i, " " * spaces + "*" * i)

# Bottom half of star formation, decreasing
for i in range(num2 - 1, num1 - 1, -1):
    spaces = num2 - i
    print(i, " " * spaces + "*" * i)
