import random

# get number of casses
while True:
    num_cases = int(input("How many cases are there?: "))
    if num_cases <= 0:
        print("Invalid number of cases, please enter a positive integer.")
    else:
        break

# get info for 10 appellate court judges
judge1_name = ""
judge2_name = ""
judge3_name = ""
judge4_name = ""
judge5_name = ""
judge6_name = ""
judge7_name = ""
judge8_name = ""
judge9_name = ""
judge10_name = ""

judge1_year = 0
judge2_year = 0
judge3_year = 0
judge4_year = 0
judge5_year = 0
judge6_year = 0
judge7_year = 0
judge8_year = 0
judge9_year = 0
judge10_year = 0

for i in range(1, 11):
    print(f"\nEnter Info for Appellate Court Judge #{i}")
    while True:
        name = input("Name: ")
        if name == "":
            print("Invalid input. Please enter at least one character for a name.")
        else:
            break
    while True:
        year = int(input("Start Year: "))
        if year < 0:
            print("Invalid year, please enter a positive integer.")
        else:
            break

    if i == 1:
        judge1_name = name
        judge1_year = year
    elif i == 2:
        judge2_name = name
        judge2_year = year
    elif i == 3:
        judge3_name = name
        judge3_year = year
    elif i == 4:
        judge4_name = name
        judge4_year = year
    elif i == 5:
        judge5_name = name
        judge5_year = year
    elif i == 6:
        judge6_name = name
        judge6_year = year
    elif i == 7:
        judge7_name = name
        judge7_year = year
    elif i == 8:
        judge8_name = name
        judge8_year = year
    elif i == 9:
        judge9_name = name
        judge9_year = year
    else:
        judge10_name = name
        judge10_year = year

# case panels 
print("\n*****************")
print("** CASE PANELS **")
print("*****************\n")

for c in range(1, num_cases + 1):

    # pick 3 unique random judges (numbers 1–10)
    j1 = random.randint(1, 10)
    j2 = random.randint(1, 10)
    while j2 == j1:
        j2 = random.randint(1, 10)
    j3 = random.randint(1, 10)
    while j3 == j1 or j3 == j2:
        j3 = random.randint(1, 10)

    # get names and years
    if j1 == 1:
        n1 = judge1_name
        y1 = judge1_year
    elif j1 == 2:
        n1 = judge2_name
        y1 = judge2_year
    elif j1 == 3:
        n1 = judge3_name
        y1 = judge3_year
    elif j1 == 4:
        n1 = judge4_name
        y1 = judge4_year
    elif j1 == 5:
        n1 = judge5_name
        y1 = judge5_year
    elif j1 == 6:
        n1 = judge6_name
        y1 = judge6_year
    elif j1 == 7:
        n1 = judge7_name
        y1 = judge7_year
    elif j1 == 8:
        n1 = judge8_name
        y1 = judge8_year
    elif j1 == 9:
        n1 = judge9_name
        y1 = judge9_year
    else:
        n1 = judge10_name
        y1 = judge10_year

    if j2 == 1:
        n2 = judge1_name
        y2 = judge1_year
    elif j2 == 2:
        n2 = judge2_name
        y2 = judge2_year
    elif j2 == 3:
        n2 = judge3_name
        y2 = judge3_year
    elif j2 == 4:
        n2 = judge4_name
        y2 = judge4_year
    elif j2 == 5:
        n2 = judge5_name
        y2 = judge5_year
    elif j2 == 6:
        n2 = judge6_name
        y2 = judge6_year
    elif j2 == 7:
        n2 = judge7_name
        y2 = judge7_year
    elif j2 == 8:
        n2 = judge8_name
        y2 = judge8_year
    elif j2 == 9:
        n2 = judge9_name
        y2 = judge9_year
    else:
        n2 = judge10_name
        y2 = judge10_year

    if j3 == 1:
        n3 = judge1_name
        y3 = judge1_year
    elif j3 == 2:
        n3 = judge2_name
        y3 = judge2_year
    elif j3 == 3:
        n3 = judge3_name
        y3 = judge3_year
    elif j3 == 4:
        n3 = judge4_name
        y3 = judge4_year
    elif j3 == 5:
        n3 = judge5_name
        y3 = judge5_year
    elif j3 == 6:
        n3 = judge6_name
        y3 = judge6_year
    elif j3 == 7:
        n3 = judge7_name
        y3 = judge7_year
    elif j3 == 8:
        n3 = judge8_name
        y3 = judge8_year
    elif j3 == 9:
        n3 = judge9_name
        y3 = judge9_year
    else:
        n3 = judge10_name
        y3 = judge10_year

    # determine chief justice (earliest start year = most senior)
    if y1 < y2 and y1 < y3:
        chief = n1
        assoc1 = n2
        assoc2 = n3
    elif y2 < y1 and y2 < y3:
        chief = n2
        assoc1 = n1
        assoc2 = n3
    elif y3 < y1 and y3 < y2:
        chief = n3
        assoc1 = n1
        assoc2 = n2
    else:
        # tie in seniority then pick random chief
        pick = random.randint(1, 3)
        if pick == 1:
            chief = n1
            assoc1 = n2
            assoc2 = n3
        elif pick == 2:
            chief = n2
            assoc1 = n1
            assoc2 = n3
        else:
            chief = n3
            assoc1 = n1
            assoc2 = n2

    # print results
    print(f"** Case {c} Justices **\n")
    print(f"Chief Justice: {chief}")
    print(f"Associate Justices: {assoc1}, {assoc2}\n")
