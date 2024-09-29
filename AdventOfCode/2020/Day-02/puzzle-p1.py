import re
from dataclasses import dataclass
from collections import Counter

DAY = '02'

@dataclass
class Inp:
    min: int
    max: int
    schar: str
    sstr: str

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    passwords = list()
    for line in input_data:
        params = re.search(r'(\d+)-(\d+) (.): (.+)', line)
        passwords.append(Inp(min=int(params[1]), max=int(params[2]), schar=params[3], sstr=params[4]))

    arevalid = 0
    for entry in passwords:
        counts = Counter(entry.sstr)
        if entry.min <= counts[entry.schar] <= entry.max:
            arevalid += 1
    
    print(f'Number of valid passwords is: {arevalid}')

if __name__ == '__main__':
    main()

#Answer = 666