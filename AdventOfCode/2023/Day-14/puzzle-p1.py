# puzzle-p1 (Day 14)

from collections import Counter

ROCK  = 'O'
SPACE = '.'
WALL = '#'

def main():

    # Fetch the puzzle data

    #filename = r'./Day-14/input-example.txt'
    filename = r'./Day-14/input.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        input = [list(line.strip()) for line in f]

    # Tilt the table, let the rocks roll

    lastrow = len(input)

    for col in range(len(input[0])):
        spaceptr = 0
 
        while True:
            if spaceptr < lastrow:
                if input[spaceptr][col] != SPACE:
                    spaceptr += 1
                else:
                    rockptr = spaceptr + 1
                    while True:
                        if rockptr < lastrow:
                            if input[rockptr][col] == ROCK:
                                input[spaceptr][col] = ROCK
                                input[rockptr][col] = SPACE
                                spaceptr += 1
                                break
                            elif input[rockptr][col] == WALL:
                                spaceptr = rockptr
                                break
                            else:
                                rockptr += 1
                        else:
                            spaceptr = lastrow
                            break
            else:
                break

    # Calculate weight

    sum = 0

    for index , row in enumerate(input):
        symcnts = Counter(row)
        sum += symcnts.get(ROCK, 0) * (lastrow - index)
        
    print ('Final weight = ', sum)


if __name__ == '__main__':
    main()

# Answer = 106997