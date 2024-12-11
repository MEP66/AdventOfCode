

DAY = '11'


NUM_BLINKS = 25


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        stones = [int(x) for x in f.read().strip().split()]

    for _ in range(NUM_BLINKS):
        new_list = list()
        for stone in stones:
            if stone == 0:
                new_list.append(1)
            elif stone == 1:
                new_list.append(2024)
            elif not (len(str(stone)) % 2):
                new_list.extend([int(str(stone)[:int(len(str(stone))/2)]), 
                                    int(str(stone)[int(len(str(stone))/2):])])
            else:
                new_list.append(stone * 2024)
        stones = new_list

    print(f'Num stones: {len(stones)}')


if __name__ == '__main__':
    main()

#Answer = 197357