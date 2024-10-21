import re
from itertools import cycle


DAY = '09'
SPCL_CASE = 23
BACKTRACK = 7

class DLCL():
    def __init__(self, ival):
        self._dlcl = dict()
        self._dlcl[ival] = {'cw' : ival, 'ccw' : ival}
        self. _hdr = ival

    def cw1ni(self, nval):
        # Advance clockwise one node and insert after. Insertion becomes header.

        self._hdr = self._dlcl[self._hdr]['cw']
        ccwn = self._hdr
        cwn = self._dlcl[self._hdr]['cw']
        self._dlcl[nval] = {'cw' :  cwn, 'ccw' : ccwn}
        self._dlcl[ccwn]['cw']= nval
        self._dlcl[cwn]['ccw'] = nval
        self._hdr = nval

    def ccw(self, nmov):
        # Advance counterclockwise x nodes and return value.
        
        for _ in range(nmov):
            self._hdr = self._dlcl[self._hdr]['ccw']
        return self._hdr
    
    def rmitem(self):
        # remove current item from list and set header to next clockwise node.

        _toremove = self._hdr
        ccwn = self._dlcl[self._hdr]['ccw']
        cwn = self._dlcl[self._hdr]['cw']
        self._dlcl[cwn]['ccw'] = ccwn
        self._dlcl[ccwn]['cw'] = cwn
        self._hdr = cwn
        del self._dlcl[_toremove]

def main():
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in re.findall(r'(\d+) players; last marble is worth (\d+) points', f.read())[0]]
        
    players, lvalue = input_data
    lvalue *= 100

    scores = dict.fromkeys(range(1, players + 1), 0)
    players_iter = cycle(scores.keys())
    
    player = next(players_iter)
    circle = DLCL(0)

    for marble in range(1, lvalue+1):
        player = next(players_iter)
        if marble % SPCL_CASE == 0:
            scores[player] += marble
            scores[player] += circle.ccw(BACKTRACK)
            circle.rmitem()
        else:
            circle.cw1ni(marble)

    print(f'Winning sore: {max(scores.values())}')
    

if __name__ == '__main__':
    main()

#Answer = 3277920293
