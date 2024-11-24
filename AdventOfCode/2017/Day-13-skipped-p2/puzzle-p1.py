

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
    
    my_depth = -1
    all_layers = tuple(layer_map.keys())
    last_packet_depth = max(all_layers)
    severity_total = 0

    while my_depth < last_packet_depth:
        my_depth += 1
        for layer in layer_map.values():
            layer['depth'] += layer['direc']
            if layer['depth'] == 0:
                layer['direc'] = 1
            elif layer['depth'] == layer['range']-1:
                layer['direc'] = -1
        if my_depth in all_layers:
            if layer_map[my_depth]['depth'] == 0:
                severity_total += (my_depth * layer_map[my_depth]['range'])

    print(f'Severity total: {severity_total}')

        
if __name__ == '__main__':
    main()

#Answer = 1612