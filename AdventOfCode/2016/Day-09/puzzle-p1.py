

DAY = '09'

def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().strip()

    i = 0
    count = 0
    while True:
        if input_data[i:i + 1] == '(':
            ie = input_data.find(')', i + 1)
            (numchars, numtimes) = [int(x) for x in input_data[i + 1 : ie].split('x')]
            count += (numchars * numtimes)
            i = ie + 1 + numchars
        else:
            i += 1
            count += 1
        
        if i > len(input_data):
            count -= 1
            break
    
    print(f'Uncompressed length:  {count}')

if __name__ == '__main__':
    main()

#Answer = 115118