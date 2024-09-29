

DAY = '09'

def eval_marker(string):
    i = 0
    count = 0
    while True:
        if string[i:i + 1] == '(':
            ie = string.find(')', i + 1)
            (numchars, numtimes) = [int(x) for x in string[i + 1 : ie].split('x')]
            substr = string[ie + 1: ie + 1 + numchars]
            
            count += numtimes * eval_marker(substr)
            i = ie + 1 + numchars
        else:
            i += 1
            count += 1
        
        if i > len(string):
            count -= 1
            break
    
    return count


def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().strip()

    count = eval_marker(input_data)
    
    print(f'Uncompressed length:  {count}')

if __name__ == '__main__':
    main()

#Answer = 11107527530