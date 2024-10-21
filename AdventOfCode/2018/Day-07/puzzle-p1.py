

DAY = '07'

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
            inst[s] = {'to' : [d], 'from' : []}
        else:
            inst[s]['to'].append(d)
        
        if d not in inst:
            inst[d] = {'to' : [], 'from' : [s]}
        else:
            inst[d]['from'].append(s)

    executed = []
    queued = [n for n in inst if not inst[n]['from']]

    while queued:
        queued.sort()
        for i, n in enumerate(queued):
            if set(inst[n]['from']).issubset(set(executed)):
                break
        
        executing = queued.pop(i)
        executed.append(executing)
        if inst[executing]['to']:
            queued.extend(inst[executing]['to'])
            queued = list(set(queued))
    
    
    print(f'Execution order: {''.join(executed)}')


if __name__ == '__main__':
    main()

#Answer: GKPTSLUXBIJMNCADFOVHEWYQRZ