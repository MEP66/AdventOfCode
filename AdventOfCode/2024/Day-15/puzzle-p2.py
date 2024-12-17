from collections import namedtuple

DAY = '15'

Coord = namedtuple('Coord', ['c', 'r'])

# Coordinates are in (x, y) or (c, r) format, with + down and right.

move_dir = {'^': Coord(c=0, r=-1), '>': Coord(c=1, r=0),
            'v': Coord(c=0, r=1), '<': Coord(c=-1, r=0)}


def is_free(coord_list, dir, fmap):
    free_list = list()
    for cur_col, cur_row in coord_list:
        nbr_coord = Coord(cur_col + move_dir[dir].c, cur_row + move_dir[dir].r)
        match fmap[nbr_coord.r][nbr_coord.c]:
            case '.':
                free_list.append(True)
            case '#':
                free_list.append(False)
            case '[':
                if dir in ['^', 'v']:
                    free_list.append(is_free([nbr_coord, Coord(nbr_coord.c+1, nbr_coord.r)], dir, fmap))
                elif dir == '>':
                    free_list.append(is_free([Coord(nbr_coord.c+1, nbr_coord.r)], dir, fmap))
                else:
                    print(f'Error. This should not have been encountered.') # <[ shoudl not occur
            case ']':
                if dir in ['^', 'v']:
                    free_list.append(is_free([Coord(nbr_coord.c-1, nbr_coord.r), nbr_coord], dir, fmap))
                elif dir == '<':
                    free_list.append(is_free([Coord(nbr_coord.c-1, nbr_coord.r)], dir, fmap))
                else:
                    print(f'Error. This should not have been encountered.') # >] shoudl not occur
    return all(free_list)


def move_it(coord_list, dir, fmap):
    for cur_col, cur_row in coord_list:
        nbr_coord = Coord(cur_col + move_dir[dir].c, cur_row + move_dir[dir].r)
        match fmap[nbr_coord.r][nbr_coord.c]:
            case '.':
                pass
            case '[':
                if dir in ['^', 'v']:
                    move_it([nbr_coord], dir, fmap)
                    #move_it([nbr_coord, Coord(nbr_coord.c+1, nbr_coord.r)], dir, fmap)
                    fmap[nbr_coord.r+move_dir[dir].r][nbr_coord.c+1] = ']'
                    fmap[nbr_coord.r][nbr_coord.c+1] = '.'
                elif dir == '>':
                    move_it([Coord(nbr_coord.c+1, nbr_coord.r)], dir, fmap)
                    fmap[nbr_coord.r][nbr_coord.c+1] = '['
                    fmap[nbr_coord.r][nbr_coord.c] = '.'

                else:
                    print(f'Error. This should not have been reached.') # <[ should not be hit
            case ']':
                if dir in ['^', 'v']:
                    move_it([nbr_coord], dir, fmap)
                    #move_it([Coord(nbr_coord.c-1, nbr_coord.r), nbr_coord], dir, fmap)
                    fmap[nbr_coord.r+move_dir[dir].r][nbr_coord.c-1] = '['
                    fmap[nbr_coord.r][nbr_coord.c-1] = '.'
                elif dir == '<':
                    move_it([Coord(nbr_coord.c-1, nbr_coord.r)], dir, fmap)
                    fmap[nbr_coord.r][nbr_coord.c-1] = ']'
                    fmap[nbr_coord.r][nbr_coord.c] = '.'
                else:
                    print(f'Error. This should not have been reached.') # >] shoult not be hit
            case '#':
                print(f'Error. This should not have been reached.')
        fmap[nbr_coord.r][nbr_coord.c] = fmap[cur_row][cur_col]
        fmap[cur_row][cur_col] = '.'
    return nbr_coord

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    #filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [[x for x in line] for line in f.read().splitlines()]

    for ri, line in enumerate(input_data):
        if not line:
            break
   
    floor_map = list()
    for line in input_data[:ri]:
        floor_line = list()
        for obj in line:
            match obj:
                case '#':
                    new_obj = ['#', '#']
                case 'O':
                    new_obj = ['[', ']']
                case '.':
                    new_obj = ['.', '.']
                case '@':
                    new_obj = ['@', '.']
            floor_line.extend(new_obj)
        floor_map.append(floor_line)
    
    instructions = list()
    for line in input_data[ri+1:]:
        instructions.extend(line)

    del input_data

    for ri, row in enumerate(floor_map):
        for ci, obj in enumerate(row):
            if obj == '@':
                robot_loc = Coord(c=ci, r=ri)
                break
        else:
            continue
        break

    for mv_dir in instructions:
        if is_free([robot_loc], mv_dir, floor_map):
            robot_loc = move_it({robot_loc}, mv_dir, floor_map)

    sum_gps = 0
    for ri, row in enumerate(floor_map):
        for ci, obj in enumerate(row):
            if obj == '[':
                sum_gps += 100 * ri + ci
    
    print(f'GPS sum = {sum_gps}')

if __name__ == '__main__':
    main()

#Answer = 1371036