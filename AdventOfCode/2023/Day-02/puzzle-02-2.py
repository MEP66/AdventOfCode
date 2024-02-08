import re

filename = r'./Day-02/Input-02.txt'

sum = 0
limits = {'red' : 12, 'green' : 13, 'blue' : 14}

with open(filename, 'r', encoding='utf-8') as f:
    input_data = f.read().splitlines()

for line in input_data:
    pulldata = {}
    maxballs = {'red' : 0, 'green' : 0, 'blue' : 0}

    for group in line.split(': ')[1].split(';'):
        for pull in group.strip().split(','):
            data = pull.strip().split(' ')
            maxballs[data[1]] = max(maxballs[data[1]], int(data[0]))

    sum += maxballs['red'] * maxballs['green'] * maxballs['blue']
print(sum)
