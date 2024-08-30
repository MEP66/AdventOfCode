

DAY = '05'

def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    stack = dict()
    for i, x in enumerate(input_data):
        stack[i] = int(x)
    
    num_steps = 0
    cur_location = 0
    end_location = len(stack)

    while 0 <= cur_location < end_location:
        num_steps += 1
        next_step = stack[cur_location]
        if stack[cur_location] >= 3:
            stack[cur_location] -= 1
        else:
            stack[cur_location] += 1
        cur_location += next_step
    
    print(num_steps)

if __name__ == '__main__':
    main()

#Answer = 29717847