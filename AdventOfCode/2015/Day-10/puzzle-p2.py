from itertools import groupby

DAY = '10'

INPUT = '3113322113'

def look_and_say(input):
    # Got this solution from Reddit
    #print(input)
    #for k, v in groupby(input):
    #    print(k, list(v))
    return ''.join(str(len(list(v))) + k for k, v in groupby(input))

def main():
    p1 = INPUT
    for _ in range(40):
        p1 = look_and_say(p1)
    print(len(p1))

    p2 = INPUT
    for _ in range(50):
        p2 = look_and_say(p2)
    print(len(p2))


if __name__ == '__main__':
    main()

#Answer = 4666278