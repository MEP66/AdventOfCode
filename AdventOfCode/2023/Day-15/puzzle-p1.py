# puzzle-p1 (Day 15)

# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.

def main():

    # Fetch the puzzle data

    filename = r'./Day-15/input-example.txt'
    filename = r'./Day-15/input.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        input = f.read()
        inputlist = input.strip().split(',')

        print(inputlist)

    # Calculate hash
    
    hash = 0
    for xstr in inputlist:
        ihash = 0
        for xltr in xstr:
            ihash += int(ord(xltr))
            ihash *= 17
            ihash = ihash % 256
        hash += ihash

    print('Final hash value = ', hash)



if __name__ == '__main__':
    main()


# Answer = 504036
    