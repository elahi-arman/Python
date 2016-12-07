from collections import defaultdict

with open('Day6.in', 'r') as f:
    decoded = []
    for i in range(0, 6):
        x = defaultdict(int)
        decoded.append(x)
    print(decoded)
    for line in f:
        decoded[0][line[0]] += 1
        decoded[1][line[1]] += 1
        decoded[2][line[2]] += 1
        decoded[3][line[3]] += 1
        decoded[4][line[4]] += 1
        decoded[5][line[5]] += 1
        print(decoded)

    # print(decoded)
