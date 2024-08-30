

DAY = '06'

def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read().split()]

    end = len(input_data)
    all_found = list()
    steps = 0

    current = tuple(input_data)
    while current not in all_found:
        all_found.append(current)
        steps += 1
        largest = max(input_data)
        for index in range(end):
            if input_data[index] == largest:
                break
        input_data[index] = 0
        while largest != 0:
            largest -= 1
            index += 1
            if index == end:
                index = 0
            input_data[index] += 1
        current = tuple(input_data)
    
    print(steps)

if __name__ == '__main__':
    main()

#Answer = 12841