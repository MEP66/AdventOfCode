

DAY = '11'

NUM_BLINKS = 75

def split_rules(num, lvl, mem):
    try:
        num_count = mem[(num, lvl)]
    
    except KeyError:
        if lvl == 0:
            num_count = 1
        else:
            if num == 0:
                result = [1]
            elif num == 1:
                result = [2024]
            elif not (len(str(num)) % 2):
                result = [int(str(num)[:int(len(str(num))/2)]), 
                            int(str(num)[int(len(str(num))/2):])]
            else:
                result = [num * 2024]

            if lvl > 1:
                nlvl = lvl - 1
                num_count = 0
                for n in result:
                    mem[(n, nlvl)] = split_rules(n, nlvl, mem)
                    num_count += mem[(n, lvl-1)]
            else:
                num_count = len(result)
            mem[(num, lvl)] = num_count
            
    return num_count


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        stones = [int(x) for x in f.read().strip().split()]

    memory = dict()

    num_stones = 0
    for stone in stones:
        memory[(stone, NUM_BLINKS)] = split_rules(stone, NUM_BLINKS, memory)
        num_stones += memory[(stone, NUM_BLINKS)]

    print(f'Final number of stones = {num_stones}')
    pass


if __name__ == '__main__':
    main()

#Answer = 234568186890978