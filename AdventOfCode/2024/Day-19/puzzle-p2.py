import re


DAY = '19'

def is_valid_design(pat, sub_pats, memory):
    if pat == '':
        return 1
    
    if pat in memory:
        return memory[pat]

    #Find all valid subpatterns.

    vld_sps = [sp for sp in sub_pats if re.search(sp, pat)]

    #Find all valid matches at beginning of string.

    vld_fst_m = list()
    for sp in vld_sps:
        if match := re.match(sp, pat):
            vld_fst_m.append(match.group())

    #Recurse until we find a valid pattern or exhaust all possibilities.

    if vld_fst_m:
        total_valid = 0
        for txt in vld_fst_m:
            total_valid += is_valid_design(pat[len(txt):], vld_sps, memory)
        memory[pat] = total_valid
        return memory[pat]
    return 0


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    all_subpatterns = input_data[0].split(', ')

    result = list()
    total_valid_designs = 0
    for pattern in input_data[2:]:
        memory = dict()
        result = is_valid_design(pattern, all_subpatterns, memory)
        if result:
            total_valid_designs += result

    print(f'Number of valid designs: {total_valid_designs}')

if __name__ == '__main__':
    main()

#Answer = 601201576113503