import re
from dataclasses import dataclass

DAY = '06'

@dataclass
class Point():
    c: int = 0
    r: int = 0

@dataclass
class Instr():
    cmd: str
    s: Point
    e: Point


def adjust_lights(input_map: list, command, start: Point, end: Point):
    for row in range(start.r, end.r + 1):
        for col in range(start.c, end.c + 1):
            input_map[row][col] = command(input_map[row][col])


def main():
    #filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    instructions = []
    for line in input_data:
        command = re.match('(.*?) [0-9]', line)[1]
        points = list(map(int, re.findall('[0-9]+', line)))
        instructions.append(Instr(cmd = command, s = Point(points[0], points[1]), e = Point(points[2], points[3])))

    light_map = [[0 for r in range(1000)] for c in range(1000)]
    turniton = lambda i: i + 1
    turnitoff = lambda i: max(0, i - 1)
    toggleit = lambda i: i + 2

    for instruction in instructions:
        match instruction.cmd:
            case 'turn on':
                adjust_lights(light_map, turniton, instruction.s, instruction.e)

            case 'turn off':
                adjust_lights(light_map, turnitoff, instruction.s, instruction.e)

            case 'toggle':
                adjust_lights(light_map, toggleit, instruction.s, instruction.e)

    total_lit = 0
    for r in light_map:
        total_lit += sum(r)
    print(total_lit)

if __name__ == '__main__':
    main()

#Answer = 14110788