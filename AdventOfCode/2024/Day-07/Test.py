from itertools import product

DAY = '07'



def main():
    ops = ('+', '*')

    for x in product(*(ops for _ in range(3))):
        print(x)



if __name__ == '__main__':
    main()
