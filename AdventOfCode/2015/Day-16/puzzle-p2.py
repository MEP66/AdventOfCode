import re

DAY = '16'

def main():
    ticker_tape = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

    #filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()
    
    sues_pass = list()

    for line in input_data:
        params = re.split(': |, ', line)
        failed_check = False
        for i in range(1, 7, 2):
            if params[i] in ticker_tape:
                if params[i] in ['cats', 'trees']:
                    if int(params[i + 1]) <= ticker_tape[params[i]]:
                        failed_check = True
                elif params[i] in ['pomeranians', 'goldfish']:
                    if int(params[i + 1]) >= ticker_tape[params[i]]:
                        failed_check = True
                else:
                    if int(params[i + 1]) != ticker_tape[params[i]]:
                        failed_check = True
        if not failed_check:
            sues_pass.append(params[0])

    print(sues_pass)

if __name__ == '__main__':
    main()

#Answer = 241