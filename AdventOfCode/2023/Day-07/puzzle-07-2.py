from dataclasses import dataclass
from collections import Counter


@dataclass
class Hand:
    cards: str
    bid: int
    rank: int = None
    sort: str = None


def puzzle07():

    filename = r'./Day-07/Input-07.txt'

    cards = list('J23456789TQKA')
    cardstrength = list('123456789ABCD')
    cardorder: dict(str, str) = dict(zip(cards, cardstrength))
    all_hands: list(Hand) = list()

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()
    
    for line in input_data:
        r = line.split(' ')
        all_hands.append(Hand((r[0]), int(r[1])))

    for hand in all_hands:
        ccount = Counter(hand.cards)
        pcount = Counter(ccount.values())
        
        if 'J' in ccount:
            numwilds = ccount['J']
            if numwilds == 5:
                ccount = Counter(['A', 'A', 'A', 'A', 'A'])
            else:
                ccount.pop('J')
                maxcount = max(ccount.values())
                maxcard = [key for key, value in ccount.items() if value==maxcount]
                ccount[maxcard[0]] += numwilds
            pcount = Counter(ccount.values())

        match max(pcount):
            case 5:
                hand.rank = 7  # Five of a kind
            case 4:
                hand.rank = 6  # Four of a kind
            case 3:
                if len(ccount) == 2:
                    hand.rank = 5  # Full house
                else:
                    hand.rank = 4  # Three of a kind
            case 2:
                if pcount[2] == 2:
                    hand.rank = 3  # Two pair
                else:
                    hand.rank = 2  # One pari
            case _:
                hand.rank = 1  # High card
    
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


# Answer: 246436046