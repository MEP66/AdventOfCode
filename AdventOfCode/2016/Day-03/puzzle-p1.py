

DAY = '03'

def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [[int(x) for x in line.strip().split()] for line in f]
    
    are_triangles = 0
    for line in input_data:
        if (line[0] + line[1] > line[2] and
            line[1] + line[2] > line[0] and
            line[2] + line[0] > line[1]):
            are_triangles += 1
        
    print(are_triangles)

if __name__ == '__main__':
    main()

#Answer = 1050