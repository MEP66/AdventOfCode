

DAY = '06'

def calc_sum(batch, sum):
    if len(batch) == 1:
        sum += len(batch[0])
    else:
        charset = batch[0]
        for nextset in batch[1:]:
            charset = charset.intersection(nextset)
        sum += len(charset)
    return sum   

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    totalsum = 0
    batch = list()
    for line in input_data:
        if line == '':
            totalsum = calc_sum(batch, totalsum)
            batch = list()
        else:
            batch.append(set(list(line)))
    
    totalsum = calc_sum(batch, totalsum)


    print(f'Answer:  {totalsum}')


if __name__ == '__main__':
    main()

#Answer = 3232
