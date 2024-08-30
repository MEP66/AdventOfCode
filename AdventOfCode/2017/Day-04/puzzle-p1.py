from collections import Counter

DAY = '04'

def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    validpwd = 0
    for line in input_data:
        wrdcount = Counter(line.split(' '))
        if sum(wrdcount.values()) == len(wrdcount):
            validpwd += 1

    print(validpwd)

if __name__ == '__main__':
    main()

#Answer = 325