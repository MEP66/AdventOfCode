

def main():
    #filename = r'./Day-16/input-example.txt'
    filename = r'./Day-16/input.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        input = {(r, c) : v
                 for r, line in enumerate(f, 1)
                 for c, v in enumerate(list(line.strip()), 1)}

    maxrow = list(input.keys())[-1][0]
    maxcol = list(input.keys())[-1][1]

    procqueue = [((1, 1), (0, 1))]
    processed = list()

    while procqueue:
        pos = procqueue[0][0]
        dir = procqueue[0][1]
        del procqueue[0]

        while (pos[0] > 0 and pos[0] <= maxrow
                and pos[1] > 0 and pos[1] <= maxcol
                and dir != (0, 0)):
            cursym = input[pos][0]  # get left most character
            input[pos] = cursym + '#'  # tag as lit up
            match cursym:
                case '\\':
                    match dir:
                        case (0, 1):  # if right
                            dir = (1, 0)  # go down
                        case (0, -1):  # if left
                            dir = (-1, 0)  # go up
                        case (1, 0):  # if down
                            dir = (0, 1)  # go right
                        case (-1, 0):  # if up
                            dir = (0, -1)  # go left
                case '/':
                    match dir:
                        case (0, 1):  # if right
                            dir = (-1, 0)  # go up
                        case (0, -1):  # if left
                            dir = (1, 0)  # go down
                        case (1, 0):  # if down
                            dir = (0, -1)  # go left
                        case (-1, 0):  # if up
                            dir = (0, 1)  # go right
                case '-':
                    if pos not in processed:
                        processed.append(pos)
                        match dir:
                            case (1, 0) | (-1, 0):  # if down or up
                                procqueue.append(((pos[0], pos[1]-1), (0, -1)))  # queue left
                                procqueue.append(((pos[0], pos[1]+1), (0, 1)))  # queue right
                                dir = (0, 0)  # stop processing this run
                    else:
                        dir = (0, 0)  # stop processing this run
                case '|':
                    if pos not in processed:
                        processed.append(pos)
                        match dir:
                            case (0, 1) | (0, -1):  # if right or left
                                procqueue.append(((pos[0]-1, pos[1]), (-1, 0)))  # queue up
                                procqueue.append(((pos[0]+1, pos[1]), (1, 0)))  # queue down
                                dir = (0, 0)  # stop processing this run
                    else:
                        dir = (0, 0)  # stop processing this run

            pos = (pos[0]+dir[0], pos[1]+dir[1])

    sum = 0
    for value in input.values():
        if '#' in value:
            sum += 1
    print('The final sum is: ', sum)

if __name__ == '__main__':
    main()

# Answer = 7798