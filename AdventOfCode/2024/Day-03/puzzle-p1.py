import re


DAY = '03'

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().strip()
    
    matches = re.findall(r'mul\(-?\d+,-?\d+\)', input_data)
    
    total = 0
    for m in matches:
        nums = re.findall(r'-?\d+', m)
        total += (int(nums[0]) * int(nums[1]))
    
    print(f'Total: {total}')

if __name__ == '__main__':
    main()

#Answer = 183669043
