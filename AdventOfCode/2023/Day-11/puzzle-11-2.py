# puzzle-11-1.py

def main():
    #filename = r'./Day-11/input-11.txt'
    filename = r'./Day-11/input-11-example.txt'
    EXPANSION = 100

    with open(filename, 'r', encoding='utf-8') as f:
        input = f.readlines()
    
    spacemap = list()
    for line in input:
        spacemap.append([1 if x == '.' else 0 for x in list(line.strip())])
    linelen = len(spacemap[0])
    
    rowexp = []
    for r in range(len(spacemap)-1, 0, -1):
        if all(spacemap[r]):
            rowexp.append(r)

    colexp = []
    for c in range(len(spacemap[0])-1, 0, -1):
        if all([spacemap[r][c] for r in range(len(spacemap))]):
            colexp.append(c)

    # Gather Galaxy locations.
    
    galaxies = [(r, c) for r in range(len(spacemap)) for c in range(len(spacemap[0])) if not spacemap[r][c]]

    # Calculate distances.

    sum = 0
    for o in range(len(galaxies)):
        for i in range(o+1, len(galaxies)):
            dist = abs(galaxies[o][0] - galaxies[i][0]) + abs(galaxies[o][1] - galaxies[i][1])

            
            sum += dist

    print(sum)


if __name__ == '__main__':
    main()

# Answer: 10289334
