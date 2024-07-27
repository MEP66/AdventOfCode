

DAY = '03'

def main():
    #filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read()

    x = y = 1
    all_visited = {(x, y)}

    for direction in input_data:
        match direction:
            case '^':
                y += 1
            case '>':
                x += 1
            case 'v':
                y -= 1
            case '<':
                x -= 1

        all_visited.add((x, y))
    
    print(len(all_visited))
    

if __name__ == '__main__':
    main()

#Answer = 2572