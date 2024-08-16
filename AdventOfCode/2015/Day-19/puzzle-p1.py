import re

DAY = '19'

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

    substitutions = list()
    getstartmolecule = False
    for line in input_data:
        if not getstartmolecule:
            if line == '':
                getstartmolecule = True
            else:
                origstr, substr = line.split(' => ')
                substitutions.append((origstr, substr))
        else:
            startmolecule = line
    
    resultmolecules = set()
    for entry in substitutions:
        origstr, substr = entry

        nummatches = len(re.findall(rf'{origstr}', startmolecule))

        for n in range(1, nummatches + 1):
            resultmolecules.add(replace(startmolecule, origstr, substr, n))
    
    print(len(resultmolecules))

if __name__ == '__main__':
    main()

#Answer = 518