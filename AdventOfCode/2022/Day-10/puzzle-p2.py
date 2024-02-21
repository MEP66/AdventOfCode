# Day 10

DAY = '10'

def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    clock_iter = iter([40, 80, 120, 160, 200, 240, 280])

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    X = 1
    clock = 0
    curclockcheck = next(clock_iter)
    crt_screen = []
    crt_lineadj = 0

    crt_line = ''
    for line in input_data:
        if line == 'noop':
            clock += 1
            if (X-1) <= (clock-1-crt_lineadj) <= (X+1):
                crt_line = crt_line + '#'
            else:
                crt_line = crt_line + '.'
            if clock == curclockcheck:
                crt_screen.append(crt_line)
                crt_line = ''
                crt_lineadj = curclockcheck
                curclockcheck = next(clock_iter)

        else:
            addxval = int(line.split(' ')[1])
            clock += 1
            if (X-1) <= (clock-1-crt_lineadj) <= (X+1):
                crt_line = crt_line + '#'
            else:
                crt_line = crt_line + '.'
            if clock == curclockcheck:
                crt_screen.append(crt_line)
                crt_line = ''
                crt_lineadj = curclockcheck
                curclockcheck = next(clock_iter)

            clock += 1
            if (X-1) <= (clock-1-crt_lineadj) <= (X+1):
                crt_line = crt_line + '#'
            else:
                crt_line = crt_line + '.'
            X += addxval
            if clock == curclockcheck:
                crt_screen.append(crt_line)
                crt_line = ''
                crt_lineadj = curclockcheck
                curclockcheck = next(clock_iter)


    for line in crt_screen:
        print(line)

if __name__ == '__main__':
    main()

# Answer = PGHFGLUG