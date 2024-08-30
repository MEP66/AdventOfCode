import re
from dataclasses import dataclass

DAY = '19'

@dataclass
class Sub:
    subst: str
    repl: str
    size: int


def replace(string, srch, rplc, n):
    Sstring = string.split(srch)
    #Got this from the following site:
    #   https://stackoverflow.com/questions/35091557/replace-nth-occurrence-of-substring-in-string
    #paste the part before the nth substring to the part after the nth substring
    #with the replacement inbetween

    return f'{srch.join(Sstring[:(n)])}{rplc}{srch.join(Sstring[n:])}' 


def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    subs = list()
    getstartmolecule = False
    for line in input_data:
        if not getstartmolecule:
            if line == '':
                getstartmolecule = True
            else:
                substr, origstr = line.split(' => ')
                subs.append(Sub(subst = origstr, repl = substr, size = len(origstr)))
        else:
            startmolecule = line
    
    subs.sort(key=lambda x: x.size, reverse=True)

    molecule = startmolecule
    numsubs = 0
    while molecule != 'e':
        for s in subs:
            nummatches = len(re.findall(rf'{s.subst}', molecule))
            
            if nummatches > 0:
                for n in range(1, nummatches + 1):
                    molecule = replace(molecule, s.subst, s.repl, 1)
                    numsubs += 1
                break
    
    print(f'Total number of substitutions = {numsubs}')
    

if __name__ == '__main__':
    main()

#Answer = 200