##########
# PART 1 #
##########
def shift_left(string, integer): # define function
    integer = integer % len(string) # this will handle negative integers or integers longer than the length of the string 

    # separate into two pieces. eahc char in the string isnt actually being 'shifted left' only the first piece is being moved
    x = string[0:integer] # first piece
    y = string[integer:] # second piece: what's left 
    z = y + x # concatenate 
    return z # return 

##########
# PART 2 #
##########
def swap(string, integer): # define function
    result = "" # start w/ empty string to build swapped result

    for i in range(0, len(string), integer * 2): # start from 0 position, step by chunk, stop before length of string,
                                                # to look at pairs of chunks at a time
        first = string[i:i+integer] # handles first chunk
        second = string[i+integer:i+integer*2] # handles second chunk

        # only swap if there is a full second chunk
        if len(second) == integer:
            result = result + second + first
        else:
            result = result + first + second # otherwise, keep chars in original order

    return result # return 

##########
# PART 3 #
##########
def encrypt(string, integer1, integer2): # define 
    shifted = shift_left(string, integer1) # first shift the string by calling the shift_left function
    swapped = swap(shifted, integer2) # then take the shifted string and swap it by calling the swap function
    return swapped # return 

##########
# PART 4 #
##########

def decrypt(string, integer1, integer2): # define 
    
    first_part = swap(string, integer2) # first un-swap the string by calling the swap function
    second_part = shift_left(first_part, -integer1) # then undo the shift by calling the shift function and shifting in the opposite direction
    return second_part # return
    

