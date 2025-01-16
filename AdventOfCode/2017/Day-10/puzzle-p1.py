

DAY = '10'

def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    ROPE_LENGTH = 5
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    ROPE_LENGTH = 256
 
    with open(filename, 'r', encoding='utf-8') as f:
        twist_lengths = [int(x) for x in f.read().split(',')]

    knots = [x for x in range(ROPE_LENGTH)]
    skip = 0
    
    total_advance = 0
    for twist in twist_lengths:
        string_twist = list(reversed(knots[:twist]))
        knots = [*string_twist, *knots[twist:]]
        advance = twist + skip
        total_advance += advance
        if advance >= ROPE_LENGTH:
            advance -= ROPE_LENGTH

        knots = [*knots[advance:], *knots[:advance]]
        skip += 1

    front_of_list = ROPE_LENGTH - (total_advance % ROPE_LENGTH)
    if front_of_list == ROPE_LENGTH - 1:
        front_two = (knots[-1], knots[0])
    else:
        front_two = (knots[front_of_list], knots[front_of_list + 1])

    print(f'Result: {front_two[0] * front_two[1]}')

if __name__ == '__main__':
    main()

#Answer = 5577