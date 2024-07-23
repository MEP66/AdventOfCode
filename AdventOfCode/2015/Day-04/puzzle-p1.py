import hashlib


DAY = '04'

def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read()

    # encoding GeeksforGeeks using md5 hash
    # function 
    number_input = 0
    while True:
        to_hash = input_data + str(number_input)
        result = hashlib.md5(to_hash.encode('utf-8'))
        if result.hexdigest()[0:5] == '00000':
            break
        number_input += 1

    # printing the equivalent byte value.
    print(result.hexdigest())
    print(number_input)


if __name__ == '__main__':
    main()

#Answer = 282749