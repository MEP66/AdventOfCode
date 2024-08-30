import re

DAY = '07'

def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    count = 0
    for line in input_data:
        babmatch = re.findall(r'\[(.*?)\]', line)
        abamatch = re.split(r'\[.*?\]', line)

        bab = list()
        for entry in babmatch:
            matches = re.finditer(r'(?=(.)((?!\1).)\1)', entry)
            temp = [(match.group(1), match.group(2)) for match in matches]
            for x in temp:
                bab.append(x)

        aba = list()
        for entry in abamatch:
            matches = re.finditer(r'(?=(.)((?!\1).)\1)', entry)
            temp = [(match.group(2), match.group(1)) for match in matches]
            for x in temp:
                aba.append(x)

        found = False
        for entry in bab:
            if entry in aba:
                found = True
    
        if found:
            count += 1

    print(count)

if __name__ == '__main__':
    main()

#Answer = 231