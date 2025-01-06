

DAY = '25'


def generate_fileline(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

def process_it(ele, ll, kl):
    if any(ele[0]):
        type = 'lock'
    else:
        type = 'key'
    trnsp = list(zip(*ele))
    profile = [sum(l)-1 for l in trnsp]

    if type == 'lock':
        ll.append(profile)
    else:
        kl.append(profile)

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'

    get_line = generate_fileline(filename)

    locks = list()
    keys = list()
    l_or_k = list()
    while True:
        try:
            line = next(get_line)
            if line:
                line = [int(x) for x in list(line.replace('#', '1').replace('.', '0'))]
                l_or_k.append(line)
            else:
                process_it(l_or_k, locks, keys)
                l_or_k = list()

        except StopIteration:
            process_it(l_or_k, locks, keys)
            break
    
    total_compat = 0
    for l in locks:
        for k in keys:
            compat = [max(0, x+y-5) for x, y in zip(l, k)]
            if not any(compat):
                total_compat += 1

    print(f'Total compatible lock/key pairs: {total_compat}')


if __name__ == '__main__':
    main()

#Answer - 3451