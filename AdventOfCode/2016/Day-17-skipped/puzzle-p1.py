import hashlib
from math import inf

# https://www.geeksforgeeks.org/md5-hash-python/


DAY = '17'

PASSCODE = 'ihgpwlah'
#PASSCODE = 'kglvqrro'
#PASSCODE = 'ulqzkmiv'
#PASSCODE = 'awrkjxxr'

CLOSED = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a')
OPEN = ('b', 'c', 'd', 'e', 'f')

HASHDIR = ('U', 'D', 'L', 'R')

START = (0, 0)  # in (x, y) or (c, r)
END = (3, 3)
vaultmap = {(0, 0): {'D': (0, 1), 'R': (1, 0)},
            (1, 0): {'D': (1, 1), 'L': (0, 0), 'R': (2, 0)},
            (2, 0): {'D': (2, 2), 'L': (1, 0), 'R': (3, 0)},
            (3, 0): {'D': (3, 3), 'L': (2, 0)},
            (0, 1): {'U': (0, 0), 'D': (0, 2), 'R': (1, 1)},
            (1, 1): {'U': (1, 0), 'D': (1, 2), 'L': (0, 1), 'R': (2, 1)},
            (2, 1): {'U': (2, 0), 'D': (2, 2), 'L': (1, 1), 'R': (3, 1)},
            (3, 1): {'U': (3, 0), 'D': (3, 3), 'L': (2, 1)},
            (0, 2): {'U': (0, 1), 'D': (0, 3), 'R': (1, 1)},
            (1, 2): {'U': (1, 1), 'D': (1, 3), 'L': (0, 1), 'R': (2, 1)},
            (2, 2): {'U': (2, 1), 'D': (2, 3), 'L': (1, 1), 'R': (3, 1)},
            (3, 2): {'U': (3, 1), 'D': (3, 3), 'L': (2, 1)},
            (0, 3): {'U': (0, 2), 'R': (1, 3)},
            (1, 3): {'U': (1, 2), 'L': (0, 3), 'R': (2, 3)},
            (2, 3): {'U': (2, 2), 'L': (1, 3), 'R': (3, 3)},
            (3, 3): {'U': (3, 2), 'L': (2, 3)}
            }

def get_neighbors(s, hcode):
    neighbors = list()
    for i, d in enumerate(HASHDIR):
        if d in vaultmap[s] and hcode[i] in OPEN:
            neighbors.append((vaultmap[s][d], d))
    return neighbors

def get_shortest_path(s, e, cpth, pcode, shortestpath):
    
    hash = hashlib.md5(pcode.encode()).hexdigest()

    for nbrc, dir in get_neighbors(s, hash):
        if nbrc == END:
            return dir
        else:
            cpth = cpth + get_shortest_path(nbrc, e, cpth, pcode + dir, shortestpath)
            if len(cpth) < shortestpath[1]:
                shortestpath = (len(cpth), cpth)
    return shortestpath

def main():

    shortestpath = (inf, '')
    currentpath = ''
    currentpos = START

    path = get_shortest_path(currentpos, END, currentpath, PASSCODE, shortestpath)

    print(f'Shortest path = {path}')


if __name__ == '__main__':
    main()
