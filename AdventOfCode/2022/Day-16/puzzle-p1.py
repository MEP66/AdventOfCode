import re

DAY = '16'

SEARCHSTRING = r'Valve ([A-Z]{2}) has flow rate=(\d+); tunnels* leads* to valves* (.+)'

def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    #filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    matrix = dict()

    with open(filename, 'r', encoding='utf-8') as f:
        line = f.readline().strip()
        while line:
            result = re.search(SEARCHSTRING, line)
            tunnels = re.findall(r'[A-Z]{2}', result.group(3))
            matrix[result.group(1)] = {'rate': result.group(2), 'tunnels': tunnels}
            line = f.readline().strip()

    pass



if __name__ == '__main__':
    main()
