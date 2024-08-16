from sympy import divisors

DAY = '20'

def main():
    #filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    #filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    input = 36000000

    elfcount = 1
    while True:
        divlist = divisors(elfcount)
        presentcount = sum(list(map(lambda x: x*10, divlist)))
        if presentcount >= input:
            print(elfcount)
            break
        else:
            elfcount += 1
          

if __name__ == '__main__':
    main()

#Answer = 831600