from collections import defaultdict, namedtuple
from math import inf
from heapq import heapify, heappop, heappush


DAY = '21'


#Coordinates are in (x, y) or (c, r) format with + down and right.

Coord = namedtuple('Coord', ['c', 'r'])
moves = {'^': -1, '>': 1, 'v': 1, '<': -1}


class Robot:
    def __init__(self, keys):
        # Create a dictionary of Key coordinates and initialize start position to the 'A' key.
        self._key_coords = dict()
        for ri, row in enumerate(keys):
            for ci, k in enumerate(row):
                if k != '#':
                    self._key_coords[k] = Coord(ci, ri)
                else:
                    self._invalid_key_coord = Coord(ci, ri) # There is only one of these
        self._cur_key_ptr = self._key_coords['A']

    def reset(self):
        self._cur_key_ptr = self._key_coords['A']
    
    def press(self, dkey):
        d_coord = self._key_coords[dkey]
        move_coords = list()
        xmove_keys = str()
        ymove_keys = str()
        x_steps = d_coord.c - self._cur_key_ptr.c
        y_steps = d_coord.r - self._cur_key_ptr.r
        xpos = self._cur_key_ptr.c
        ypos = self._cur_key_ptr.r
        move_dir = 1
        if x_steps > 0:
            move_dir = 1
            xkey = '>'
        else:
            move_dir = -1
            xkey = '<'
        for _ in range(abs(x_steps)):
            move_coords.append(Coord(xpos := xpos+move_dir, ypos))
            xmove_keys = xmove_keys + xkey

        if y_steps > 0:
            move_dir = 1
            ykey = 'v'
        else:
            move_dir = -1
            ykey = '^'
        for x in range(abs(y_steps)):
            move_coords.append(Coord(xpos, ypos := ypos+move_dir))
            ymove_keys = ymove_keys + ykey

        self._cur_key_ptr = Coord(xpos, ypos)

        if self._invalid_key_coord in move_coords:
            keypath = ymove_keys + xmove_keys
        else:
            keypath = xmove_keys + ymove_keys
        
        return keypath + 'A'


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        keycodes = [line for line in f.read().splitlines()]
    
    # Use '#' to represent invalid location.
    num_keypad = (('789'), ('456'), ('123'), ('#0A'))
    DoorRobot = Robot(num_keypad)

    dir_keypad = (('#^A'), ('<v>'))
    CntlRobot = Robot(dir_keypad)
    MeRobot = Robot(dir_keypad)

    result = 0

    for sequence in keycodes:
        #DoorRobot.reset()
        #CntlRobot.reset()
        #MeRobot.reset()
        final_keysequence = list()
        
        final_keysequence = ''
        for key in sequence:
            movements1 = DoorRobot.press(key)
            movements2 = ''
            for key1 in movements1:
                movements2 = movements2 + CntlRobot.press(key1)
            movements3 = ''
            for key2 in movements2:
                movements3 = movements3 + MeRobot.press(key2)
                
            final_keysequence += movements3
        pass
        result += (len(final_keysequence) * int(sequence[:3]))
    
    print(f'Final result = {result}')
    pass

if __name__ == '__main__':
    main()

#Answer - 252324 is too high