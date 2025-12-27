##########
# PART 1 #
##########

# define function distance_1d
def distance_1d(a, b): # take in two arguments
    if a < b: # check: if a is less than b, then make sure to subtract a from b
        answer = b - a
    else: # check: if b is less than a, or b =a, them make sure to subtract b from a
        answer = a - b # this makes sure that distance will always be non-negative
    return answer # unpack the answer into the variable ('distance')

distance = distance_1d(0, 7.5) # call the function
print(distance) # print distance

##########
# PART 2 #
##########

# define function grid_distance_2d
def grid_distance_2d(x1, y1, x2, y2): 
    distanceone = distance_1d(x1, x2) # compute distance one by calculating x distance
    distancetwo = distance_1d(y1, y2) # compute distance two by calculation y distance
    answer = distanceone + distancetwo # answer is equal to y plus x distance
    if answer < 0: # take absolute value
        answer = answer * -1
    return answer # unpack answer into variable

grid = grid_distance_2d(1,1,2,2) # call function
print(grid) # print grid distance

##########
# PART 3 #
##########

def direct_distance_2d(x1, y1, x2, y2): # define function
    distanceone = distance_1d(x1, x2) # assign distance between x1 and x2 to var
    distancetwo = distance_1d(y1, y2) # assign distance between y1 and y2 to var
    answer = (distanceone**2 + distancetwo**2)**(1/2) # pythagorean theorem to calculate hypotenuse
    return answer # return answer

direct = direct_distance_2d(0, 0, 3, 4) # call
print(direct) # print

##########
# PART 4 #
##########

def grid_distance_3d(x1, y1, z1, x2, y2, z2): # define function
  down = distance_1d(0, z1) # find down value from 0 to starting height
  across = grid_distance_2d(x1, y1, x2, y2) # find grid distance
  up = distance_1d(0, z2) # find up value from 0 to ending height
  totaldistance = down + across + up # total distance will be down across and up
  return totaldistance # return and unpack

three_d = grid_distance_3d(2, 2, 7, 5, 5, 7) # call
print(three_d) # print

##########
# PART 5 #
##########

def shortest_path_length(x1, y1, z1, x2, y2, z2, x3, y3, z3): # define function
    route1 = grid_distance_3d(x1, y1, z1, x2, y2, z2) + grid_distance_3d(x2, y2, z2, x3, y3, z3) # grid distance between A and B add to distance then B and C
    route2 = grid_distance_3d(x1, y1, z1, x3, y3, z3) + grid_distance_3d(x3, y3, z3, x2, y2, z2) # grid distance between A and C add to distance between C and B
    if route1 < route2: # if first route is less than second, return first
        return route1
    else: # otherwise return second
        return route2

short = shortest_path_length(1, 0, 0, 2, 0, 0, -3, 0, 0) # call 
print(short) # print
    
