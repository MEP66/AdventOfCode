import re


DAY = '21'

#START = 'abcde'
START = 'abcdefgh'


def read_file_gen(filename):
    with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                 yield line.strip()

def main():
    #filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    password = list(START)
    
    for line in read_file_gen(filename):
        words = line.split(' ')
        match words[0]:
            case 'swap':
                if words[1] == 'letter':
                    posa = password.index(words[2])
                    posb = password.index(words[5])
                    password[posa] = words[5]
                    password[posb] = words[2]

                elif words[1] == 'position':
                    leta = password[int(words[2])]
                    letb = password[int(words[5])]
                    password[int(words[5])] = leta
                    password[int(words[2])] = letb
            
                else:
                     print(f'Decoding error.')
              
            case 'reverse':
                beg = password[:int(words[2])]
                mid = password[int(words[2]):int(words[4])+1]
                end = password[int(words[4])+1:]
                mid.reverse()
                beg.extend(mid)
                beg.extend(end)
                password = beg
              
            case 'rotate':
                if words[1] == 'left':
                    for _ in range(int(words[2])):
                        char = password.pop(0)
                        password.append(char)

                elif words[1] == 'right':
                    for _ in range(int(words[2])):
                        char = password.pop(-1)
                        password.insert(0, char)

                elif words[1] == 'based':
                    offset = password.index(words[6])
                    if offset >=4:
                        offset += 1
                    offset += 1
                    for _ in range(offset):
                        char = password.pop(-1)
                        password.insert(0, char)
                else:
                    print(f'Decoding error.')
              
            case 'move':
                char = password.pop(int(words[2]))
                password.insert(int(words[5]), char)
    
            case _:
                print(f'Decoding error.')

    print(f'Final password: {''.join(password)}')
    pass


if __name__ == '__main__':
    main()

#Answer = agcebfdh
