

DAY = '09'

def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read()

    total_score = 0
    group_level = 0
    garbage_count = 0
    state_queue = list()
    state_queue.append('init')

    for c in input_data:
        if state_queue[-1] == 'init':
            if c == '{':
               state_queue.append('group open')
               group_level += 1
            else:
               print(f'Error. No open group on init.')
        elif state_queue[-1] == 'group open':
            match c:
                case '{':
                    state_queue.append('group open')
                    group_level += 1
                case '<':
                    state_queue.append('garbage collection')
                case '!':
                    state_queue.append('ignore next')
                case '}':
                    total_score += group_level
                    group_level -= 1
                    state_queue.pop(-1)
        elif state_queue[-1] == 'garbage collection':
            match c:
                case '!':
                    state_queue.append('ignore next')
                case '>':
                    state_queue.pop(-1)
                case _:
                    garbage_count += 1
        elif state_queue[-1] == 'ignore next':
            state_queue.pop(-1)

    if state_queue[-1] != 'init':
        print(f'Error. Queue not empty.')
    else:
        print(f'Total score: {total_score}')
        print(f'Total garbage: {garbage_count}')


if __name__ == '__main__':
    main()

#Answer p1 = 11898
#Answer p2 = 5601