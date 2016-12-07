# 141698-20161206-b6d09a7f
moves = ['R1', 'R1', 'R3', 'R1', 'R1', 'L2', 'R5', 'L2', 'R5', 'R1', 'R4', 'L2',
         'R3', 'L3', 'R4', 'L5', 'R4', 'R4', 'R1', 'L5', 'L4', 'R5', 'R3', 'L1',
         'R4', 'R3', 'L2', 'L1', 'R3', 'L4', 'R3', 'L2', 'R5', 'R190', 'R3',
         'R5', 'L5', 'L1', 'R54', 'L3', 'L4', 'L1', 'R4', 'R1', 'R3', 'L1', 'L1',
         'R2', 'L2', 'R2', 'R5', 'L3', 'R4', 'R76', 'L3', 'R4', 'R191', 'R5',
         'R5', 'L5', 'L4', 'L5', 'L3', 'R1', 'R3', 'R2', 'L2', 'L2', 'L4', 'L5',
         'L4', 'R5', 'R4', 'R4', 'R2', 'R3', 'R4', 'L3', 'L2', 'R5', 'R3', 'L2',
         'L1', 'R2', 'L3', 'R2', 'L1', 'L1', 'R1', 'L3', 'R5', 'L5', 'L1', 'L2',
         'R5', 'R3', 'L3', 'R3', 'R5', 'R2', 'R5', 'R5', 'L5', 'L5', 'R2', 'L3',
         'L5', 'L2', 'L1', 'R2', 'R2', 'L2', 'R2', 'L3', 'L2', 'R3', 'L5', 'R4',
         'L4', 'L5', 'R3', 'L4', 'R1', 'R3', 'R2', 'R4', 'L2', 'L3', 'R2', 'L5',
         'R5', 'R4', 'L2', 'R4', 'L1', 'L3', 'L1', 'L3', 'R1', 'R2', 'R1', 'L5',
         'R5', 'R3', 'L3', 'L3', 'L2', 'R4', 'R2', 'L5', 'L1', 'L1', 'L5', 'L4',
         'L1', 'L1', 'R1']

def determineOrientation(current, turn):
    ''' Returns a direction: [N, E, S, W] based on current and turn '''
    directions = ['N', 'E', 'S', 'W']
    if turn == 'R':
        return directions[(directions.index(current) + 1) % 4] # move forward 1
    else:
        return directions[(directions.index(current) + 3) % 4] # move back 1

# initial values
current_position = [0, 0]
orientation = 'N'

for move in moves:

    # split input, first letter is always turn, everything else is a number
    direction = move[0]
    steps = int(move[1:])

    orientation = determineOrientation(orientation, direction)

    # we're placed on a Cartesian grid
    if orientation == 'N':
        current_position[1] += steps
    elif orientation == 'S':
        current_position[1] -= steps
    elif orientation == 'E':
        current_position[0] += steps
    else:
        current_position[0] -= steps

# we want magnitude of blocks away so take absolute values
print (abs(current_position[0]) + abs(current_position[1]))
