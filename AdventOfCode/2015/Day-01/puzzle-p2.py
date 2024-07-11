

DAY = '01'

def main():
    #filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read()
    
    floor = 0
    for char in input_data:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

    print(floor)

if __name__ == '__main__':
    main()

#Answer = 74