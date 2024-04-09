import re

DAY = '11'


class Monkey():
    def __init__(self, number, startingitems: list, op, test, monkeytrue: int, monkeyfalse: int):
        self.items = startingitems
        self.operation = op
        self.test = test
        self.throw = {True: monkeytrue, False: monkeyfalse}
        self.inspections = 0

    def process_item(self, old):
        self.inspections += 1
        worry = eval(self.operation)
#        worry = worry // 3
        return (worry, self.throw[not(bool(worry % self.test))])
    

def main():
    filename = fr'./AdventOfCode/2022/Day-{DAY}/input-example.txt'
    #filename = fr'./AdventOfCode/2022/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    monkeys = {}

    for line in input_data:
        if re.match(r'Monkey ', line):
            num = int(re.search(r'\d', line)[0])

        elif re.match(r'  Starting items:', line):
            items = re.findall(r'\d+', line)
            startingitems = [int(item) for item in items]

        elif re.match(r'  Operation: ', line):
            operation = line.split('= ')[1]

        elif re.match(r'  Test:', line):
            divisibleby = int(re.search(r'\d+', line)[0])

        elif re.match(r'    If true:', line):
            iftrue = int(re.search(r'\d+', line)[0])
        
        elif re.match(r'    If false:', line):
            iffalse = int(re.search(r'\d+', line)[0])
            monkeys[num] = Monkey(num, startingitems, operation, divisibleby, iftrue, iffalse)

    for index in range(10000):
        for monkey in monkeys.values():
            while monkey.items:
                item = monkey.items.pop(0)
                action = monkey.process_item(item)
                monkeys[action[1]].items.append(action[0])
        if index == 999:
            results = []
            for monkey in monkeys.values():
                results.append(monkey.inspections)
            print(f'{index}   {results}')

    results = []
    for monkey in monkeys.values():
        results.append(monkey.inspections)

    results.sort(reverse=True)
    print(results)
    print(f'The product of the top two monkeys is: {results[0] * results[1]}')



if __name__ == '__main__':
    main()


# Answer = 
