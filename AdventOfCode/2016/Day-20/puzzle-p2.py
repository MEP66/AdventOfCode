

DAY = '20'

#MAXIP = 10
MAXIP = 4294967295


def main():
    #filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        ip_list = [tuple(int(x) for x in line.split('-')) for line in f.read().splitlines()]
        
    ip_list.sort(key = lambda tup: tup[0])

    all_ip_ranges = list()
    ip_low_range = [0, 0]
    for ip_pair in ip_list:
        if ip_pair[0] > ip_low_range[1] + 1:
            all_ip_ranges.append(ip_low_range)
            ip_low_range = list(ip_pair)
        else:
            ip_low_range[1] = max(ip_low_range[1], ip_pair[1])
    all_ip_ranges.append(ip_low_range)
    
    sumblocked = 0
    for range in all_ip_ranges:
        sumblocked += range[1] - range[0] + 1

    allowed = MAXIP + 1 - sumblocked

    print(f'Total number of allowed IPs is: {allowed}')

if __name__ == '__main__':
    main()

#Answer p1: 23923783
#Answer p2: 125