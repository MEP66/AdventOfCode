from dataclasses import dataclass


DAY = '22'


@dataclass
class DF:
     fs: str
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
    
    df_out = list()
    for line in read_file_gen(filename):
        if line[0] == '/':
            cols = line.split()
            f = cols[0]
            s = int(cols[1][:-1])
            ud = int(cols[2][:-1])
            a = int(cols[3][:-1])
            us = int(cols[4][:-1])

            df_out.append(DF(fs=f, size=s, used=ud, avail=a, use=us))

    viable = 0
    for A in df_out:
         for B in df_out:
              if A.fs != B.fs and A.used > 0 and A.used <= B.avail:
                   viable += 1
    
    print(f'Num of vialble pairs is: {viable}')


if __name__ == '__main__':
    main()

#Answer: 981