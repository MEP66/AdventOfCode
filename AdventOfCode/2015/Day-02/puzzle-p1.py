

DAY = '02'

def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
          input_data = f.read().splitlines()

    total_sq_wrap = 0

    for line in input_data:
         l, w, h = map(int, line.split('x'))
         total_sq_wrap += ((l*w*2 + l*h*2 + w*h*2) + min(l*w, l*h, w*h))
        
    print(total_sq_wrap)


if __name__ == '__main__':
    main()

#Answer = 1598415