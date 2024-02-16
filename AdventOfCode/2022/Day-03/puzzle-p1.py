

DAY = '03'

def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
          input_data = f.read().splitlines()

    sum = 0
    for line in input_data:
        l = len(line)
        commascii = ord(list(set(line[:int(l/2)]) & set(line[int(l/2):]))[0])
        commcode = commascii - 96 if commascii > 91 else commascii - 38
        sum += commcode

    print(f'The sum is: {sum}')

if __name__ == '__main__':
    main()


# Answer = 8053