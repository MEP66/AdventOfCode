from collections import deque
from collections import defaultdict

DAY = '21'


doorkeypad = {'7': {'8': '>', '4': 'v'}, '8': {'9': '>', '5': 'v', '7': '<'}, '9': {'6': 'v', '8': '<'},
              '4': {'7': '^', '5': '>', '1': 'v'}, '5': {'8': '^', '6': '>', '2': 'v', '4': '<'}, '6': {'9': '^', '3': 'v', '5': '<'},
              '1': {'4': '^', '2': '>'}, '2': {'5': '^', '3': '>', '0': 'v', '1': '<'}, '3': {'6': '^', 'A': 'v', '2': '<'},
              '0': {'2': '^', 'A': '>'}, 'A': {'3': '^', '0': '<'}}

controlkeypad = {'^': {'A': '>', 'v': 'v'}, 'A': {'^': '<', '>': 'v'},
                 '<': {'v': '>'}, 'v': {'^': '^', '>': '>', '<': '<'}, '>': {'A': '^', 'v': '<'}}

NUMCTLKP = 25

class Keypad():    
    def __init__(self, kp):
        self.kp = kp
        self.memory = dict()
    
    def all_shortest_paths(self, start, end):
        queue = deque([(start, [start])])
        visited = set()
        all_paths = []

        while queue:
            node, path = queue.popleft()
            visited.add(node)

            if node == end:
                all_paths.append(path)
            else:
                for neighbor in self.kp[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        all_keystrokes = []
        for path in all_paths:
            keystrokes = [self.kp[s][e] for s, e in zip(path, path[1:])]
            keystrokes.append('A') # Gotta press the button.
            all_keystrokes.append(keystrokes)
        return all_keystrokes


def shortest_path_length(all_codes, dkp, ckp, lvl=0):
    kp = [ckp, dkp][lvl == 0]

    final_pathlengths = defaultdict(lambda: 0)

    for pi, code in enumerate(all_codes):
        code.insert(0, 'A')

        for sk, ek in zip(code, code[1:]):
            if (lvl, (sk, ek)) in kp.memory:
                seg_length = kp.memory[(lvl, (sk, ek))]
            else:
                cur_shortest_pathset = kp.all_shortest_paths(sk, ek)
                if lvl == NUMCTLKP:
                    seg_length = len(cur_shortest_pathset[0])
                else:
                    seg_length = shortest_path_length(cur_shortest_pathset, dkp, ckp, lvl+1)
                    kp.memory[lvl, (sk, ek)] = seg_length
            final_pathlengths[pi] += seg_length
    shortest_path = min(final_pathlengths.values())
    return shortest_path


def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        keycodes = [list(line) for line in f.read().splitlines()]

    doorkp = Keypad(doorkeypad)
    controlkp = Keypad(controlkeypad)

    result = 0
    for code in keycodes:
        multiplier = int(''.join(code[0:3]))
        path = shortest_path_length([code], doorkp, controlkp)
        result += multiplier * path
    print(f'Final result = {result}')

if __name__ == '__main__':
    main()

#Answer = 294209504640384
