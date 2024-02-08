import re
import math

def quadratic(t: int, d: int) -> tuple[int, int] | None:
    commterm = math.sqrt((t**2)-4*d)
    lowerbound = math.ceil((t - commterm)/2)
    upperbound = math.floor((t + commterm)/2)
    if (t - commterm) % 2 == 0:
        lowerbound += 1
        upperbound -= 1
    
    return lowerbound, upperbound


def puzzle06():

    prod = 1
    filename = r'./Day-06/Input-06.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    start = len(re.match('Time:\s+', input_data[0]).group())
    times = [int(re.sub('\s+', '', input_data[0][start::]))]
    start = len(re.match('Distance:\s+', input_data[1]).group())
    distances = [int(re.sub('\s+', '', input_data[1][start::]))]

    for time, distance in zip(times, distances):
        lower, upper = quadratic(time, distance)
        prod *= (upper - lower + 1)
    print(prod)

if __name__ == '__main__':
    puzzle06()

# Answer = 42550411
