# Day 09

DAY = '09'
headmoves = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    headpos = [0, 0]
    tailpos = [0, 0]
    tailvisited = {(0, 0)}

    for line in input_data:
        command = line.split(' ')
        movdir = command[0]
        movdist = int(command[1])

        for _ in range(movdist):
            headpos = (headpos[0] + headmoves[movdir][0], headpos[1] + headmoves[movdir][1])
            absdist = (abs(headpos[0] - tailpos[0]), abs(headpos[1] - tailpos[1]))

            if not ((absdist[0] == 0 or absdist[0] == 1) and (absdist[1] == 0 or absdist[1] == 1)):
                if absdist[0] == 2:
                    tailpos[0] = int((tailpos[0] + headpos[0])/2)
                else:
                    tailpos[1] = int((tailpos[1] + headpos[1])/2)
                if absdist[0] == 1:
                    tailpos[0] = headpos[0]
                elif absdist[1] == 1:
                    tailpos[1] = headpos[1]
                tailvisited.add((tailpos[0], tailpos[1]))

    print(f'The total number of tail visits is: {len(tailvisited)}')


if __name__ == '__main__':
    main()

# Answer = 5710