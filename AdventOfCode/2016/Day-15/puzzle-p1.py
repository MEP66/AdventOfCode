import re
import itertools
from dataclasses import dataclass


DAY = '15'
SPATTERN = r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).'

@dataclass
class BtnPress:
    time: int()
    discpos: int()
    valid: bool()

def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    discs = dict()
    for line in input_data:
        discnum, size, start = [int(x) for x in re.search(SPATTERN, line).groups()]
        discs[discnum] = {'discpos' : None, 'iter' : itertools.cycle(range(size))}
        discs[discnum]['dispos'] = next(discs[discnum]['iter'])
        for _ in range(start):
            discs[discnum]['discpos'] = next(discs[discnum]['iter'])
    last_disc = discnum

    t = 0
    buttonpresses = list()
    found = False

    while not found:
        t += 1
        for disc in discs:
            discs[disc]['discpos'] = next(discs[disc]['iter'])

        for buttonpress in buttonpresses:
            if discs[buttonpress.discpos + 1]['discpos'] == 0:
                buttonpress.discpos += 1
                if buttonpress.discpos == last_disc:
                    print(f'Button press at time {buttonpress.time} was successful.')
                    found = True
            else:
                buttonpress.valid = False


        if discs[1]['discpos'] == 0:
            buttonpresses.append(BtnPress(t-1, 1, True))

        buttonpresses = [bp for bp in buttonpresses if bp.valid]

    pass

if __name__ == '__main__':
    main()

#Answer: 121834