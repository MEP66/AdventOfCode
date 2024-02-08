from pathlib import Path

DAY = '01'

filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'

def main():
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    maxsum = 0
    sum = 0

    for line in input_data:
        if not line:
            maxsum = max(sum, maxsum)
            sum = 0
        else:
            sum += int(line)
    
    print(maxsum)

if __name__ == '__main__':
    main()


# Answer = 66719