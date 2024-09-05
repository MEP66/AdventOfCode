

DAY = '01'

def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f]

    count = 0
    for index in range(len(input_data) - 3):
        if sum(input_data[index + 1:index + 4]) > sum(input_data[index : index + 3]):
            count += 1

    print(f'Count of increasing sequences = {count}')


if __name__ == '__main__':
    main()

#Answer = 1311