

DAY = 'x'

def calculate_hash():
    

def main():
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2017/Day-{DAY}/input.txt'
    
    ROPE_LENGTH = 256
    SUFFIX = [17, 31, 73, 47, 23]
    ROUNDS = 64
    HASHGROUP = 16

    with open(filename, 'r', encoding='utf-8') as f:
        twist_lengths = [ord(c) for c in f.read().strip()]
    twist_lengths.extend(SUFFIX)

    knots = list(range(ROPE_LENGTH))
    skip = 0
    total_advance = 0

    for _ in range(ROUNDS):
        for twist in twist_lengths:
            string_twist = list(reversed(knots[:twist]))
            knots = [*string_twist, *knots[twist:]]
            advance = (twist + skip) % ROPE_LENGTH
            total_advance += advance
            total_advance = total_advance % ROPE_LENGTH

            knots = [*knots[advance:], *knots[:advance]]
            skip += 1

    front_of_list = ROPE_LENGTH - total_advance
    knots = [*knots[front_of_list:], *knots[:front_of_list]]

    grouphash = [knots[i:i+HASHGROUP] for i in range(0, len(knots), HASHGROUP)]

    result = list()
    for group in grouphash:
        hash = reduce(lambda x, y: x ^ y, group)
        result.append(str(hex(hash)).replace('0x', '').zfill(2))

    print(f'Result: {"".join(result)}')


if __name__ == '__main__':
    main()