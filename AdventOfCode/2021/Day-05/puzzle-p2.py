from dataclasses import dataclass
from collections import defaultdict
import re


DAY = '05'

@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    coordmap = list()
    for line in input_data:
        nums = [int(n) for n in re.split(',| -> ', line)]
        coordmap.append(Line(x1=nums[0], y1=nums[1], x2=nums[2], y2=nums[3]))
    
    visited = defaultdict(lambda: 0)

    for line in coordmap:
        if line.x1 == line.x2:
            x = line.x1
            for y in range(min(line.y1, line.y2), max(line.y1, line.y2) + 1):
                visited[(x, y)] += 1

        elif line.y1 == line.y2:
            y = line.y1
            for x in range(min(line.x1, line.x2), max(line.x1, line.x2) + 1):
                visited[(x, y)] += 1
    
        else:
            if line.x1 < line.x2:
                xinc = 1
                xe = line.x2 + 1
            else:
                xinc = -1
                xe = line.x2 - 1
            
            if line.y1 < line.y2:
                yinc = 1
            else:
                yinc = -1
            
            x = line.x1
            y = line.y1
            while True:
                visited[(x, y)] += 1
                x += xinc
                y += yinc
                if x == xe:
                    break

    count = 0
    for key, value in visited.items():
        if value >= 2:
            count +=1
    
    print(f'Count of spaces visited more than once is: {count}')

if __name__ == '__main__':
    main()

#Answer = 22364