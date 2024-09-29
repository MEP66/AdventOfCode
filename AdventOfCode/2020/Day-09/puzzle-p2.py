from itertools import combinations


DAY = '09'
#PREAMBLE = 5
PREAMBLE = 25

def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(x) for x in f.read().splitlines()]

    for i in range(PREAMBLE, len(input_data)):
        found = False
        for combo in combinations(input_data[i-PREAMBLE:i], 2):
            if (sum(combo) == input_data[i]) and (combo[0] != combo[1]):
                found = True
        if not found:
            result = input_data[i]
            break

    print(f'Part 1 result = {result}')

    for i in range(len(input_data)):
        total = 0
        inner_i = i
        while total < result:
            total += input_data[inner_i]
            inner_i += 1
        if total == result:
            print(f'Part 2 result = {min(input_data[i:inner_i]) + max(input_data[i:inner_i])}')
            break

if __name__ == '__main__':
    main()

#Answer P1 = 50047984
#Answer p2 = 5407707