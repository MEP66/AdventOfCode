import re


DAY = '19'

def is_valid_design(pat, sub_pats, memory):
    if pat == '':
        return True
    
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
        for txt in vld_fst_m:
            memory[pat] = is_valid_design(pat[len(txt):], vld_sps, memory)
            if memory[pat]:
                return True
    return False


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    all_subpatterns = input_data[0].split(', ')

    result = list()
    for pattern in input_data[2:]:
        memory = dict()
        result.append(is_valid_design(pattern, all_subpatterns, memory))
    valid_designs = sum(result)

    print(f'Number of valid designs: {valid_designs}')

if __name__ == '__main__':
    main()

#Answer = 226