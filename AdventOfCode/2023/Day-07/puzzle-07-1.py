from dataclasses import dataclass
from collections import Counter


@dataclass
class Hand:
    cards: str
    bid: int
    rank: int = None
    sort: str = None


def puzzle07():

    cards = list('23456789TJQKA')
    cardstrength = list('0123456789ABC')
    cardorder = dict(zip(cards, cardstrength))

    filename = r'./Day-07/Input-07.txt'
    all_hands = list()

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()
    
    for line in input_data:
        r = line.split(' ')
        all_hands.append(Hand((r[0]), int(r[1])))

    for hand in all_hands:
        ccount = Counter(hand.cards)
        pcount = Counter(ccount.values())
        
        match max(pcount):
            case 5:
                hand.rank = 7
            case 4:
                hand.rank = 6
            case 3:
                if len(ccount) == 2:
                    hand.rank = 5
                else:
                    hand.rank = 4
            case 2:
                if pcount[2] == 2:
                    hand.rank = 3
                else:
                    hand.rank = 2
            case _:
                hand.rank = 1
    
        sortorder = str(hand.rank)
        for card in hand.cards:
            sortorder = sortorder + str(cardorder[card])
        hand.sort = sortorder
    
    all_hands.sort(key=lambda x: x.sort)
    sum, rank = 0, 0
    for rank, hand in enumerate(all_hands, 1):
        sum += (rank * hand.bid)

    print(sum)


if __name__ == '__main__':
    puzzle07()


# Answer: 248396258