from collections import defaultdict


DAY = '05'


def file_line_gen(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    before = defaultdict(set)
    after = defaultdict(set)

    line = next(get_line := file_line_gen(filename))

    while line != '':
        params = [int(x) for x in line.split('|')]
        before[params[1]].add(params[0])
        after[params[0]].add(params[1])
        line = next(get_line)

    updates = [[int(x) for x in line.split(',')] for line in get_line]

    sum_middle_pages = 0
    for update in updates:
        valid = True
        for i, current_page in enumerate(update):
            pgs_before = set(update[:i])
            pgs_after = set(update[i+1:])
            if not (pgs_before.issubset(before[current_page]) and pgs_after.issubset(after[current_page])):
                valid = False
                break
        if valid:
            sum_middle_pages += update[len(update)//2]

    print(f'Sum of middle phages: {sum_middle_pages}')

if __name__ == '__main__':
    main()

#Answer = 4578