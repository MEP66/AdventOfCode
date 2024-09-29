

DAY = '06'

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    totalsum = 0
    charset = set()
    for line in input_data:
        if line == '':
            totalsum += len(charset)
            charset = set()
        else:
            charset.update(list(line))
    totalsum += len(charset)

    print(f'Answer:  {totalsum}')


if __name__ == '__main__':
    main()

#Answer = 6443
