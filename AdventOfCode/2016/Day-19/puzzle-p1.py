

DAY = '19'

#NUMELVES = 5
NUMELVES = 3004953


def main():

    elves = {k: [1, k+1] for k in range(1, NUMELVES+1)}
    elves[NUMELVES][1] = 1

    index = 1
    while index != elves[index][1]:
        elves[index][0] += elves[elves[index][1]][0]
        elves[index][1] = elves[elves[index][1]][1]
        index = elves[index][1]
    
    print(f'Elve with all the presents: {elves[index][1]}')

if __name__ == '__main__':
    main()

#Answer = 1815603
