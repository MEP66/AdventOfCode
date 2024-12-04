from collections import Counter

DAY = '04'

#Coordinates are in (x, y) or (c, r)
DIR = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

def get_letters(scoord, dir, cnt, lmap):
    if 0 <= scoord[0] < len(lmap) and 0 <= scoord[1] < len(lmap[0]):
        letter = lmap[scoord[1]][scoord[0]]
        cnt -= 1
        if cnt > 0:
            ncoord = (scoord[0] + dir[0], scoord[1] + dir[1])
            if next_letter := get_letters(ncoord, dir, cnt, lmap):
                return letter + next_letter
            else:
                return letter
        else:
            return letter
    else:
        return None

def num_xmas(coord, puzmap):
    ci, ri = coord
    xmas_count = 0
    for d in DIR:
        if new_word := get_letters(coord, d, 4, puzmap):
            if new_word == 'XMAS':
                xmas_count += 1
    return xmas_count

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        puzzle = [[c for c in line] for line in f.read().splitlines()]

    xmas_count = 0

    for ri, row in enumerate(puzzle):
        for ci, char in enumerate(row):
            if char == 'X':
                xmas_count += num_xmas((ci, ri), puzzle)
    print(f'Total XMAS count: {xmas_count}')
    

if __name__ == '__main__':
    main()

#Answer = 2554