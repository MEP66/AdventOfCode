

DAY = '10'

brackets = {'(' : ')', '[' : ']', '{' : '}', '<' : '>'}
scoring = {')' : 1, ']' : 2, '}' : 3, '>' : 4}


def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    all_scores = list()
    for line in input_data:
        stack = list()
        for char in line:
            if char in brackets:
                stack.append(char)
            else:
                lastpop = stack.pop(-1)
                if brackets[lastpop] != char:
                    break
        else:
            score = 0
            stack.reverse()
            for opener in stack:
                score = (score * 5) + scoring[brackets[opener]]
            all_scores.append(score)

    all_scores.sort()
    print(f'Score: {all_scores[int(len(all_scores)/2)]}')


if __name__ == '__main__':
    main()

#Answer = 1105996483