import re
from dataclasses import dataclass


def main():

    # Get input data

    @dataclass
    class Rating:
        x: int
        m: int
        a: int
        s: int

    filename = r'./Day-19/input-example.txt'
    filename = r'./Day-19/input.txt'

    workflows = dict()
    ratings = list()

    with open(filename, 'r', encoding='utf-8') as f:
        getworkflow = True
        for line in f:
            if getworkflow:
                if line.strip():
                    wfkey = re.match(r'(.+){', line).group(1)
                    wtemp = [tuple(item.split(':')) for item in re.search(r'{(.+)}', line).group(1).split(',')]
                    workflows[wfkey] = wtemp
                else:
                    getworkflow = False
            else:
                i = re.findall(r'\d+', line)
                ratings.append(Rating(int(i[0]), int(i[1]), int(i[2]), int(i[3])))

    results = list()

    for rating in ratings:
        x = rating.x
        m = rating.m
        a = rating.a
        s = rating.s
        currentrule = 'in'
        currentstatus = 'U'
        while currentstatus == 'U':
            for rule, ptr in workflows[currentrule][:-1]:
                if eval(rule):
                    if ptr == 'A' or ptr == 'R':
                        currentstatus = ptr
                        break
                    else:
                        currentrule = ptr
                        break
            else:
                ptr = workflows[currentrule][-1][0]
                if ptr == 'A' or ptr == 'R':
                    currentstatus = ptr
                else:
                    currentrule = ptr
        results.append(currentstatus)

    sum = 0
    for i, result in enumerate(results):
        if result == 'A':
            sum += ratings[i].x + ratings[i].m + ratings[i].a + ratings[i].s
    
    print('The final sum is: ', sum)


if __name__ == '__main__':
    main()


# Answer is: 391132