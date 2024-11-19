

DAY = '18'

def triple_binary(iterator):
    i = iterator.copy()
    i.insert(0, 1)
    i.append(1)
    s = iter([str(n) for n in i])
    t = iter([str(n) for n in i])
    next(t)
    u = iter([str(n) for n in i])
    next(u)
    next(u)
    return [int(''.join(n), 2) for n in zip(s, t, u)]


def main():
    #TOTALROWS = 10
    #filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    TOTALROWS = 40
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().strip()
    
    room_map = list()
    row = list()
    for c in input_data:
        if c == '.':
            row.append(1)
        else:
            row.append(0)
    room_map.append(row)

    #decode_dict = {0: 1, 1: 0, 2: 1, 3: 0, 4: 0, 5: 1, 6: 0, 7: 1}
    decode_dict = {0b000: 1, 0b001: 0, 0b010: 1, 0b011: 0, 0b100: 0, 0b101: 1, 0b110: 0, 0b111: 1}

    rowi = 0
    while len(room_map) < TOTALROWS:
        row = [decode_dict[n] for n in triple_binary(room_map[rowi])]
        room_map.append(row)
        rowi += 1

    sum_safe = 0
    for row in room_map:
        sum_safe += sum(row)

    print(f'Sum of safe tiles is: {sum_safe}')


if __name__ == '__main__':
    main()

#Answer = 2016