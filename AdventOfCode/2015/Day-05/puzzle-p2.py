from collections import Counter

DAY = '05'


def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    nice_count = 0
    for line in input_data:
        double_letters = [line[i:i+2] for i in range(0, len(line)-1)]
        found = False
        for s in range(len(double_letters)-1):
            for e in range(s+2, len(double_letters)):
                if double_letters[s] == double_letters[e]:
                    found = True
                    break
            if found:
                break
        
        if not found:
            continue

        triple_letters = [line[i:i+3] for i in range(0, len(line)-2)]
        for triplet in triple_letters:
            if triplet[0] == triplet[2]:
                nice_count += 1
                break


    print(nice_count)
            

if __name__ == '__main__':
    main()

#Answer = 69