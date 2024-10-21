import re


DAY = '10'

def main():
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()
    
    starmap = list()
    for line in input_data:
        starmap.append([int(x) for x in re.findall(r'-?\d+', line)])

    diffy = max(y[1] for y in starmap) - min(y[1] for y in starmap)

    t = 0
    while True:
        for line in starmap:
            line[0] += line[2]
            line[1] += line[3]
        t += 1

        miny = min(y[1] for y in starmap)
        maxy = max(y[1] for y in starmap)

        if maxy - miny < diffy:
            diffy = maxy - miny
        else:
            break

    for line in starmap:
        line[0] -= line[2]
        line[1] -= line[3]
    minx = min(x[0] for x in starmap)
    maxx = max(x[0] for x in starmap)
    miny = min(y[1] for y in starmap)
    maxy = max(y[1] for y in starmap)
    t -= 1

    final_pts = [(x[0], x[1]) for x in starmap]
    page = list()
    for y in range(miny, maxy+1):
        line = list()
        for x in range(minx, maxx+1):
            if (x, y) in final_pts:
                line.append('#')
            else:
                line.append(' ')
        page.append(line)

    for line in page:
        print(f'{''.join(line)}')
    print(f'Time: {t} seconds')

if __name__ == '__main__':
    main()

#Answer p1 = CPJRNKCF
#Answer p2 = 10345