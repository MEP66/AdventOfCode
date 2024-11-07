

DAY = '18'

#SERIALNO = 18
SERIALNO = 9221


def main():
    #filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    #filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    #with open(filename, 'r', encoding='utf-8') as f:
        
    grid = list()
    for y in range(1, 301):
        row = list()
        for x in range(1, 301):
            rackID = x + 10
            pl = ((rackID * y) + SERIALNO) * rackID
            if pl < 100:
                pl = 0
            else:
                pl = int(str(pl)[-3]) - 5
            row.append(pl)
        grid.append(row)

    max_pl = 0

    for gs in range(1, 301):
        for y in range(300-gs+1):
            for x in range(300-gs+1):
                sum_pl = sum(grid[y+xs][x+ys] for ys in range(gs) for xs in range(gs))
                if sum_pl > max_pl:
                    max_coord = (x+1, y+1, gs, max_pl)
                    max_pl = sum_pl
    
        print(f'Max coord: {max_coord}, current gs: {gs}')

    pass
    

if __name__ == '__main__':
    main()

#Answer = 143,57,10
