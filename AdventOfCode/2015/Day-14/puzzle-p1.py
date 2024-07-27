

DAY = '14'

#race_time = 1000
race_time = 2503

def main():
    #filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    max_dist = 0

    deer_info = dict()

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            params = line.split(' ')
            deer = params[0]
            flyspeed = int(params[3])
            flytime = int(params[6])
            resttime = int(params[13])

            deer_info[deer] = {'flyspeed': flyspeed, 'flytime': flytime, 'resttime': resttime, 'score': 0, 'dist': 0, 'flying': True, 'countdown': flytime}

    for t in range(race_time):
        max_dist = 0
        for deer in deer_info.items():
            if deer[1]['flying'] == True:
                deer[1]['dist'] += deer[1]['flyspeed']
            deer[1]['countdown'] -= 1
            if deer[1]['countdown'] == 0:
                deer[1]['flying'] = not deer[1]['flying']
                if deer[1]['flying']:
                    deer[1]['countdown'] = deer[1]['flytime']
                else:
                    deer[1]['countdown'] = deer[1]['resttime']
            max_dist = max(max_dist, deer[1]['dist'])

        for deer in deer_info.items():
            if deer[1]['dist'] == max_dist:
                deer[1]['score'] += 1

    max_score = 0
    for deer in deer_info.items():
        max_score = max(max_score, deer[1]['score'])

    print(max_score)

if __name__ == '__main__':
    main()

#Answer = 2640