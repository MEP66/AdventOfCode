import re


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
        batches = [[set(x) for x in line.split()] for line in f.read().split('\n\n')]

    totalsum = sum([len(set.intersection(*batch)) for batch in batches])
    print(f'Answer:  {totalsum}')


if __name__ == '__main__':
    main()

#Answer = 3232
