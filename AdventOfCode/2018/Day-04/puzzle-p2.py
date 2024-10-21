import re
from datetime import datetime
from collections import Counter
from dataclasses import dataclass


DAY = '04'

SECS_PER_MIN = 60

@dataclass
class Sleep_sch():
    start: datetime
    duration: int

@dataclass
class Sleep_info():
    sleepy_min: int
    count: int

def main():
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2018/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = [[e for e in re.search(r'\[(.+)\] (.+)', line).groups()] for line in f.read().splitlines()]
    
    input_data = [[datetime.strptime(x[0], r'%Y-%m-%d %H:%M'), tuple(x[1].split())] for x in input_data]
    input_data.sort(key=lambda e: e[0])

    all_guards = dict()
    for event_date, event in input_data:
        match event[0]:
            case 'Guard':
                guard_num = int(event[1][1:])
                if guard_num not in all_guards.keys():
                    all_guards[guard_num] = {'sleep_time' : 0, 'sleep_sched' : list()}

            case 'falls':
                start_date = event_date

            case 'wakes':
                slp_time = int(((event_date - start_date).seconds)/SECS_PER_MIN)
                all_guards[guard_num]['sleep_sched'].append(Sleep_sch(start = start_date, duration = int(slp_time)))
                all_guards[guard_num]['sleep_time'] += slp_time

    all_results = dict()
    for guard, info in all_guards.items():
        if info['sleep_sched']:
            sleep_counter = Counter()
            for sched in info['sleep_sched']:
                sleep_counter.update([m for m in range(sched.start.minute, sched.start.minute + sched.duration)])
            sleepyest_min = max(sleep_counter, key=lambda key: sleep_counter[key])
            all_results[guard] = (Sleep_info(sleepy_min = sleepyest_min, count = sleep_counter[sleepyest_min]))
    
    result = max(all_results, key=lambda key: all_results[key].count)
    print(f'Result: {result * all_results[result].sleepy_min}')


if __name__ == '__main__':
    main()

#Answer: 76576
