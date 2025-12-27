import random

print("Let's Play Rock, Paper, Scissors, Lizard, Spock!")
print()

# keep asking user for valid data input of number of wins
wins_needed = 0
while wins_needed <= 0:
    user_input = input("How many wins is required to end the tournament? ")
    wins_needed = int(user_input)
    if wins_needed <= 0:
        print("Invalid, try again")
print('\nOK, here we go!\n')

# initialize scores and winning steaks
user_wins = 0
comp_wins = 0
ties = 0
round_no = 1

curr_owner = ""   # keep track of current owner of winning steaks
curr_len = 0      # keep track of how long winning streak is
best_owner = ""   # keep track of longest streak
best_len = 0      # keep track of current owner of longest streak

# initialize user counter
user_rock = 0
user_paper = 0
user_scissors = 0
user_lizard = 0
user_spock = 0

# initialize computer counter
comp_rock = 0
comp_paper = 0
comp_scissors = 0
comp_lizard = 0
comp_spock = 0

# main loop
while user_wins < wins_needed and comp_wins < wins_needed:
    # streak line
    if best_len == 0:
        streak_line = "There has been no winning streak so far"
    else:
        if best_owner == "user":
            streak_line = "The user has the longest winning streak of " + str(best_len)
        elif best_owner == "comp":
            streak_line = "The computer has the longest winning streak of " + str(best_len)
        else:
            streak_line = "The both players have the longest winning streak of " + str(best_len)
    
    print("-" * 37)
    print("Round #", round_no)
    print("You have won", user_wins, "rounds")
    print("The computer has won", comp_wins, "rounds")
    print("There have been", ties, "ties so far")
    print(streak_line)
    print("-" * 37)

    # keep asking user for valid data input 
    user_move = ""
    while user_move == "":
        choice = input("(R)ock, (P)aper, (S)cissors, (L)izard or Sp(O)ck: ")
        if choice == "r" or choice == "R":
            user_move = "Rock"
            user_rock = user_rock + 1
        elif choice == "p" or choice == "P":
            user_move = "Paper"
            user_paper = user_paper + 1
        elif choice == "s" or choice == "S":
            user_move = "Scissors"
            user_scissors = user_scissors + 1
        elif choice == "l" or choice == "L":
            user_move = "Lizard"
            user_lizard = user_lizard + 1
        elif choice == "o" or choice == "O":
            user_move = "Spock"
            user_spock = user_spock + 1
        else:
            print("This is an invalid choice, please try again.")

    # computer random choice
    r = random.randint(0, 4)
    if r == 0:
        comp_move = "Rock"
        comp_rock = comp_rock + 1
    elif r == 1:
        comp_move = "Paper"
        comp_paper = comp_paper + 1
    elif r == 2:
        comp_move = "Scissors"
        comp_scissors = comp_scissors + 1
    elif r == 3:
        comp_move = "Lizard"
        comp_lizard = comp_lizard + 1
    else:
        comp_move = "Spock"
        comp_spock = comp_spock + 1

    print("The computer has selected", comp_move)

    # decide winner based on user move and computer move
    if user_move == comp_move:
        print("The round has ended in a tie! No points awarded!")
        ties = ties + 1
        curr_owner = ""
        curr_len = 0
    elif user_move == "Scissors" and comp_move == "Paper":
        print('Scissors cuts Paper!')
        print("User wins!")
        user_wins = user_wins + 1
        if curr_owner == "user":
            curr_len = curr_len + 1
        else:
            curr_owner = "user"
            curr_len = 1
    elif user_move == "Scissors" and comp_move == "Lizard":
        print('Scissors decapitates Lizard!')
        print("User wins!")
        user_wins = user_wins + 1
        if curr_owner == "user":
            curr_len = curr_len + 1
        else:
            curr_owner = "user"
            curr_len = 1
    elif user_move == "Paper" and comp_move == "Rock":
        print('Paper covers Rock!')
        print("User wins!")
        user_wins = user_wins + 1
        if curr_owner == "user":
            curr_len = curr_len + 1
        else:
            curr_owner = "user"
            curr_len = 1
    elif user_move == "Paper" and comp_move == "Spock":
        print('Paper disproves Spock!')
        print("User wins!")
        user_wins = user_wins + 1
        if curr_owner == "user":
            curr_len = curr_len + 1
        else:
            curr_owner = "user"
            curr_len = 1
    elif user_move == "Rock" and comp_move == "Scissors":
        print('Rock crushes Scissors!')
        print("User wins!")
        user_wins = user_wins + 1
        if curr_owner == "user":
            curr_len = curr_len + 1
        else:
            curr_owner = "user"
            curr_len = 1
    elif user_move == "Rock" and comp_move == "Lizard":
        print('Rock crushes Lizard!')
        print("User wins!")
        user_wins = user_wins + 1
        if curr_owner == "user":
            curr_len = curr_len + 1
        else:
            curr_owner = "user"
            curr_len = 1
    elif user_move == "Lizard" and comp_move == "Spock":
        print('Lizard poisons Spock!')
        print("User wins!")
        user_wins = user_wins + 1
        if curr_owner == "user":
            curr_len = curr_len + 1
        else:
            curr_owner = "user"
            curr_len = 1
    elif user_move == "Lizard" and comp_move == "Paper":
        print('Lizard eats Paper!')
        print("User wins!")
        user_wins = user_wins + 1
        if curr_owner == "user":
            curr_len = curr_len + 1
        else:
            curr_owner = "user"
            curr_len = 1
    elif user_move == "Spock" and comp_move == "Scissors":
        print('Spock smashes Scissors!') 
        print("User wins!")
        user_wins = user_wins + 1
        if curr_owner == "user":
            curr_len = curr_len + 1
        else:
            curr_owner = "user"
            curr_len = 1
    elif user_move == "Spock" and comp_move == "Rock":
        print('Spock vaporizes Rock!')
        print("User wins!")
        user_wins = user_wins + 1
        if curr_owner == "user":
            curr_len = curr_len + 1
        else:
            curr_owner = "user"
            curr_len = 1
    else:
        print("Computer wins!")
        comp_wins = comp_wins + 1
        if curr_owner == "comp":
            curr_len = curr_len + 1
        else:
            curr_owner = "comp"
            curr_len = 1

    # update streaks
    if curr_len > best_len:
        best_len = curr_len
        best_owner = curr_owner
    elif curr_len == best_len and best_len != 0:
        if best_owner != curr_owner:
            best_owner = "both"

    print()
    round_no = round_no + 1


if user_wins == wins_needed:
    print("User wins the game!")
else:
    print("Computer wins the game!")

# Game summary
print()
print("Game summary:")
print("- Rock was played", user_rock + comp_rock, "times (User=" + str(user_rock) + "; Computer=" + str(comp_rock) + ")")
print("- Paper was played", user_paper + comp_paper, "times (User=" + str(user_paper) + "; Computer=" + str(comp_paper) + ")")
print("- Scissors was played", user_scissors + comp_scissors, "times (User=" + str(user_scissors) + "; Computer=" + str(comp_scissors) + ")")
print("- Lizard was played", user_lizard + comp_lizard, "times (User=" + str(user_lizard) + "; Computer=" + str(comp_lizard) + ")")
print("- Spock was played", user_spock + comp_spock, "times (User=" + str(user_spock) + "; Computer=" + str(comp_spock) + ")")



    

      
