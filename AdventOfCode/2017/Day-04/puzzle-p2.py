from itertools import combinations

DAY = '04'

def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    
    num_valid = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            elements = [list(w) for w in line.strip().split()]
            for i, l in enumerate(elements):
                l.sort()
                elements[i] = ''.join(l)
            valid = True
            for c in combinations(elements, 2):
                if c[0] == c[1]:
                    valid = False
                    break
            if valid:
                num_valid += 1
    
    print(num_valid)


if __name__ == '__main__':
    main()

#Answer = 119