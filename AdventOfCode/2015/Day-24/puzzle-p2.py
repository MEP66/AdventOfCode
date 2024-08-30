from itertools import combinations
from itertools import accumulate
from math import inf

DAY = '24'

def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = set(map(int, f.read().splitlines()))

    targetsum = int(sum(input_data) / 4)

    minsetlen = 0
    temp = targetsum
    nums = list(input_data)
    nums.sort(reverse=True)
    while temp > 0:
        temp -= nums[minsetlen]
        minsetlen += 1

    minsumcombos = list()
    i = minsetlen
    while not minsumcombos:
        for nums in combinations(input_data, i):
            if sum(nums) == targetsum:
                minsumcombos.append(set(nums))
        i += 1

    minsize = inf
    minqe = inf

    for combo in minsumcombos:
        secondcombined = input_data - combo
        if sum(secondcombined) == 3 * targetsum:

            size = len(combo)
            qe = 1
            for element in combo:
                qe *= element
            if size <= minsize and qe <= minqe:
                minsize = size
                minqe = qe

    print(minsize, minqe)

if __name__ == '__main__':
    main()

#Answer = 72050269