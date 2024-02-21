
DAY = '08'

def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    matrix = []
    with open(filename, 'r', encoding='utf-8') as f:
        line = f.readline().strip()
        while line:
            row = [int(c) for c in line]
            matrix.append(row)
            line = f.readline().strip()
    
    width = len(matrix[0])
    height = len(matrix)
    maxvisibility = 0

    for rcur in range(height):
        for ccur in range(width):
            visright, visleft, visdown, visup = 0, 0, 0, 0
            curheight = matrix[rcur][ccur]
            if not (rcur == 0 or rcur == (height-1) or ccur == 0 or ccur == (width-1)):

                # look down
                c = ccur
                for r in range(rcur+1, height):
                    visdown += 1
                    if matrix[r][c] >= curheight:
                        break
                # look up
                c = ccur
                for r in range(rcur-1, -1, -1):
                    visup += 1
                    if matrix[r][c] >= curheight:
                        break

                # look right
                r = rcur
                for c in range(ccur+1, width):
                    visright += 1
                    if matrix[r][c] >= curheight:
                        break
            
                # look left
                r = rcur
                for c in range(ccur-1, -1, -1):
                    visleft += 1
                    if matrix[r][c] >= curheight:
                        break

            visibility = visleft * visright * visdown * visup
            
            maxvisibility = max(maxvisibility, visibility)

    print(f'The max visibility score is: {maxvisibility}')


if __name__ == '__main__':
    main()

# Answer = 332640