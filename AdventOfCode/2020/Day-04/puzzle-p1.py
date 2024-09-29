import re


DAY = '04'

rqflds = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

def isvalidpp(pp):
    matches = re.findall(r'(...):', pp)
    for rf in rqflds:
        if rf not in matches:
            return False
    return True


def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    validpassports = 0
    passport = ''

    for line in input_data:
        if line == '':
            if isvalidpp(passport):
                validpassports += 1
            passport = ''
        else:
            passport = '\n'.join((passport, line))
    if isvalidpp(passport):
        validpassports += 1

    print(f'Valid passports: {validpassports}')


if __name__ == '__main__':
    main()

#Anser = 230