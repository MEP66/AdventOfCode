import re

DAY = '04'

def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
          input_data = f.read().splitlines()

    fullycontained = 0
    for line in input_data:
        x = re.findall(r'\d+', line)
        fs, fe, ss, se = map(int, x)
        if (fs >= ss and fe <= se) or (ss >= fs and se <= fe):
            fullycontained += 1

    print(f"The number of fully contained sets are: {fullycontained}")



if __name__ == '__main__':
    main()

# Answer = 562