import itertools

DAY = '17'

def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    v = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            v.append(int(line.strip()))

    target_sum = 150
    count = 0
    for index in range(1, len(v)):
        all_combos = itertools.combinations(v, index)
        for entry in all_combos:
            if sum(entry) == target_sum:
                count += 1
        if count > 0:
            break

    print(count)


if __name__ == '__main__':
    main()

#Answer = 57