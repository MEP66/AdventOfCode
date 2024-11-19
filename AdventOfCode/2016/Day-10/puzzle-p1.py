from dataclasses import dataclass
import re


DAY = '10'

MC_WATCH = {2, 5}
MC_WATCH = {17, 61}


@dataclass
class Input:
    bot: int()
    val: int()

class Bot:
    instances = dict()
    
    def __init__(self, num, low=None, high=None):
        self._num = num
        self._regs = list()
        self._low = low
        self._high = high
        Bot.instances[num] = self

    @classmethod
    def get_instances(cls):
        return cls.instances

    @classmethod
    def get(cls, num):
        return cls.instances[num]

    @property
    def regs(self):
        return self._regs
    
    @regs.setter
    def regs(self, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        self._regs.append(value)
        if len(self._regs) == 2:
            if set(self._regs) == MC_WATCH:
                print(f'Bot number {self._num} triggered on the watch.')
            if self._low[0] == 'out':
                print(f'Output number {self._low[1]} from bot {self._num} is value {min(self._regs)}')
            else:
                Bot.get(self._low[1]).regs= min(self._regs)
            if self._high[0] == 'out':
                print(f'Output number {self._high[1]} from bot {self._num} is value {max(self._regs)}')
            else:
                Bot.get(self._high[1]).regs = max(self._regs)


def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()
    
    inputs = list()
    for line in input_data:
        if line[0] == 'b':
            (sbot, ldtype, ld, hdtype, hd) = [x for x in re.search(r'bot (\d+) gives low to (.+) (\d+) and high to (.+) (\d+)', line).groups()]
            if ldtype == 'bot':
                low_cntr = ('bot', int(ld))
            elif ldtype == 'output':
                low_cntr = ('out', int(ld))
            else:
                print(f'Error in parsing')
            if hdtype == 'bot':
                high_cntr = ('bot', int(hd))
            elif hdtype == 'output':
                high_cntr = ('out', int(hd))
            else:
                print(f'Error in parsing')
            Bot(int(sbot), low=low_cntr, high=high_cntr)
        elif line[0] == 'v':
            (ival, dbot) = [x for x in re.search(r'value (\d+) goes to bot (\d+)', line).groups()]
            inputs.append(Input(bot=int(dbot), val = int(ival)))
        else:
            print(f'Error in parsing')

    for input in inputs:
        Bot.get(input.bot).regs = input.val

    pass

if __name__ == '__main__':
    main()

#Answer p1 = 93
#Answer p2 = 47101