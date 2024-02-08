'''
Advent of Code 2023
Day 17
https://adventofcode.com/2023/day/17

Site that helped me with the search algorythm:
https://www.redblobgames.com/pathfinding/a-star/introduction.html

Other site that helped me with coding ideas:
https://github.com/PhunkyBob/adventofcode/blob/master/2023/day_17_viz.py

'''

from typing import NamedTuple, List, Dict
from queue import PriorityQueue
from enum import Enum
from dataclasses import dataclass, field

DAY = '17'


class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)


class Coord(NamedTuple):
    r: int
    c: int

    def __add__(self, direction: Direction) -> 'Coord':
        return Coord(self.r + direction.value[0], self.c + direction.value[1])


class Block(NamedTuple):
    coord: Coord
    dir: Direction
    direction_count: int
    priority: int

    def opposite_direction(self) -> Direction:
        match self.dir:
            case Direction.UP:
                return Direction.DOWN
            case Direction.RIGHT:
                return Direction.LEFT
            case Direction.DOWN:
                return Direction.UP
            case Direction.LEFT:
                return Direction.RIGHT

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Block=field(compare=False)


def get_input(filename: str) -> List[List[int]]:
    matrix: Dict([Coord, int]) = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for row, line in enumerate(f.readlines()):
            for col, value in enumerate(line.strip()):
                matrix[Coord(row, col)] = int(value)
    end = Coord(row, col)
    return matrix, end


def take_step(cur_block, step_dir, frontier, matrix, cost, end):

    maxstep = 3
    if step_dir == cur_block.opposite_direction():
        return None

    cur_priority = cur_block.priority
    new_coord = cur_block.coord + step_dir
    if (new_coord.r < 0 or new_coord.r > end.r
        or new_coord.c < 0 or new_coord.c > end.c):
        return None  # Stepped beyond the bounds of our heatmap

    new_dir_count = cur_block.direction_count + 1  if cur_block.dir == step_dir else 1
    if new_dir_count > maxstep:
        return None  # Took too many steps.

    new_priority = cur_priority + matrix[new_coord]
    if new_coord not in cost or new_priority <= cost[new_coord].priority:
        cost[new_coord] = Block(new_coord, step_dir, new_dir_count, new_priority)
        frontier.put(PrioritizedItem(new_priority, Block(new_coord, step_dir, new_dir_count, new_priority)))
        return (Block(new_coord, step_dir, new_dir_count, new_priority))   
    else:
        return None


def findshortestpath(matrix: List[List[int]], end: Coord) -> int:

    start = Coord(r=0, c=0)

    frontier: PriorityQueue(int, Block) = PriorityQueue()
    cost_so_far: Dict[Coord, Block] = {}

    frontier.put(PrioritizedItem(0, Block(start, 'NA', 0, 0)))
    cost_so_far[start] = Block(start, 'NA', 0, 0)

    while not frontier.empty():
        frontier_block = frontier.get().item
        if frontier_block.coord == end:
            break

        for step_direction in Direction:
            next_block = frontier_block
            while True:
                current_block = next_block
                next_block = take_step(current_block, step_direction, frontier, matrix, cost_so_far, end)
                if not next_block:
                    break
    
    return cost_so_far[end].priority


def main():

    input_filename = f'./Day-{DAY}/input-example.txt'
    #input_filename = f'./Day-{DAY}/input.txt'

    heatmap, end = get_input(input_filename)
    path = findshortestpath(heatmap, end)
    print(f'The shortest path is: {path}')


if __name__ == '__main__':
    main()
