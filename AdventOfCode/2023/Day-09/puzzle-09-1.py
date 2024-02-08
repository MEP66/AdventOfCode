from collections import defaultdict
import re

def calcnext(currentlist) -> int:
    newlist: list(int) = defaultdict()
    newlist = [currentlist[i+1] - currentlist[i] for i in range(len(currentlist)-1)]
    if len(newlist) != 1:
        lastterm = calcnext(newlist)
        return lastterm + currentlist[-1]
    else:
        return newlist[-1]

def puzzle09():

    filename = r'./Day-09/Input-09.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    oasisreport: list(list(int)) = list()
    for line in input_data:
        valhistory = [int(x) for x in re.findall('-?\d+', line)]
        oasisreport.append(valhistory)

    totalsum = 0
    for line in oasisreport:
        indivsum = calcnext(line)
        totalsum += indivsum

    print(totalsum)



if __name__ == '__main__':
    puzzle09()


# Answer = 1637452029
    