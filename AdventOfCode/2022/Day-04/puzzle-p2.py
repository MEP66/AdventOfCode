import re

DAY = '04'

def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
          input_data = f.read().splitlines()

    overlap = 0
    for line in input_data:
        x = re.findall(r'\d+', line)
        fs, fe, ss, se = map(int, x)
        if (((ss <= fs <= se) or (ss <= fe <= se)) or
            ((fs <= ss <= fe) or (fs <= se <= fe))):

            overlap += 1

    print(f"The number of overlapped sets are: {overlap}")



if __name__ == '__main__':
    main()

# Answer = 924