
officers = {} # create empty dictionary

folder = "/Users/Jill/Downloads/Assignment 9 Supporting Files/problem2_supporting_files/" # locate folder
f = open(folder + "names_and_ranks.txt", "r") # open txt inside folder
data = f.read().split("\n") # read and split by new line
f.close() # close 

for line in data: # for each person
    if "," in line: # check
        parts = line.split(",") # separate person from their rank 
        name = parts[0].strip() # first index is their name
        rank = parts[1].strip() # second is their rank
        officers[name] = rank # match keys to values



accounts = {}   # create empty dictionary

f = open("accounts.txt", "a") # create new txt
f.close() # close 


f = open("accounts.txt", "r") # open and read it
contents = f.read()
f.close() # close 


if contents != "": 
    rows = contents.split("\n") # split file into individual lines
    for row in rows:
        if row != "": # ignore empty lines
            pieces = row.split(",") # break lines
            username = pieces[0] # get username
            password = pieces[1] # and password
            fullname = pieces[2] # and fullname
            rank = pieces[3] # and rank
            accounts[username] = [password, fullname, rank] # store all this in dictionary



def can_authorize(rank):
    return rank == "GRAND MOFF" or rank == "SUPREME COMMANDER"
# checks if rank is allowed to authorize a strike

def can_mark_complete(rank):
    allowed = ["LIEUTENANT SR", "LT COMMANDER", "COMMANDER", "CAPTAIN",
               "COMMODORE", "ADMIRAL", "GENERAL", "GRAND MOFF", "SUPREME COMMANDER"]
    return rank in allowed
# checks if rank is allowed to mark a strike 

# reads current strike target from strike.txt
def get_current_strike():
    try:
        f = open("strike.txt", "r")
        target = f.read().strip()
        f.close()
        if target == "":
            return None # if file is empty, returns none
        return target
    except:
        return None

# attempts to authorize a new strike
def authorize_strike(rank):
    if not can_authorize(rank): # only high ranks
        print("Your rank is insufficient to order a strike.")
        return

    current = get_current_strike()
    if current != None: # if strike is already in progress, prevent doing a new one
        print(f"Strike on {current} is currently in progress. Cannot authorize another strike.")
        return

    target = input("Enter Target: ") # adds new target to strike.txt
    f = open("strike.txt", "w")
    f.write(target) # adds target and closes
    f.close()
    print(f"Strike has been authorized for {target}.")

def cancel_strike(rank): # ensures only high ranks can cancel
    if not can_authorize(rank):
        print("Your rank is insufficient to cancel a strike.")
        return

    current = get_current_strike() # get whatever strike is currently active
    if current == None: # if none, can't cancel anything
        print("No un-completed strike was recorded, cannot cancel strike.")
        return

    print(f"Strike on {current} has been cancelled.")
    f = open("strike.txt", "w") # if a strike exists, then cancel it 
    f.write("")                 # by using 'w' to wipe the file
    f.close()

def mark_strike_complete(rank):# check if rank is allowed to mark a strike
    if not can_mark_complete(rank):
        print("Your rank is insufficient to mark a strike as complete.")
        return

    current = get_current_strike() # read current strike target from strike.txt
    if current == None: # if no actives, there is nothing to complete
        print("No strike is currently in progress.")
        return

    # otherwise we have permission and an active strike
    print(f"Strike on {current} has been marked as complete.")
    f = open("strike.txt", "w") # overwrite
    f.write("")      # empty string = no active target
    f.close() # close 




logged_in = False # start with assumpyton that user hasn't logged in 
current_user = "" # creat empty string

print("* * * * * * * * * * * * * * * * *")
print("* * WELCOME TO THE DEATH STAR * *")
print("* * * * * * * * * * * * * * * * *")

while True: # main program loop

    if logged_in == False: # if not logged in, show main menu options
        choice = input("Main Menu: (l)ogin, (r)egister, (q)uit: ")
    # prompt user

  
    if choice == "q": # if they choose to quit, then break
        print("Thank you for your service to your emperor. Goodbye.")
        break


    # if user wants to register AND not logged in yet
    if choice == "r" and logged_in == False:

        name = input("Name: ") # ask for name 

        
        if name not in officers: # check if name is an authorized person
            print(name, "is not an authorized Imperial Officer This incident will be reported.")
            continue

        
        already = False # check if user has already created an account 
        for u in accounts:
            if accounts[u][1] == name: # [u[1] is the full name stored
                already = True # if full name already stored then user already created an account

        if already == True: # if they have, print this
            print("You have already registered an account.")
            continue
        # otherwise, person is valid : proceed
        print("Welcome,", officers[name], name + ". Please create your account.")

        username = input("Username: ")

        if username in accounts: # prevent duplicate usernames
            print("That username is already taken.")
            continue

        password = input("Password: ")

        # store new account in dictionary
        accounts[username] = [password, name, officers[name]]

        # write all acounts back to accounts.txt
        f = open("accounts.txt", "w") # clear file
        for u in accounts:
            pw = accounts[u][0] # password
            fullname = accounts[u][1] # full name
            rank = accounts[u][2] # rank
            f.write(u + "," + pw + "," + fullname + "," + rank + "\n")
        f.close() # write in username,password,fullname,rank format and then close

        print("Thank you. Your account has been created.")
        continue


   # if user wants to login and they havent already
    if choice == "l" and logged_in == False:

        username = input("Username: ") # ask for this 
        password = input("Password: ")

        if username not in accounts: # if username doesn't exist in dictionary
            print("Unfortunately, you do not have an account. To register, please select (r)egister.")
            continue
        # get actual stored password for the username 
        real_password = accounts[username][0]
        # check if entered password is correct
        if password != real_password:
            print("Incorrect password. Please try again.")
            continue
        # successful login
        logged_in = True
        current_user = username
        #get full name and rank from accounts dictionary
        fullname = accounts[username][1]
        rank = accounts[username][2]
        # welcome logged in user
        print(f"Welcome, {rank.upper()} {fullname}.")
        
    while logged_in: # main login menu loop
            main_choice = input(f"[{current_user}] Main Menu: Press (o)rder, (q)uit: ")
            # keep user trapped for an action
            if main_choice == "q": # if user quits, break and exit
                print("Thank you for your service to your emperor. Goodbye.")
                logged_in = False
                break   

            elif main_choice == "o": # if user wants to order
                # check if theyre in the allowed ranks
                allowed = ["LIEUTENANT", "LT COMMANDER", "COMMANDER",
                           "CAPTAIN", "SUPREME COMMANDER", "GRAND MOFF"]
                # if theyre not, block the action
                if rank.upper() not in allowed:
                    print("Your rank is insufficient to order anyone around. Try harder.")
                    continue     

              # if the user CAN authorize a strike, show them this menu
                if can_authorize(rank):
                   
                    while True: # show menu for high rank users
                        choice = input(
                            f"[{current_user}] Action Menu: Press (s)trike, "
                            f"(c)ancel strike, (m)ark complete, (q)uit: "
                        )
                        # handle each command and call functions
                        if choice == "s":
                            authorize_strike(rank)
                        elif choice == "c":
                            cancel_strike(rank)
                        elif choice == "m":
                            mark_strike_complete(rank)
                        elif choice == "q":
                            # exit to main menu
                            print("Thank you for your service to your emperor. Goodbye.")
                            logged_in = False
                            break
                        else:
                            print("Invalid choice.")
                else:
                    # if the user CANT authorize a stike, give them this limited menu
                    while True:
                        choice = input(
                            f"[{current_user}] Action Menu: Press (m)ark complete, (q)uit: "
                        )
                        # if user wants to mark
                        if choice == "m":
                            mark_strike_complete(rank) # call function
                        elif choice == "q": # if user quits, break
                            print("Thank you for your service to your emperor. Goodbye.")
                            logged_in = False
                            break
                        else: # otherwise, invalid choice
                            print("Invalid choice.")

