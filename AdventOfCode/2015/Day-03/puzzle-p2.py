

DAY = '03'

def main():
    #filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read()

    sx = sy = 1
    rsx = rsy = 1
    all_visited = {(sx, sy)}
    santa = True

    for direction in input_data:
        if santa:
            x = sx
            y = sy
        else:
            x = rsx
            y = rsy
       
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
        if santa:
            sx = x
            sy = y
        else:
            rsx = x
            rsy = y
        
        santa = not santa
    
    print(len(all_visited))
    

if __name__ == '__main__':
    main()

#Answer = 2631