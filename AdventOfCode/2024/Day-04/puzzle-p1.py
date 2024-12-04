from collections import Counter


DAY = '04'

#Coordinates are in (x, y) or (c, r)
DIR = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

def get_letters(scoord, dir, cnt, lmap):
    ncoord = (scoord[0] + dir[0], scoord[1] + dir[1])
    if 0 <= ncoord[0] < len(lmap) and 0 <= ncoord[1] < len(lmap[0]):
        letter = lmap[ncoord[1]][ncoord[0]]
        cnt -= 1
        if cnt > 0:
            if next_letter := get_letters(ncoord, dir, cnt, lmap):
                return letter + next_letter
            else:
                return letter
        else:
            return letter
    else:
        return None

def get_words(coord, puzmap):
    ci, ri = coord
    words = list()
    for d in DIR:
        if new_word := get_letters(coord, d, 3, puzmap):
            words.append(puzmap[ri][ci] + new_word)
    return words

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        puzzle = [[c for c in line] for line in f.read().splitlines()]

    word_count = Counter()

    for ri, row in enumerate(puzzle):
        for ci, char in enumerate(row):
            if char == 'X':
                word_count.update(get_words((ci, ri), puzzle))
    print(f'Total XMAS count: {word_count["XMAS"]}')
    

if __name__ == '__main__':
    main()

#Answer = 2554