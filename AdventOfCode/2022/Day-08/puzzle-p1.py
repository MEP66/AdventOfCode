
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
    result = [[0] * width for i in range(height)]

    tallest = -1
    for r in range(height):
        tallest = -1
        for c in range(width):
            if matrix[r][c] > tallest:
                tallest = matrix[r][c]
                result[r][c] = 1
    tallest = -1
    for c in range(width):
        tallest = -1
        for r in range(height):
            if matrix[r][c] > tallest:
                tallest = matrix[r][c]
                result[r][c] = 1
    tallest = -1
    for r in range(height):
        tallest = -1
        for c in range(width-1, 0, -1):
            if matrix[r][c] > tallest:
                tallest = matrix[r][c]
                result[r][c] = 1
    tallest = -1
    for c in range(width-1, 0, -1):
        tallest = -1
        for r in range(height-1,0, -1):
            if matrix[r][c] > tallest:
                tallest = matrix[r][c]
                result[r][c] = 1

    print(sum(sum(result, [])))

if __name__ == '__main__':
    main()

# Answer = 1859