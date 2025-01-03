

DAY = '22'

ITERATIONS = 2000

def gen_secret_prices(num, itr):
    p = [int(num % 10)]
    for _ in range(itr):
        step1 = ((num ^ (num * 64)) % 16777216)
        step2 = ((step1 ^ (step1 // 32)) % 16777216)
        num = ((step2 ^ (step2 * 2048)) % 16777216)
        p.append(int(num % 10))
    return p

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [int(line) for line in f.read().splitlines()]

    all_prices = list()
    for num in input_data:
        all_prices.append(gen_secret_prices(num, ITERATIONS))
    price_changes = list()
    for prices in all_prices:
        price_changes.append([y - x for x, y in zip(prices, prices[1:])])

    all_buy_seq = dict()
    for i, pc in enumerate(price_changes):
        all_buy_seq[i] = dict()
        for i2, ps4 in enumerate(zip(pc, pc[1:], pc[2:], pc[3:])):
            if ps4 not in all_buy_seq[i]:
                all_buy_seq[i][ps4] = all_prices[i][i2 + 4]

    max_score = 0
    visited = set()
    for d in all_buy_seq.values():
        for bs in d:
            if bs not in visited:
                temp_score = 0
                for d2 in all_buy_seq.values():
                    try:
                        temp_score += d2[bs]
                    except KeyError:
                        pass
                max_score = max(max_score, temp_score)
                visited.add(bs)

    print(f'Max score is: {max_score}')

if __name__ == '__main__':
    main()

#Answer = 2044
