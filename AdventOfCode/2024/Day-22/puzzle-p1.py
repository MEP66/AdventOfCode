

DAY = '22'

ITERATIONS = 2000

def gen_secret_num(num, itr):
    for _ in range(itr):
        step1 = ((num ^ (num * 64)) % 16777216)
        step2 = ((step1 ^ (step1 // 32)) % 16777216)
        num = ((step2 ^ (step2 * 2048)) % 16777216)
    return num

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(line) for line in f.read().splitlines()]

    total = 0
    for num in input_data:
        total += gen_secret_num(num, ITERATIONS)

    print(f'Sum total is: {total}')

if __name__ == '__main__':
    main()

#Answer = 18261820068
