

DAY = '09'

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read().strip()]

    disk_parts = dict()
    proc_id = True
    part_i = 0
    file_id = 0
    dict_entry = 0
    for num in input_data:
        if proc_id:
            disk_parts[dict_entry] = {'part': part_i, 'data': [file_id for _ in range(num)], 'sp': 0}
            file_id += 1
        else:
            disk_parts[dict_entry] = {'part': part_i, 'data': [], 'sp': num}
        part_i += num
        proc_id = not(proc_id)
        dict_entry += 1
    del input_data

    tail_i = len(disk_parts)-1
    while True:
        try:
            while not disk_parts[tail_i]['data']:
                tail_i -= 1
            data_size = len(disk_parts[tail_i]['data'])
            for head_i in range(0, tail_i):
                if disk_parts[head_i]['sp'] >= data_size:
                    disk_parts[head_i]['data'].extend(disk_parts[tail_i]['data'])
                    disk_parts[head_i]['sp'] -= data_size
                    disk_parts[tail_i]['data'] = []
                    break
            tail_i -= 1
        except KeyError:
            #Reached end of list
            break

    checksum = 0
    for _, v in disk_parts.items():
        if v['data']:
            idx = v['part']
            for n in v['data']:
                checksum += n * idx
                idx += 1
    
    print(f'Final checksum: {checksum}')
    

if __name__ == '__main__':
    main()

#Answer = 6363268339304