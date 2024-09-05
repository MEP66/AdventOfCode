

DAY = '01'

def main():
    #filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    freqsfound = set()
    freq = 0
    found = False
    while True:
        for line in input_data:
            freq += int(line)
            if freq in freqsfound:
                found = True
                break
            else:
                freqsfound.add(freq)
        if found:
            print(f'First freq reached twice = {freq}')
            break


if __name__ == '__main__':
    main()

#Answer = 481