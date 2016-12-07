from Libs.StateMachine import StateMachine

def easy(sequence):
    # If you cut a white cable you can't cut white or black cable.
    # If you cut a red cable you have to cut a green one
    # If you cut a black cable it is not allowed to cut a white, green or orange one
    # If you cut a orange cable you should cut a red or black one
    # If you cut a green one you have to cut a orange or white one
    # If you cut a purple cable you can't cut a purple, green, orange or white cable
    try:
        current = 'x'
        for wire in sequence:
            color = wire[0]
            if current is 'w':
                if color is not 'w' or color is not 'b':
                    current = color
                else:
                    print('BOOM')
                    return
            elif current is 'r':
                if color is 'g':
                    current = color
                else:
                    print('BOOM')
                    return
            elif current is 'b':
                if color is not 'w' or color is not 'g' or color is not 'o':
                    current = color
                else:
                    print('BOOM')
                    return
            elif current is 'o':
                if color is 'r' or color is 'b':
                    current = color
                else:
                    print('BOOM')
                    return
            elif current is 'g':
                if color is 'o' or color is 'w':
                    current = color
                else:
                    print('BOOM')
                    return
            elif current is 'p':
                if color is not 'p' or color is not 'g' or color is not 'o' or color is not 'w':
                   current = color
                else:
                   print('BOOM')
                   return
            else:
                current = color
        print ('Bomb Defused')

    except TypeError:
        print('Sorry the given sequence is not iterable')

def medium2(sequence):
    # You have to start with either with a white or a red wire.
    # If you picked white wire you can either pick another white wire again or you can take an orange one.
    # If you picked a red wire you have the choice between a black and red wire.
    # When a second red wire is picked, you can start from rule one again.
    # Back to the second rule, if you picked another white one you will have to pick a black or red one now
    # When the red wire is picked, you again go to rule one.
    # On the other hand if you then picked an orange wire, you can choose between green, orange and black.
    # When you are at the point where you can choose between green, orange and black and you pick either green or orange you have to choose the other one and then the bomb is defused.
    # If you ever pick a black wire you will be at the point where you have to choose between green, orange and black

    sm = StateMachine(7)

    for i in range(7):
        sm.addVertex(i)

    sm.addEdge(0, 1, 'w')
    sm.addEdge(0, 2, 'r')
    sm.addEdge(1, 2, 'w')
    sm.addEdge(1, 2, 'o')
    sm.addEdge(2, 0, 'r')
    sm.addEdge(2, 3, 'b')
    sm.addEdge(3, 3, 'b')
    sm.addEdge(3, 4, 'g')
    sm.addEdge(3, 5, 'o')
    sm.addEdge(4, 6, 'o')
    sm.addEdge(5, 6, 'g')

    for wire in sequence:
        color = wire[0]
        print(sm.currentState, end=",")
        sm.advance(color)
        print (sm.currentState)
        if sm.currentState == -1:
            return 'Boom'
        elif sm.currentState == 6:
            return 'Bomb Defused'

    return 'Boom'

if __name__ == '__main__':
    sequence = []
    while True:
        next_wire = input('>')
        if next_wire == '0':
            print(medium2(sequence))
            break
        else:
            sequence.append(next_wire)
