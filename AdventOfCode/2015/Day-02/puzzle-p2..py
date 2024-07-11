

DAY = '02'

def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
          input_data = f.read().splitlines()

    total_sq_wrap = 0

    for line in input_data:
         l, w, h = map(int, line.split('x'))
         total_sq_wrap += ((l * w * h) + min(2*l+2*w, 2*l+2*h, 2*w+2*h))
        
    print(total_sq_wrap)


if __name__ == '__main__':
    main()


#Answer = 3812909