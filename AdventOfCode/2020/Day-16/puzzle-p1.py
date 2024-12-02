

DAY = '16'


def get_file_line(filename):
    with open(filename, 'r', encoding='utf-u') as f:
        for line in f:
            yield line

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    #filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    line_gen = get_file_line(filename)
    line = next(line_gen)

    tkt_valid = dict()

    while not line:
        params = line.split(': ')
        bndry
    

if __name__ == '__main__':
    main()
