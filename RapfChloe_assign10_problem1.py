# import chess board
from chess import print_board

clear_piece_locations = { # coords with pieces 
                         'A1':'rook','A2':'knight',
                         'A3':'bishop','A4':'queen',
                         'A5':'king','A6':'bishop',
                         'A7':'knight','A8':'rook',
                         # empty coords
                         'C1':'empty','C2':'empty',
                         'C3':'empty','C4':'empty',
                         'C5':'empty','C6':'empty',
                         'C7':'empty','C8':'empty',
                         'D1':'empty','D2':'empty',
                         'D3':'empty','D4':'empty',
                         'D5':'empty','D6':'empty',
                         'D7':'empty','D8':'empty',
                         'E1':'empty','E2':'empty',
                         'E3':'empty','E4':'empty',
                         'E5':'empty','E6':'empty',
                         'E7':'empty','E8':'empty',
                         'F1':'empty','F2':'empty',
                         'F3':'empty','F4':'empty',
                         'F5':'empty','F6':'empty',
                         'F7':'empty','F8':'empty',
                         # coords with pieces
                         'B1':'pawn','B2':'pawn',
                         'B3':'pawn','B4':'pawn',
                         'B5':'pawn','B6':'pawn',
                         'B7':'pawn','B8':'pawn',
                         }


filled_piece_locations = {'H1':'rook','H2':'knight',
                          'H3':'bishop','H4':'king',
                          'H5':'queen','H6':'bishop',
                          'H7':'knight','H8':'rook',
                          'G1':'pawn','G2':'pawn',
                          'G3':'pawn','G4':'pawn',
                          'G5':'pawn','G6':'pawn',
                          'G7':'pawn','G8':'pawn',
                          }

            
# define function                          
def get_piece_at_coordinate(coord): # this function will take in a coordinate and return the piece 
    if coord in clear_piece_locations: # check first if the coord is clear
        if clear_piece_locations[coord] != 'empty': # then check if it is not empty
            return f'clear {clear_piece_locations[coord]}' # if it is, then return the clear piece
        else: # if it is empty then return empty
            return 'empty'
    elif coord in filled_piece_locations: # do the same for filled pieces
        return f'filled {filled_piece_locations[coord]}'
    else:
        return 'empty'

# define function    
def is_legal_coordinate(coord): # this function will check if the coord is in either dictionaires
    if coord in clear_piece_locations: # if it is in clear dict, return true 
        return True
    elif coord in filled_piece_locations: # if it is in filled dict, return true
        return True
    else: # otherwise return false
        return False

# define function 
def move_piece(start_coord, end_coord): # this function will move one piece to another position
    if start_coord in clear_piece_locations: # check if start coord is clear
        if clear_piece_locations[start_coord] == 'empty': # check if it is empty 
            return # if it is, return and do nothing 
        else: # otherwise switch positions
            clear_piece_locations[end_coord] = clear_piece_locations[start_coord]
            clear_piece_locations[start_coord] = 'empty' # and make start coord empty
            return # return 
    elif start_coord in filled_piece_locations: # check if start coord is filled
        if filled_piece_locations[start_coord] == 'empty': # if it is then return and do nothing 
            return
        else: # otherwise switch positions
            filled_piece_locations[end_coord] = filled_piece_locations[start_coord]
            filled_piece_locations[start_coord] = 'empty' # and make start coord empty
            return

def is_friendly_fire(start_coord, end_coord): # this function will check for friendly fire 
    start_coord_type = get_piece_at_coordinate(start_coord).split()[0] # extract the type (clear or filled)
    end_coord_type = get_piece_at_coordinate(end_coord).split()[0] # same for end coord
    if start_coord_type == end_coord_type: # if they are the same type then return true
        return True
    else: # other wise return false 
        return False 
        
def is_illegal_jump(start_coord, end_coord): # this function will assess if it is an illegal jump
    # call function to get the start coord piece
    start_info = get_piece_at_coordinate(start_coord)
    if start_info == "empty": # if it is empty, return false
        # not an illegal jump 
        return False
    
    start_piece_type = start_info.split()[1] # extract piece type

    # knights can always jump
    if start_piece_type == "knight":
        return False

    cols = ["A","B","C","D","E","F","G","H"] # create list of coord letters for collumns

    start_row_letter = start_coord[0] # extract first letter from start coord
    end_row_letter   = end_coord[0] # do the same with end coord 
    start_col = int(start_coord[1]) # extract number from start coord
    end_col   = int(end_coord[1]) # same with end coord 

    if start_row_letter not in cols or end_row_letter not in cols: # if it is out of bounds
       
        return False

    start_row_i = cols.index(start_row_letter) # index the letter from the list 
    end_row_i   = cols.index(end_row_letter)
    # row_diff: signed change in row (positive = moving up the board,
    # negative = moving down the board)
    row_diff = end_row_i - start_row_i
    # col_diff: signed change in column (positive = moving right,
    # negative = moving left)
    col_diff = end_col - start_col

    # row_dist: absolute vertical distance traveled (always positive),
    row_dist = row_diff if row_diff >= 0 else -row_diff
    # col_dist: absolute horizontal distance traveled (always positive)
    col_dist = col_diff if col_diff >= 0 else -col_diff

    # work out the direction we’re stepping
    if row_diff > 0:
        row_step = 1
    elif row_diff < 0:
        row_step = -1
    else:
        row_step = 0

    if col_diff > 0:
        col_step = 1
    elif col_diff < 0:
        col_step = -1
    else:
        col_step = 0

    # only straight lines or perfect diagonals can "jump over" pieces
    if not (start_row_i == end_row_i or
            start_col == end_col or
            row_dist == col_dist):
        return False

    # how many squares between start and end
    num_steps = row_dist if row_dist > col_dist else col_dist

    cur_row_i = start_row_i
    cur_col   = start_col

    # check the squares strictly between start and end
    for i in range(1, num_steps):
        cur_row_i += row_step
        cur_col   += col_step

        square = cols[cur_row_i] + str(cur_col)
        mid_info = get_piece_at_coordinate(square)

        # don't split if it's empty
        if mid_info != "empty":
            return True   # there is a piece in between - illegal jump

    # nothing in between
    return False


def piece_type_can_move(start_coord, end_coord):
    # get piece at start
    start_info = get_piece_at_coordinate(start_coord)
    if start_info == 'empty':
        return False # if it is empty return false 

    side, piece = start_info.split()   # split, for ex: 'clear pawn' - 'clear' 'pawn'

    # rows are letters, columns are numbers
    rows = ['A','B','C','D','E','F','G','H']

    start_row = start_coord[0]
    end_row = end_coord[0]

    # if rows off-board, return False
    if start_row not in rows or end_row not in rows:
        return False
    # convert row letters into indices
    start_row_i = rows.index(start_row)
    end_row_i = rows.index(end_row)
    # convert  coord digits to integers
    start_col = int(start_coord[1])
    end_col = int(end_coord[1])
    # how far the move travels vertically and horizontally 
    row_diff = end_row_i - start_row_i      # can be negative
    col_diff = end_col - start_col          # can be negative

    # rook moves on horizontally or vertically
    if piece == 'rook':
        # same row but diff column (horizontal move)
        # or same column but diff row (vertical move)
        if (start_row_i == end_row_i and start_col != end_col) or \
           (start_col == end_col and start_row_i != end_row_i):
            return True
        else: # store which piece failed, use din error printing later
            not_permitted_pattern_piece = piece
            return False

    # bishop moves diagonally
    if piece == 'bishop':
        # diagonal means:
        if (row_diff == col_diff or row_diff == -col_diff) and row_diff != 0:
            return True
        else:
            not_permitted_pattern_piece = piece
            return False

    # queen rook movement or bishop movement
    if piece == 'queen':
        # same row or same column
        straight = ((start_row_i == end_row_i and start_col != end_col) or
                    (start_col == end_col and start_row_i != end_row_i))
        # bishop-like diagonal movement
        diagonal = (row_diff == col_diff or row_diff == -col_diff) and row_diff != 0
        not_permitted_pattern_piece = piece
        # return true if either movement patter is valid 
        return straight or diagonal

    # king moves on square in any direction, but can't stay still
    if piece == 'king':
        # one square in any direction (but not zero move)
        if (row_diff in (-1, 0, 1)) and (col_diff in (-1, 0, 1)) and not (row_diff == 0 and col_diff == 0):
            return True
        else:
            not_permitted_pattern_piece = piece
            return False

    # knight
    if piece == 'knight':
        # L-shape: 2 by 1 or 1 by 2
        # did we move two rows
        two_row = (row_diff == 2 or row_diff == -2)
        # one row?
        one_row = (row_diff == 1 or row_diff == -1)
        # two columns
        two_col = (col_diff == 2 or col_diff == -2)
        # one column?
        one_col = (col_diff == 1 or col_diff == -1)
         # valid if: 2 rows + 1 column  or  1 row + 2 columns
        if (two_row and one_col) or (one_row and two_col):
            return True
        else:
            not_permitted_pattern_piece = piece
            return False

    # pawn
    if piece == 'pawn':
        # extra credit version: pawns only move forward
        # clear pawns move toward increasing row index (down the board),
        # filled pawns move toward decreasing row index (up the board)
        if side == 'clear':
            forward_step = 1
        else:  # otherwise (side == 'filled')
            forward_step = -1
        # look at what is currently on the destination square
        target_info = get_piece_at_coordinate(end_coord)

        # straight move: one step forward, destination must be empty
        if start_col == end_col and row_diff == forward_step:
            if target_info == 'empty':
                return True # return true 
            else: # otherwise store piece and return false
                not_permitted_pattern_piece = piece
                return False

        # diagonal capture: one step forward diagonally, must hit enemy piece
        if (row_diff == forward_step) and (col_diff == 1 or col_diff == -1):
            if target_info != 'empty':
                target_side, _ = target_info.split()
                # legal only if capturing the opposite side
                if target_side != side:
                    return True
                # either empty square or same side piece - illegal move
            return False

        # anything else is illegal for pawns
        return False

    # if somehow the piece type is unknown
    return False

def move_if_valid(start_coord, end_coord, turn): # this function will check the validity of the coords before moving
    if get_piece_at_coordinate(start_coord) == 'empty': # check if empty 
        return f'No piece to move at coordinate {start_coord}'
    
    if get_piece_at_coordinate(start_coord).split()[0] != turn: # check if same type
        return "Cannot move the other team's pieces"
    
    if not is_legal_coordinate(start_coord): # call function to check legality 
        return f'Coordinate {start_coord} is invalid'
    
    if not is_legal_coordinate(end_coord): # same for end coord
        return f'Coordinate {end_coord} is invalid'
    
    if is_checked(turn): # check if king is in check
        return 'Check: move results in king being in check'
    
    if is_friendly_fire(start_coord, end_coord): # check for friendly fire
        return 'Friendly fire: cannot move into a square where you already have a piece'
    
    if is_illegal_jump(start_coord, end_coord): # check for illegal jump
        return 'Illegal jumping: cannot jump over pieces'
    
    if not piece_type_can_move(start_coord, end_coord): # check for permitted moves based on type 
        return f'{get_piece_at_coordinate(start_coord).split()[1]} did not move in a permitted pattern'

    
    move_piece(start_coord, end_coord) # otherwise move
    return ""

def is_checked(side): # side is clear or filled, returns true if that side's king is in check, false otherwise 
 
    
    if side == "clear": # figure out which dict has the king, and which has the enemy pieces
        my_pieces = clear_piece_locations
        enemy_pieces = filled_piece_locations
    else:  # otherwise side == 'filled'
        my_pieces = filled_piece_locations
        enemy_pieces = clear_piece_locations
    
    king_coord = None # find this side's king coordinate
    for coord, piece in my_pieces.items():
        if piece == "king":
            king_coord = coord
            break

    if king_coord is None: # if there is no king on the board, return false 
        return False

    for enemy_coord, enemy_piece in enemy_pieces.items(): # look at every enemy piece and see if it can legally capture the king
        if enemy_piece == "empty":
            continue  # no piece here

        if not piece_type_can_move(enemy_coord, king_coord): # first check if the piece's movement pattern could reach the king
            continue

        if is_illegal_jump(enemy_coord, king_coord): # next make sure it is not an illegal jump
            continue

        if is_friendly_fire(enemy_coord, king_coord): # make sure no firendly fire
            continue

        return True

    return False # no enemy piece can capture the king in one move

  
    
def has_won(side):
    
    if side == "clear": # we look at the opposite side's pieces
        enemy_positions = filled_piece_locations
    else:   # otherwise side == "filled"
        enemy_positions = clear_piece_locations

    for piece in enemy_positions.values(): # check if the enemy still has a king anywhere
        if piece == "king":
            return False

    
    return True # otherwsie if king is not found, player has won

def play_game():
    current_turn = "clear" # game always starts with clear team

    while True:
        print(f"Turn: {current_turn.capitalize()}") # print the turn

        start_coord = input("Move Start Coordinate: ").strip() # user inputs
        end_coord = input("Move End Coordinate: ").strip()

        result = move_if_valid(start_coord, end_coord, current_turn) # call function

        if result == "":
            print("Move successful")

            # extra credit part M
            for coord in clear_piece_locations: # promote clear pawns that reached row H 
                if clear_piece_locations[coord] == "pawn" and coord[0] == "H":
                    clear_piece_locations[coord] = "queen"

            for coord in filled_piece_locations: # promote filled pawns that reached row A (A1–A8)
                if filled_piece_locations[coord] == "pawn" and coord[0] == "A":
                    filled_piece_locations[coord] = "queen"
            

            # after promotion check if someone has won
            if has_won(current_turn):
                if current_turn == "clear":
                    print("Filled king was captured - Clear Team wins!")
                else:
                    print("Clear king was captured - Filled Team wins!")
                print_board(clear_piece_locations, filled_piece_locations)
                break

            # print updated board
            print_board(clear_piece_locations, filled_piece_locations)

            # switch turns
            if current_turn == "clear":
                current_turn = "filled"
            else:
                current_turn = "clear"

        else:
            # invalid move and same team goes again
            print(result)


    
    
