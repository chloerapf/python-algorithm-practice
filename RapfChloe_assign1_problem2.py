# Problem 2
# Language: Python
# This program stores four test scores, a student's first name and last name,
# bonus points, class name, average score, and average score with bonus points
# into different variables. It then displays those variables to the user, and
# calculates average score and average score with bonus points.
# Chloe Rapf, 09/05/2025, 012, RapfChloe_assign1_problem2.py

# Test Scores
test_score_1 = 92
test_score_2 = 81
test_score_3 = 88
test_score_4 = 95

# Names
student_first_name = "Sam"
student_last_name = "Nelson"

# Bonus Points
bonus_points = 3

# Class Name
class_name = "'Introduction to Computer Programming' (no prior experience)"

# Calculations
average_score = (test_score_1 + test_score_2 + test_score_3 + test_score_4) / 4
average_score_bonus_points = average_score + bonus_points

# Print Statements
print('*' * 60)
print(class_name)
print('*' * 60)
print('\nStudent: ', end='')
print(student_last_name, student_first_name, sep=', ')
print('Most recent test scores: ', end='')
print(test_score_1, test_score_2, test_score_3, sep=', ', end=' ')
print("and", test_score_4)
print("Average score:", average_score)
print("Class bonus points:", bonus_points)
print("Average score with bonus points added:", average_score_bonus_points)

