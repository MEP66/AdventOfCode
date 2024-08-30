

DAY = '03'

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [[int(x) for x in line.strip().split()] for line in f]
    
    are_triangles = 0

    for lines in chunks(input_data, 3):
        for i in range(3):
            if (lines[0][i] + lines[1][i] > lines[2][i] and
                lines[1][i] + lines[2][i] > lines[0][i] and
                lines[2][i] + lines[0][i] > lines[1][i]):
                are_triangles += 1
        
    print(are_triangles)

if __name__ == '__main__':
    main()

#Answer = 1921