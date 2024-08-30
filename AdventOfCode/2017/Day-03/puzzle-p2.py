
DAY = '03'

move = {'R': {'r': 0, 'c': 1}, 'U': {'r': -1, 'c': 0}, 'L': {'r': 0, 'c': -1}, 'D': {'r': 1, 'c': 0}}

def main():

    target = 361527

    data = 1
    dataloc = (0, 0)
    rowbndry = {'mn': 0, 'mx': 0}
    colbndry = {'mn': 0, 'mx': 0}

    currentdir = 'R'
    visited = dict()
    visited[dataloc] = data

    while data < target:
        dataloc = (dataloc[0] + move[currentdir]['r'], dataloc[1] + move[currentdir]['c'])
        data = 0
        for r in range(dataloc[0] - 1, dataloc[0] + 2):
            for c in range(dataloc[1] - 1, dataloc[1] + 2):
                x = visited.get((r, c), 0)
                data += x
        visited[dataloc] = data

        match currentdir:
            case 'R':
                if dataloc[1] > colbndry['mx']:
                    colbndry['mx'] = dataloc[1]
                    currentdir = 'U'

            case 'U':
                if dataloc[0] < rowbndry['mn']:
                    rowbndry['mn'] = dataloc[0]
                    currentdir = 'L'

            case 'L':
                if dataloc[1] < colbndry['mn']:
                    colbndry['mn'] = dataloc[1]
                    currentdir = 'D'

            case 'D':
                if dataloc[0] > rowbndry['mx']:
                    rowbndry['mx'] = dataloc[0]
                    currentdir = 'R'

    print(dataloc, data, (abs(dataloc[0]) + abs(dataloc[1])))

if __name__ == '__main__':
    main()

#Answer = 363010