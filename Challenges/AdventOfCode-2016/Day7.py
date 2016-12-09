def checkABBA(letters):
    # print('Checking Sequence: {}'.format(letters), end='\t')
    if letters[0] == letters[1]:
        # print('First letters are the same, false')
        return False
    if letters[1] == letters[2]:
        # print('Found Match, True')
        return letters[0] == letters[3]

    # print('No ABBA, False')
    return False

def partitionString(string):
    brackets = ['']
    nonbrackets = ['']
    current_sequence = 0
    i = 0
    while i < len(string):

        if string[i] != '[':
            nonbrackets[current_sequence] += string[i]
            i += 1
        else:
            i += 1

            while string[i] != ']':
                brackets[current_sequence] += string[i]
                i += 1
                # print(string[i])

            i += 1
            current_sequence += 1
            brackets.append('')
            nonbrackets.append('')

    for sequence in brackets:

        if len(sequence) < 4:
            continue

        for i in range(1, len(sequence) - 2):
            if checkABBA(sequence[i-1:i+3]) is True:
                return False

    for sequence in nonbrackets:

        if len(sequence) < 4:
            pass

        for i in range(1, len(sequence) - 3):
            if checkABBA(sequence[i-1:i+3]) is True:
                return True

with open('Day7.in', 'r') as f:
    count = 0
    for line in f:
        if partitionString(line) is True:
            count += 1

    print(count)
