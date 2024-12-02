from collections import defaultdict


DAY = '15'

MAXTURN = 2020


def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        st_nums = [int(x) for x in f.read().strip().split(',')]

    
    spoken = defaultdict(list)
    turn = 0
    
    for n in st_nums:
        turn += 1
        spoken[n] = [turn]
        last_spoken = n

    while turn < MAXTURN:
        turn += 1
        if len(spoken[last_spoken]) == 1:
            last_spoken = 0
        else:
            last_spoken = spoken[last_spoken][-1] - spoken[last_spoken][-2]
        spoken[last_spoken].append(turn)
            
    print(f'Last Spoken: {last_spoken}')


if __name__ == '__main__':
    main()

#Answer = 929