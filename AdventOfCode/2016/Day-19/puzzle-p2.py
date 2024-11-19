

DAY = '19'

#NUMELVES = 5
NUMELVES = 3004953


def main():

    elves = {k: k+1 for k in range(1, NUMELVES+1)}
    elves[NUMELVES] = 1

    totalelves = NUMELVES
    stealer = 1
    stealee_m1 = (NUMELVES // 2)

    while totalelves > 2:
        elves[stealee_m1] = elves[elves[stealee_m1]]
        stealer = elves[stealer]
        totalelves -= 1
        if not totalelves & 1:
            stealee_m1 = elves[stealee_m1]
    
    print(f'Elf with all the presents: {stealer}')

if __name__ == '__main__':
    main()

#Answer = 1410630
