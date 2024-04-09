
DAY = '13'

def compare(l, r) -> bool:
    if type(l) != type(r):
        if type(l) == int:
            l = [l]
        else:
            r = [r]
    if type(l) is list:
        result = None
        for index in range(len(l)):
            if result == None and index >= len(r):
                return False
            result = compare(l[index], r[index])
            if result is None:
                continue
            elif result:
                return True
            else:
                return False
        return True
    else:
        if l == r:
            return None
        elif r == None:
            return False
        elif l == None:
            return True
        elif l < r:
            return True
        return False
       

def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines() 

    correctorder = []
    index = 0
    while index < len(input_data):
        left = list(eval(input_data[index]))
        right = list(eval(input_data[index + 1]))
        index += 3

        if compare(left, right):
            correctorder.append(int((index-3)/3)+1)
        
    print(f'The sum of properly ordered pairs is: {sum(correctorder)}')


if __name__ == '__main__':
    main()
