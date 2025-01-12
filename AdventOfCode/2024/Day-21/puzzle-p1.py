from collections import deque
from itertools import product, chain


DAY = '21'


doorkeypad = {'7': {'8': '>', '4': 'v'}, '8': {'9': '>', '5': 'v', '7': '<'}, '9': {'6': 'v', '8': '<'},
              '4': {'7': '^', '5': '>', '1': 'v'}, '5': {'8': '^', '6': '>', '2': 'v', '4': '<'}, '6': {'9': '^', '3': 'v', '5': '<'},
              '1': {'4': '^', '2': '>'}, '2': {'5': '^', '3': '>', '0': 'v', '1': '<'}, '3': {'6': '^', 'A': 'v', '2': '<'},
              '0': {'2': '^', 'A': '>'}, 'A': {'3': '^', '0': '<'}}

controlkeypad = {'^': {'A': '>', 'v': 'v'}, 'A': {'^': '<', '>': 'v'},
                 '<': {'v': '>'}, 'v': {'^': '^', '>': '>', '<': '<'}, '>': {'A': '^', 'v': '<'}}


def all_keystrokes(keypad, kcode, startchar):
    kcode.insert(0, startchar)
    all_keystroke_pairs = []
    for start, end in zip(kcode, kcode[1:]):
        all_keystrokes = all_shortest_paths(keypad, start, end)
        all_keystroke_pairs.append(all_keystrokes)
    final_keystrokes = []
    for i in product(*all_keystroke_pairs):
        final_keystrokes.append(list(chain(*i))) 
    return final_keystrokes

def all_shortest_paths(matrix, start, end):
    queue = deque([(start, [start])])
    visited = set()
    all_paths = []

    while queue:
        node, path = queue.popleft()
        visited.add(node)

        if node == end:
            all_paths.append(path)
        else:
            for neighbor in matrix[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    all_keypaths = []
    for path in all_paths:
        keystrokes = [matrix[s][e] for s, e in zip(path, path[1:])]
        keystrokes.append('A')
        all_keypaths.append(keystrokes)
    return all_keypaths


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        keycodes = [list(line) for line in f.read().splitlines()]

    result = 0
    for code in keycodes:
        multiplier = int(''.join(code[0:3]))
        firstrobot = all_keystrokes(doorkeypad, code, 'A')
              
        secondlevelkeys = list()
        for code in firstrobot:
            secondlevelkeys.extend(all_keystrokes(controlkeypad, code, 'A'))

        thirdlevelkeys = list()
        for code in secondlevelkeys:
            thirdlevelkeys.extend(all_keystrokes(controlkeypad, code, 'A'))

        result += min([len(x) for x in thirdlevelkeys]) * multiplier

    print(f'Final result = {result}')

if __name__ == '__main__':
    main()

#Answer = 242484
