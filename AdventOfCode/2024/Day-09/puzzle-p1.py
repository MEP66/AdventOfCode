

DAY = '09'

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read().strip()]

    disk_parts = list()
    id = True
    i = 0
    for num in input_data:
        if id:
            disk_parts.extend([i for _ in range(num)])
            i += 1
        else:
            disk_parts.extend(['.' for _ in range(num)])
        id = not(id)
    del input_data

    i = 0
    while True:
        try:
            while disk_parts[i] != '.':
                i += 1
            while True:
                tail = disk_parts.pop(-1)
                if tail != '.':
                    break
            disk_parts[i] = tail
        except IndexError:
            #Reached end of list
            break

    checksum = 0
    for i, v in enumerate(disk_parts):
        checksum += i * v
    
    print(f'Final checksum: {checksum}')
    

if __name__ == '__main__':
    main()

#Answer = 6331212425418