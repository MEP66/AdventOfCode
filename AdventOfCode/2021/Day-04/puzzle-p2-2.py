

DAY = '04'

class Bingocard:
    def __init__(self, card):
        self.card = tuple(card)
        self.marker = [[0, 0, 0, 0, 0],
                       [0, 0 ,0 ,0 ,0],
                       [0, 0 ,0 ,0 ,0],
                       [0, 0 ,0 ,0 ,0],
                       [0, 0 ,0 ,0 ,0]]
        self.status = 'not winner'

    def callnumber(self, number):
        for r, row in enumerate(self.card):
            if number in row:
                for c, num in enumerate(row):
                    if num == number:
                        self.marker[r][c] = 1
                        break
        return self.evalcard()

    def evalcard(self):
        for r in self.marker:
            if all(r):
                self.status = 'winner'
        for r in zip(*self.marker):
            if all(r):
                self.status = 'winner'
        return self.status

    def scorecard(self, draw):
        sum = 0
        for r, row in enumerate(self.marker):
            for c, mark in enumerate(row):
                if mark == 0:
                    sum += self.card[r][c]
        return sum * draw


def main():
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2021/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().split('\n\n')

    call_number = tuple([int(n) for n in input_data[0].split(',')])
    del input_data[0]

    all_cards = [Bingocard([tuple([int(x) for x in line.split()])
                    for line in batch.splitlines()])
                    for batch in input_data]

    for draw in call_number:
        for card in all_cards:
            card.callnumber(draw)
            totalwinners = [True if card.status == 'winner' else False for card in all_cards]
            if all(totalwinners):
                winningscore = card.scorecard(draw)
                break
            else:
                continue
        else:
            continue
        break

    print(f'The score of the final winning card is: {winningscore}')


if __name__ == '__main__':
    main()

#Answer = 16830