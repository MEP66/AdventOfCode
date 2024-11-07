import re

DAY = '16'

SEARCHSTRING = r'Valve ([A-Z]{2}) has flow rate=(\d+); tunnels* leads* to valves* (.+)'



def get_lines(file):
    for row in open(file, 'r', encoding='utf-8'):
        yield row

def get_params(line):
    result = re.search(SEARCHSTRING, line)
    valve = result.group(1)
    rate = result.group(2)
    tunnels = re.findall(r'[A-Z]{2}', result.group(3))
    return (valve, rate, tunnels)
        
def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    #filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    matrix = dict()

    for line in get_lines(filename):
        params = get_params(line)
        matrix[params[0]] = {'rate': params[1], 'tunnels': params[2]}

    pass


if __name__ == '__main__':
    main()
