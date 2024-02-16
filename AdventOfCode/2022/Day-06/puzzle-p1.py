from collections import Counter

DAY = '06'

def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read()

    LEN = 4

    for index in range(len(input_data)):
        marker = input_data[index:index+LEN]
        if len(Counter(marker)) == LEN:
            break
    
    print(f'Marker location is at: {index+LEN}')

if __name__ == '__main__':
    main()

# Answer = 1175