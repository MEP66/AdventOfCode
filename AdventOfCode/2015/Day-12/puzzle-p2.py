import re

DAY = '12'

def save_reds(input_list):
    global index

    while True:
        index += 1
        if input_list[index] == '{':
            drop_reds(input_list)
            continue
        if input_list[index] == '[':
            save_reds(input_list)
            continue
        if input_list[index] == ']':
            break


def drop_reds(input_list):
    global index

    redfound = False
    startpos = index
    while True:
        index += 1
        if input_list[index] == '[':
            save_reds(input_list)
            continue
        if (input_list[index] == 'r'
            and input_list[index + 1] == 'e'
            and input_list[index + 2] == 'd'):
            
            redfound = True
            continue
        if input_list[index] == '{':
            drop_reds(input_list)
            continue
        if input_list[index] == '}':
            if redfound:
                for i in range(startpos+1, index):
                    input_list[i] = '-'
                break
            else:
                break

def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    global index

    index = 0

    with open(filename, 'r', encoding='utf-8') as f:
          input_data = f.read()

    input_list = list(input_data)

    while index < len(input_list):
        if input_list[index] == '{':
             drop_reds(input_list)
             continue
        if input_list[index] == '[':
            save_reds(input_list)
            continue
        index += 1

    final_string = ''.join(input_list)
    numbers = re.findall(r'-?\d+', final_string)
    total_sum = 0
    for num in numbers:
         total_sum += int(num)

    print(total_sum)

if __name__ == '__main__':
    main()

#Answer = 68466
