

DAY = '07'

TIMEOFFSET = 1 - ord('A')
TIMEOFFSET = 61 - ord('A')

WORKERS = 2
WORKERS = 5

def main():
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    inst = dict()

    for line in input_data:
        s = line[5]
        d = line[36]

        if s not in inst:
            inst[s] = {'etim' : ord(s) + TIMEOFFSET, 'to' : [d], 'from' : []}
        else:
            inst[s]['to'].append(d)
        
        if d not in inst:
            inst[d] = {'etim' : ord(d) + TIMEOFFSET, 'to' : [], 'from' : [s]}
        else:
            inst[d]['from'].append(s)

    executed = []
    executing = []
    queued = [n for n in inst if not inst[n]['from']]
    queued.sort()
    t = 0

    while True:
        i = 0
        while len(executing) < WORKERS and queued and i < len(queued):
            n = queued[i]
            if set(inst[n]['from']).issubset(set(executed)):
                newtask = queued.pop(i)
                executing.append(newtask)
                if inst[n]['to']:
                    queued.extend(inst[n]['to'])
            else:
                i += 1

        queued = list(set(queued))
        queued.sort()

        t += 1
        for n in executing:
            inst[n]['etim'] -= 1
            if inst[n]['etim'] == 0:
                executed.append(n)
        
        executing = [n for n in executing if inst[n]['etim'] > 0]

        if not queued and not executing:
            break


    print(f'Execution order: {''.join(executed)}')
    print(f'Execution time is: {t}')


if __name__ == '__main__':
    main()

#Answer: 920