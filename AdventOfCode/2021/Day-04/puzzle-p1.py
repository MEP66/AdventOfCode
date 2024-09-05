

DAY = '04'

class Bingocard:
    def __init__(self, card):
        self.card = card
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
        input_data = f.read().splitlines()

    call_number = [int(n) for n in input_data[0].split(',')]
    all_cards = list()
    current_card = list()

    for line in input_data[2:]:
        if line == '':
            all_cards.append(Bingocard(tuple(current_card)))
            current_card = list()
        else:
            row = [int(n) for n in line.split()]
            current_card.append(tuple(row))
    all_cards.append(Bingocard(tuple(current_card)))


    winner = False
    for draw in call_number:
        for card in all_cards:
            if card.callnumber(draw) == 'winner':
                winner = True
                winningscore = card.scorecard(draw)
                break
        if winner:
            break

    if winner:
        print(f'The score of the winning card is: {winningscore}')

if __name__ == '__main__':
    main()

#Answer = 51776