

DAY = '13'


def get_file_gen(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    
    get_line = get_file_gen(filename)
    layer_map = dict()

    for line in get_line:
        params = [int(x) for x in line.split(': ')]
        layer_map[params[0]] = {'range': params[1], 'direc': 1, 'depth': -1}
    
    all_layers = tuple(layer_map.keys())
    last_packet_depth = max(all_layers)

    my_delay = 0
    all_attempts = list()
    found = False
    while True:
        print(f'{my_delay}')
        all_attempts.append([my_delay, -1])
        passed_layers = list()
        for layer in layer_map.values():
            layer['depth'] += layer['direc']
            if layer['depth'] == 0:
                layer['direc'] = 1
            elif layer['depth'] == layer['range']-1:
                layer['direc'] = -1
        while all_attempts:
            attempt = all_attempts.pop(0)
            attempt[1] += 1
            
            if attempt[1] in all_layers:
                if layer_map[attempt[1]]['depth'] != 0:
                    if attempt[1] == last_packet_depth:
                        print(f'Min delay: {attempt[0]}')
                        found = True
                        break
                    else:
                        passed_layers.append(attempt)
            else:
                passed_layers.append(attempt)
            if found:
                break
        else:
            all_attempts = passed_layers.copy()
            my_delay += 1
        if found:
            break
    print(f'Min delay: {attempt[0]}')


        
if __name__ == '__main__':
    main()

#Answer = 