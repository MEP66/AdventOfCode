

DAY = '10'

def main():
    INPUT = '3113322113'
    
    result = list(INPUT)
    for x in range(40):
        char = None
        count = 0
        new_result = list()
        while result:
            cur_char = result.pop(0)
            if cur_char == char:
                count += 1
            else:
                if char is not None:
                    new_result.append(str(count))
                    new_result.append(char)
                char = cur_char
                count = 1
        new_result.append(str(count))
        new_result.append(char)
        result = new_result
        print(x, len(result))
        
    print(len(result))  


if __name__ == '__main__':
    main()

#Answer = 329356