import re


DAY = '16'


def get_file_line(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    #filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'

    line_gen = get_file_line(filename)
    line = next(line_gen)

    tkt_validation = dict()

    while line != '':
        params = line.split(': ')
        bndry = [int(x) for x in re.findall(r'\d+', params[1])]
        tkt_validation[params[0]] = [(bndry[0], bndry[1]), (bndry[2], bndry[3])]
        line = next(line_gen)

    while line != 'your ticket:':
        line = next(line_gen)
    line = next(line_gen)

    my_ticket = [int(x) for x in line.split(',')]

    while line != 'nearby tickets:':
        line = next(line_gen)

    nby_tickets = [[int(x) for x in line.split(',')] for line in line_gen]
    nby_tickets.append(my_ticket)
    
    valid_tickets = list()

    for tkt in nby_tickets:
        for param in tkt:
            found = False
            for bnd in tkt_validation.values():
                if bnd[0][0] <= param <= bnd[0][1] or bnd[1][0] <= param <= bnd[1][1]:
                    found = True
            if not found:
                break
        if found:
            valid_tickets.append(tkt)



    pass






    print(f'Error rate: {error_rate}')

if __name__ == '__main__':
    main()

#Answer = 26026