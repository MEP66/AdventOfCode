from collections import namedtuple
import re

DAY = '15'

XY = namedtuple('XY', ['x', 'y'])
SB = namedtuple('SB', ['s', 'b'])

def mandist(pts):
    return (abs(pts.s.x - pts.b.x) + abs(pts.s.y - pts.b.y))


def findnotb(sen, row, dist):
    if abs(sen.y - row) > dist:
        return None
    else:
        impact = abs(abs(sen.y - row) - dist)
    return (sen.x - impact, sen.x + impact) 

# https://stackoverflow.com/questions/6821156/how-to-find-range-overlap-in-python

def findoverlap(r1, r2):
    if r1[0] <= r2[1] and r2[0] <= r1[1]:
        return (min(r1[0], r2[0]), max(r1[1], r2[1]))
    else:
        return None


def sumup(nblist):
    nbsum = 0
    while nblist:
        current = nblist[0]
        nblist.pop(0)
        isoverlap = False
        for i in range(0, len(nblist)):
            overlap = findoverlap(current, nblist[i])
            if overlap:
                nblist.pop(i)
                nblist.append(overlap)
                isoverlap = True
        if not isoverlap:
            nbsum += abs(current[0] - current[1] + 1)
    nbsum += 1  # not sure why???
    return nbsum



def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()
    
    allSB = set()
    for line in input_data:
        points = re.findall(r'-?\d+', line)
        ipoints = list(map(int, points))
        allSB.add(SB(s=XY(x=ipoints[0], y=ipoints[1]), b=XY(x=ipoints[2], y=ipoints[3])))
    
    roi = 10
    roi = 2000000
    notbeacon = []

    for sb in allSB:
        d = mandist(sb)
        binter = findnotb(sb.s, roi, d)
        if binter:
            notbeacon.append(binter)
    
    count = sumup(notbeacon)

    print(f'Total count of non-beacon positions in row {roi} is {count}')
     

if __name__ == '__main__':
    main()

#Answer = 5256611