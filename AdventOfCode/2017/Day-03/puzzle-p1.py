from dataclasses import dataclass

@dataclass
class Loc:
    r: int
    c: int

@dataclass
class Bndry:
    mn: int
    mx: int

move = {'R': (0, 1), 'U': (-1, 0), 'L': (0, -1), 'D': (1, 0)}

DAY = '03'

def main():

    target = 361527

    data = 1
    dataloc = Loc(r = 0, c = 0)
    rowbndry = Bndry(mn = 0, mx = 0)
    colbndry = Bndry(mn = 0, mx = 0)

    currentdir = 'R'

    while data != target:
        data += 1
        dataloc = Loc(dataloc.r + move[currentdir][0], dataloc.c + move[currentdir][1])
        match currentdir:
            case 'R':
                if dataloc.c > colbndry.mx:
                    colbndry.mx = dataloc.c
                    currentdir = 'U'

            case 'U':
                if dataloc.r < rowbndry.mn:
                    rowbndry.mn = dataloc.r
                    currentdir = 'L'

            case 'L':
                if dataloc.c < colbndry.mn:
                    colbndry.mn = dataloc.c
                    currentdir = 'D'

            case 'D':
                if dataloc.r > rowbndry.mx:
                    rowbndry.mx = dataloc.r
                    currentdir = 'R'

    print(dataloc, (abs(dataloc.r) + abs(dataloc.c)))

if __name__ == '__main__':
    main()

#Answer = 326