import re

DAY = '07'

def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    count = 0
    for line in input_data:
        negmatch = re.findall(r'\[(.*?)\]', line)
        posmatch = re.split(r'\[.*?\]', line)

        found = False
        for entry in posmatch:
            if re.search(r'(.)((?!\1).)\2\1', entry):
                found = True
        if found:
            found = False
            for entry in negmatch:
                if re.search(r'(.)((?!\1).)\2\1', entry):
                    found = True
            if not found:
                count += 1

    print(count)

if __name__ == '__main__':
    main()

#Answer = 115