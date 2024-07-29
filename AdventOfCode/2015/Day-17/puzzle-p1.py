import itertools


DAY = '17'

#This function came from the following website:
# https://stackoverflow.com/questions/3420937/algorithm-to-find-which-number-in-a-list-sum-up-to-a-certain-number

def fun(v, i, S, memo):
    if i >= len(v): return 1 if S == 0 else 0
    if (i, S) not in memo:  # <-- Check if value has not been calculated.
        count = fun(v, i + 1, S, memo)
        count += fun(v, i + 1, S - v[i], memo)
        memo[(i, S)] = count  # <-- Memoize calculated result.
    return memo[(i, S)]     # <-- Return memoized value.

def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    v = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            v.append(int(line.strip()))

    sum = 150
    memo = dict()
    print(fun(v, 0, sum, memo))


if __name__ == '__main__':
    main()

#Answer = 654