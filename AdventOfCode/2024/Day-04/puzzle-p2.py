

DAY = '04'

#Coordinates are in (x, y) or (c, r) with + right and down

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
    

def is_x_mas(coord, puzmap):
    ci, ri = coord
    x1 = get_letters((ci-1, ri-1), (1, 1), 3, puzmap)
    x2 = get_letters((ci+1, ri-1), (-1, 1), 3, puzmap)
    if x1 in ['MAS', 'SAM'] and x2 in ['MAS', 'SAM']:
        return True
    return False


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        puzzle = [[c for c in line] for line in f.read().splitlines()]

    x_mas_count = 0

    for ri, row in enumerate(puzzle):
        for ci, char in enumerate(row):
            if char == 'A':
                if is_x_mas((ci, ri), puzzle):
                    x_mas_count += 1
    print(f'Total X-MAS count: {x_mas_count}')
    

if __name__ == '__main__':
    main()

#Answer = 1916