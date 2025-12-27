# While loop to trap user and validate data
import random
while True:
    sides = int(input("How many sides on your dice (4, 6, 8, 10, 12, or 20): "))
    if (sides % 2 == 0 and 4 <= sides <= 12) or sides == 20:
        print('\nThanks! Here we go!')
        print()
        break
    else:
        print('Invalid choice, try again')

tries = 1

highcounter = 0 # accumulator variables to do averages at the end
evencounter = 0
oddcounter = 0
multiplecounter = 0
sumcounter = 0
totalcounter = 0
sequencecounter = 0
samesiescounter = 0
snakecounter = 0

# initialize dice counter to do average at the end
acounter = 0
bcounter = 0
ccounter = 0

while True:

    # Generate random die number
    
    a = random.randint(1, sides)
    b = random.randint(1, sides)
    c = random.randint(1, sides)
    acounter += a
    bcounter += b
    ccounter += c

    
    pairs = '' # start empty in order to accumulate multiple categories
  
   # establish special pairs
    if sides == 8 and a == 8 and b == 8 and c == 8:
        pairs += 'High Roll! '
        highcounter += 1
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        pairs += 'Even Roll! '
        evencounter += 1
    if a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
        pairs += 'Odd Roll! '
        oddcounter +=1
    if a * b == c or a * c == b or b * c == a:
        pairs += 'Multiple Roll! '
        multiplecounter += 1
    if a + b == c or a + c == b or b + c == a:
        pairs += 'Sum Roll! '
        sumcounter += 1
    if a + b + c == sides:
        pairs += 'Total Roll! '
        totalcounter +=1
    if a + 1 == b and b + 1 == c:   
        pairs += 'Sequence Roll! '
        sequencecounter += 1
    if a == b and b == c:
        pairs += 'Samesies Roll! '
        samesiescounter += 1
    if a == 1 and b == 1 and c == 1:
        pairs += 'Three-Eyed Snake! '
        snakecounter += 1
        
    # print each roll
    print(f'{tries}. die roll is {a}-{b}-{c}. {pairs}')
    
    # three-eyed snake
    if a == 1 and b == 1 and c == 1:
        print(f'\nYou finally got the three-eyed snake on roll #{tries}!')
        break
    # accumulate tries for print statement       
    tries += 1
    
# average for special pairs
hroll = ( highcounter / tries ) * 100
eroll = ( evencounter / tries ) * 100
oroll = ( oddcounter / tries ) * 100
mroll = ( multiplecounter / tries ) * 100
suroll = ( sumcounter / tries ) * 100
troll = ( totalcounter / tries ) * 100
seroll = ( sequencecounter / tries ) * 100
saroll = ( samesiescounter / tries ) * 100
throll = ( snakecounter / tries ) * 100

# final print statements
print(f'\nAlong the way you rolled HIGH ROLL {highcounter} times(s). ({hroll:.2f}% of all rolls)')
print(f'Along the way you rolled EVEN ROLL {evencounter} times(s). ({eroll:.2f}% of all rolls) ')
print(f'Along the way you rolled ODD ROLL {oddcounter} times(s). ({oroll:.2f}% of all rolls)')
print(f'Along the way you rolled MULTIPLE ROLL {multiplecounter} times(s). ({mroll:.2f}% of all rolls)')
print(f'Along the way you rolled SUM ROLL {sumcounter} times(s). ({suroll:.2f}% of all rolls)')
print(f'Along the way you rolled TOTAL ROLL {totalcounter} times(s). ({troll:.2f}% of all rolls)')
print(f'Along the way you rolled SEQUENCE ROLL {sequencecounter} times(s). ({seroll:.2f}% of all rolls)')
print(f'Along the way you rolled SAMESIES ROLL {samesiescounter} times(s). ({saroll:.2f}% of all rolls)')
print(f'Along the way you rolled THREE-EYED SNAKE ROLL {snakecounter} times(s). ({throll:.2f}% of all rolls)')

# average of every die
print(f'Average roll for die #1: {acounter / tries:.2f}')
print(f'Average roll for die #2: {bcounter / tries:.2f}')
print(f'Average roll for die #3: {ccounter / tries:.2f}')
