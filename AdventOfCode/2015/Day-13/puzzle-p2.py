import re
import itertools

DAY = '13'

def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    

    invitees = set()
    happiness_lookup = dict()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            data = re.split(' ', line.strip()[:-1])
            name1 = data[0]
            sign = data[2]
            amount = int(data[3])
            if sign == 'lose':
                amount = amount * -1
            name2 = data[10]

            happiness_lookup[(name1, name2)] = amount

            invitees.add(name1)
            invitees.add(name2)
    
    all_perms = itertools.permutations(invitees)
    max_happiness = 0

    for perm in all_perms:
        cur_perm = list(perm)
        
        all_seat_pairs_cw = [(cur_perm[i], cur_perm[i+1]) for i in range(len(cur_perm) - 1)]
        
        all_seat_pairs_ccw = [(cur_perm[i+1], cur_perm[i]) for i in range(len(cur_perm) - 1)]

        all_happiness_factors_cw = [happiness_lookup[s] for s in all_seat_pairs_cw]
        all_happiness_factors_ccw = [happiness_lookup[s] for s in all_seat_pairs_ccw]

        this_happiness = sum(all_happiness_factors_cw) + sum(all_happiness_factors_ccw)

        max_happiness = max(max_happiness, this_happiness)

    print(max_happiness)

if __name__ == '__main__':
    main()

#Answer = 640
