

DAY = '03'

def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
          input_data = f.read().splitlines()

    sum = 0
    index = 0
    while index < len(input_data):
        ascii1 = set(input_data[index])
        ascii2 = set(input_data[index + 1])
        ascii3 = set(input_data[index + 2])
        index += 3
        
        commascii = ord(list(ascii1 & ascii2 & ascii3)[0])
        commcode = commascii - 96 if commascii > 91 else commascii - 38
        sum += commcode

    print(f'The sum is: {sum}')

if __name__ == '__main__':
    main()


# Answer = 2425