from dataclasses import dataclass


DAY = '13'


@dataclass
class Fold():
    a: str
    num: int


def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    dot_map = list()
    fold_map = list()

    for line in input_data:
        if line.find('fold') != -1:
            temp = line.split('=')
            axis = temp[0][-1]
            count = int(temp[1])
            fold_map.append(Fold(a=axis, num=count))
        elif line.find(',') != -1:
            temp = line.split(',')
            dot_map.append((int(temp[0]), int(temp[1])))
        else:
            pass

    for fi, fold in enumerate(fold_map):
        if fold.a == 'x':
            for di, dot in enumerate(dot_map):
                if dot[0] > fold.num:
                    dot_map[di] = (fold.num-(dot[0]-fold.num), dot[1])

        else:
            for di, dot in enumerate(dot_map):
                if dot[1] > fold.num:
                    dot_map[di] = (dot[0], fold.num-(dot[1]-fold.num))

        dot_map = list(set(dot_map))

        if fi+1 == 1:
            print(len(dot_map))

    num_rows = max([dot[1] for dot in dot_map]) + 1
    num_cols = max([dot[0] for dot in dot_map]) + 1
    
    image = [[' ' for _ in range(num_cols)] for _ in range(num_rows)]
            
    for dot in dot_map:
        image[dot[1]][dot[0]] = '*'
        
    for line in image:
        print(''.join(line))
    
    pass

if __name__ == '__main__':
    main()

#Answer p1 = 737.
#Answer p2 = ZUJUAFHP