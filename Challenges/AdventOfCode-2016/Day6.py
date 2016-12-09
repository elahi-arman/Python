from collections import Counter

with open('Day6.in', 'r') as f:
    columns = [''] * 8

    for line in f:
        columns[0] += line[0]
        columns[1] += line[1]
        columns[2] += line[2]
        columns[3] += line[3]
        columns[4] += line[4]
        columns[5] += line[5]
        columns[6] += line[6]
        columns[7] += line[7]

    for string in columns:
        print(Counter(string).most_common(1)[0])
    # print(decoded)
