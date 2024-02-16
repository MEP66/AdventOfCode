

DAY = '02'

def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
          input_data = f.read().splitlines()


    # A X Rock 1 Lose 0
    # B Y Paper 2 Draw 3
    # C Z Scissors 3 Win 6

    #score = {('A', 'X'): 1 + 3, ('A', 'Y'): 2 + 6, ('A', 'Z'): 3 + 0,
    #         ('B', 'X'): 1 + 0, ('B', 'Y'): 2 + 3, ('B', 'Z'): 3 + 6,
    #         ('C', 'X'): 1 + 6, ('C', 'Y'): 2 + 0, ('C', 'Z'): 3 + 3}
    
    score = {('A', 'X'): 3 + 0, ('A', 'Y'): 1 + 3, ('A', 'Z'): 2 + 6,
             ('B', 'X'): 1 + 0, ('B', 'Y'): 2 + 3, ('B', 'Z'): 3 + 6,
             ('C', 'X'): 2 + 0, ('C', 'Y'): 3 + 3, ('C', 'Z'): 1 + 6}
    
    total = 0
    for line in input_data:
         total += score[(line[0], line[2])]

    print(f'The total score is: {total}')

if __name__ == '__main__':
    main()

# Answer = 14204
    