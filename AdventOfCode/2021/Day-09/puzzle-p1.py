

DAY = '09'

adjacents = ((-1, 0), (0, 1), (1, 0), (0, -1))

def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    risk_total = 0

    with open(filename, 'r', encoding='utf-8') as f:
        floor_map = [[int(c) for c in line] for line in f.read().splitlines()]
        
    for ri, line in enumerate(floor_map):
        for ci, hgt in enumerate(line):
            lowest = True
            for ra, ca in adjacents:
                row_i = ri + ra
                col_i = ci + ca
                if row_i >= 0 and col_i >= 0:
                    try:
                        if hgt >= floor_map[ri+ra][ci+ca]:
                            lowest = False
                    except IndexError:
                        pass
            if lowest: 
                risk_total += (hgt + 1)
    
    print(f'Total Risk: {risk_total}')
    

if __name__ == '__main__':
    main()

#Answer = 560