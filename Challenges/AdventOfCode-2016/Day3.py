with open('Day3.in', 'r') as f:
    count = 0
    for line in f:
        triangle = [int(x) for x in line.split()]
        if (triangle[0] + triangle[1] > triangle[2]
            and triangle[1] + triangle[2] > triangle[0]
            and triangle[0] + triangle[2] > triangle[1]):
            print(line)
            count += 1
    print(count)
