from collections import Counter

DAY = '05'


forbidden_strings = ('ab', 'cd', 'pq', 'xy')
vowels = ('a', 'e', 'i', 'o', 'u')

def main():
    #filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    nice_count = 0
    for line in input_data:
        letters = Counter(line.lower())
        vowel_count = 0
        for letter in letters:
            if letter in vowels:
                vowel_count += letters[letter]
        if vowel_count < 3:
            continue

        double_letters = [line[i:i+2] for i in range(0, len(line)-1)]
        for dublet in double_letters:
            if dublet[0] != dublet[1]:
                pass
            else:
                break
        else:
            continue

        for dublet in double_letters:
            if dublet not in forbidden_strings:
                pass
            else:
                break
        else:
            nice_count += 1

    print(nice_count)
            

if __name__ == '__main__':
    main()

#Answer = 238