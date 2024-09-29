import re


DAY = '04'

rqsrchs = (('byr', r'(byr):(\d{4})($|\s)'),
            ('iyr', r'(iyr):(\d{4})($|\s)'),
            ('eyr', r'(eyr):(\d{4})($|\s)'),
            ('hgt', r'(hgt):(\d+)(cm|in)($|\s)'),
            ('hcl', r'(hcl):#[0-9a-f]{6}($|\s)'),
            ('ecl', r'(ecl):(amb|blu|brn|gry|grn|hzl|oth)($|\s)'),
            ('pid', r'(pid):[0-9]{9}($|\s)'))


def isvalidpp(pp):
    ppvalid = True
    for type, srchstr in rqsrchs:
        srcmatch = re.search(srchstr, pp)
        if srcmatch:
            match type:
                case 'byr':
                    if not (1920 <= int(srcmatch.group(2)) <= 2002):
                        ppvalid = False
                        break

                case 'iyr':
                    if not (2010 <= int(srcmatch.group(2)) <= 2020):
                        ppvalid = False
                        break

                case 'eyr':
                    if not (2020 <= int(srcmatch.group(2)) <= 2030):
                        ppvalid = False
                        break

                case 'hgt':
                    if srcmatch.group(3) == 'cm':
                        if not (150 <= int(srcmatch.group(2)) <= 193):
                            ppvalid = False
                            break
                    elif srcmatch.group(3) == 'in':
                        if not (59 <= int(srcmatch.group(2)) <= 76):
                            ppvalid = False
                            break

                case 'hcl':
                    pass

                case 'ecl':
                    pass

                case 'pid':
                    pass

        else:
            ppvalid = False
            break
    return ppvalid


def main():
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2020/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    validpassports = 0
    passport = ''

    for line in input_data:
        line.strip()
        if line == '':
            if isvalidpp(passport):
                validpassports += 1
            passport = ''
        else:
            passport = ' '.join((passport, line))
    if isvalidpp(passport):
        validpassports += 1

    print(f'Valid passports: {validpassports}')


if __name__ == '__main__':
    main()

#Anser = 156