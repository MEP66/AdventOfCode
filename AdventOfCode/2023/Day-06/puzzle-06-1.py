import re
import math

# acceleration = a  (1mm/ms)
# velocity(t) = at + v'  (t)
# position(t) = 0.5(a)t**2 + v't + s'  (0.5t**2)

# So, d = 0.5t**2 or 0.5t**2-d = 0
# Solve this for each race to see at what t you get the given distances.

# Quadratic = (-b +/- (b**2 - 4ac)**0.5)/2a
# Where a = 0.5, b = 0, c = d for all races

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
    times = [int(n) for n in re.split('\s+', input_data[0][start::])]
    start = len(re.match('Distance:\s+', input_data[1]).group())
    distances = [int(n) for n in re.split('\s+', input_data[1][start::])]

    for time, distance in zip(times, distances):
        lower, upper = quadratic(time, distance)
        print(lower, upper)
        prod *= (upper - lower + 1)
    print(prod)


if __name__ == '__main__':
    puzzle06()

# Answer = 1195150
