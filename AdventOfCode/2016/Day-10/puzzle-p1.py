from collections import defaultdict
import re


DAY = '10'

def evaluate_bot(bdict, b):
    if b[0] != 'O':
        bdict[bdict[b]['low']]['regs'].add(min(bdict[b]['regs']))
        if len(bdict[bdict[b]['low']]['regs']) == 2:
            evaluate_bot(bdict, bdict[b]['low'])

        bdict[bdict[b]['high']]['regs'].add(max(bdict[b]['regs']))
        if len(bdict[bdict[b]['high']]['regs']) == 2:
            evaluate_bot(bdict, bdict[b]['high'])


def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()
    
    bots = defaultdict(lambda: {'regs': set(), 'from': list(), 'low': None, 'high': None})
    
    for line in input_data:
        if line[0] == 'b':
            (sbot, ldtype, ld, hdtype, hd) = [x for x in re.search(r'bot (\d+) gives low to (.+) (\d+) and high to (.+) (\d+)', line).groups()]
            if ldtype == 'bot':
                bots[sbot]['low'] = ld
                bots[ld]['from'].append(sbot)
            elif ldtype == 'output':
                bots[sbot]['low'] = 'O-' + ld
                bots['O-' + ld]['from'].append(sbot)
            else:
                print(f'Error in parsing')
            if hdtype == 'bot':
                bots[sbot]['high'] = hd
                bots[hd]['from'].append(sbot)
            elif hdtype == 'output':
                bots[sbot]['high'] = 'O-' + hd
                bots['O-' + hd]['from'].append(sbot)
            else:
                print(f'Error in parsing')
            
        elif line[0] == 'v':
            (val, dbot) = [x for x in re.search(r'value (\d+) goes to bot (\d+)', line).groups()]
            bots[dbot]['regs'].add(val)
            
        else:
            print(f'Error in parsing')

    for k, v in bots.items():
        if len(v['regs']) == 2:
            break
    
    evaluate_bot(bots, k)

    for k, v in bots.items():
        if '61' in v['regs'] and '17' in v['regs']:
            print(f'Answer = bot:  {k}')
    pass

if __name__ == '__main__':
    main()
