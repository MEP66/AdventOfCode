

DAY = '14'

race_time = 2503
#race_time = 1000

def main():
    #filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    max_dist = 0

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            params = line.split(' ')
            deer = params[0]
            flyspeed = int(params[3])
            flytime = int(params[6])
            resttime = int(params[13])

            intv_dist = flyspeed * flytime
            intv_time = flytime + resttime

            comp, part = divmod(race_time, intv_time)

            dist = intv_dist * comp

            if flytime <= part:
                dist += (flytime * flyspeed)
            else:
                dist += (part * flyspeed)

            max_dist = max(max_dist, dist)

    print(max_dist)

if __name__ == '__main__':
    main()

#Answer = 2640