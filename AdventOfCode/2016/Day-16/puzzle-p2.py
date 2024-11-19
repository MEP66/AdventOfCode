# Got help from this site:
# https://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list

DAY = '16'

#INPUT = '10000'
#DISKLENGTH = 20
INPUT = '11100010111110100'
#DISKLENGTH = 272
DISKLENGTH = 35651584


def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    s = iter(iterable)
    return zip(s, s)


def main():

    a = INPUT
    while len(a) < DISKLENGTH:
        b = a[::-1]
        b = b.replace('1', '2')
        b = b.replace('0', '1')
        b = b.replace('2', '0')
        c = a + '0' + b
        a = c
        
    a = a[:DISKLENGTH]
    
    cksum = list()
    
    cksum = [int(x) ^ int(y) for x, y in pairwise(a)]
    while not len(cksum) % 2:
        a = cksum
        cksum = [((int(x) ^ int(y)) ^ 1) for x, y in pairwise(a)]

    print(f'Final checksum: {''.join([str(c) for c in cksum])}')

if __name__ == '__main__':
    main()

#Answer = 01010001101011001