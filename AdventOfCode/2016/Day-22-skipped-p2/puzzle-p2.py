from dataclasses import dataclass
import re


DAY = '22'


@dataclass
class DF:
     size: int
     used: int
     avail: int
     use: int


def read_file_gen(filename):
    with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                 yield line.strip()

def main():
    #filename = fr'./AdventOfCode/2016/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2016/Day-{DAY}/input.txt'
    
    df_out = dict()
    get_file_line = read_file_gen(filename)
    next(get_file_line)
    next(get_file_line)

    for line in get_file_line:
        params = [int(x) for x in re.findall(r'\d+', line)]
        df_out[(params[0], params[1])] = DF(size=params[2], used=params[3],
                                            avail=params[4], use=params[5])

    pass


if __name__ == '__main__':
    main()

#Answer: 981