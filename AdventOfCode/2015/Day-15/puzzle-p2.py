from dataclasses import dataclass

DAY = '15'

@dataclass
class Ingr:
    cap: int
    dur: int
    flv: int
    txt: int
    cal: int


def get_input_combo():
    MAX = 100
    for a in range(1, MAX - 3):
        for b in range(1, MAX - a):
            for c in range(1, MAX - a - b - 1):
                yield (a, b, c, MAX - a - b - c)


def main():
    ingredients = {'Sugar' : Ingr(cap = 3, dur = 0, flv = 0, txt = -3, cal = 2),
                   'Sprinkles' : Ingr(cap = -3, dur = 3, flv = 0, txt = 0, cal = 9),
                   'Candy' : Ingr(cap = -1, dur = 0, flv = 4, txt = 0, cal = 1),
                   'Chocolate' : Ingr(cap = 0, dur = 0, flv = -2, txt = 2, cal = 8)}
    
    maxscore = 0

    for sugar, sprinkles, candy, chocolate in get_input_combo():

        capacity = max(0, (sugar * ingredients['Sugar'].cap
                    + sprinkles * ingredients['Sprinkles'].cap
                    + candy * ingredients['Candy'].cap
                    + chocolate * ingredients['Chocolate'].cap))
        
        durability = max(0, (sugar * ingredients['Sugar'].dur
                    + sprinkles * ingredients['Sprinkles'].dur
                    + candy * ingredients['Candy'].dur
                    + chocolate * ingredients['Chocolate'].dur))
        
        flavor = max(0, (sugar * ingredients['Sugar'].flv
                    + sprinkles * ingredients['Sprinkles'].flv
                    + candy * ingredients['Candy'].flv
                    + chocolate * ingredients['Chocolate'].flv))

        texture = max(0, (sugar * ingredients['Sugar'].txt
                    + sprinkles * ingredients['Sprinkles'].txt
                    + candy * ingredients['Candy'].txt
                    + chocolate * ingredients['Chocolate'].txt))

        calories = max(0, (sugar * ingredients['Sugar'].cal
                    + sprinkles * ingredients['Sprinkles'].cal
                    + candy * ingredients['Candy'].cal
                    + chocolate * ingredients['Chocolate'].cal))
        
        score = capacity * durability * flavor * texture

        if calories == 500:
            maxscore = max(score, maxscore)

    print(maxscore)

if __name__ == '__main__':
    main()

#Answer = 117936