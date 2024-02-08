from pathlib import Path

DAY = '01'

filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'

def main():
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    sum = 0
    allsums = []

    for line in input_data:
        if not line:
            allsums.append(sum)
            sum = 0
        else:
            sum += int(line)
    allsums.append(sum)  # save the last sum batch

    allsums.sort(reverse=True)
    print(allsums[0] + allsums[1] + allsums[2])

if __name__ == '__main__':
    main()

# Answer = 198551