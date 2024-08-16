
DAY = '25'


def main():
    FIRSTCODE = 20151125
    MULTIPLIER = 252533
    DIVISOR = 33554393
    TARGETROW = 2947
    TARGETCOL = 3029

    ri = ci = i = 1
    value = FIRSTCODE

    while True:
        value = (value * MULTIPLIER) % DIVISOR
        if ri == 1:
            i += 1
            ri = i
            ci = 1
        else:
            ri -= 1
            ci += 1
        if ri == TARGETROW and ci == TARGETCOL:
            break
    
    print(value)    

if __name__ == '__main__':
    main()

#Answer = 19980801
