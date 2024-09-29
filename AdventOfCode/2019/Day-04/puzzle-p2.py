

DAY = '04'


def adjnum(num):
    numlist = list(str(num))
    for i in range(len(numlist) - 1):
        if numlist[i + 1] < numlist[i]:
            for x in range(i + 1, len(numlist)):
                numlist[x] = numlist[i]

    return int(''.join(numlist))

def main():

    START = 402328
    END = 864247    

    curnum = adjnum(START)

    count = 0
    while curnum <= END:
        numlist = list(str(curnum))
        if ((numlist[0] == numlist[1] and numlist[2] != numlist[0])
            or (numlist[1] == numlist[2] and numlist[0] != numlist[1] and numlist[3] != numlist[1])
            or (numlist[2] == numlist[3] and numlist[1] != numlist[2] and numlist[4] != numlist[2])
            or (numlist[3] == numlist[4] and numlist[2] != numlist[3] and numlist[5] != numlist[3])
            or (numlist[4] == numlist[5] and numlist[3] != numlist[4])):
            count += 1
        curnum += 1
        if curnum % 10 == 0:
            curnum = adjnum(curnum)

    print(f'Count: {count}')

if __name__ == '__main__':
    main()

#Answer = 288