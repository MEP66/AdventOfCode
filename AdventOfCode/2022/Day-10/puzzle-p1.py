# Day 10

DAY = '10'

def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    clock_iter = iter([20, 60, 100, 140, 180, 220])

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    X = 1
    clock = 0
    curclockcheck = next(clock_iter)
    result = []

    for line in input_data:
        if line == 'noop':
            clock += 1
            if clock == curclockcheck:
                result.append(X * clock)
                try:
                    curclockcheck = next(clock_iter)
                except StopIteration:
                    break
        else:
            addxval = int(line.split(' ')[1])
            clock += 1
            if clock == curclockcheck:
                result.append(X * clock)
                try:
                    curclockcheck = next(clock_iter)
                except StopIteration:
                    break
            X += addxval
            clock += 1
            if clock == curclockcheck:
                result.append(X * clock)
                try:
                    curclockcheck = next(clock_iter)
                except StopIteration:
                    break
    
    print(result)
    print(f'The final result is: {sum(result)}')

if __name__ == '__main__':
    main()

# Answer = 15260