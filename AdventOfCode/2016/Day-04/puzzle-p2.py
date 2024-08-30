import re
from collections import Counter

DAY = '04'

ASCIIa = 97

def main():
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    input_data = list()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            x = re.search(r'(.+)-(\d+)\[(.+)\]', line)
            input_data.append((x[1], int(x[2]), x[3]))
    
    sum = 0
    for entry in input_data:
        counts = list(Counter(''.join(entry[0].split('-'))).items())
        counts.sort(key = lambda x: (-x[1], x[0]))
        counts = counts[:5]
        if ''.join([x[0] for x in counts]) == entry[2]:
            decrypted = []
            for char in entry[0]:
                if char == '-':
                    decrypted.append(' ')
                else:
                    decrypted.append(chr((((ord(char) - ASCIIa) + entry[1]) % 26) + ASCIIa))
            print(entry[1], ''.join(decrypted))
    print(sum)


if __name__ == '__main__':
    main()

#Answer = 993
