from dataclasses import dataclass
from itertools import combinations
from math import inf

DAY = '21'

@dataclass
class Stat:
    cost : int
    damage : int
    armor: int


def main():
    MYHITPTS = 100
    MYDAMAGE = 0
    MYARMOR = 0

    BOSSHITPTS = 109
    BOSSDAMAGE = 8
    BOSSARMOR = 2

    Weapons = {'Dagger': Stat(cost=8, damage=4, armor=0),
                'Shortsword': Stat(cost=10, damage=5, armor=0),
                'Warhammer': Stat(cost=25, damage=6, armor=0),
                'Longsword': Stat(cost=40, damage=7, armor=0),
                'Greataxe': Stat(cost=74, damage=8, armor=0)}

    Armor = {'None': Stat(cost=0, damage=0, armor=0),
                'Leather': Stat(cost=13, damage=0, armor=1),
                'Chainmail': Stat(cost=31, damage=0, armor=2),
                'Splintmail': Stat(cost=53, damage=0, armor=3),
                'Bandedmail': Stat(cost=75, damage=0, armor=4),
                'Platemail': Stat(cost=102, damage=0, armor=5)}

    Rings = {'Damage +1': Stat(cost=25, damage=1, armor=0),
                'Damage +2': Stat(cost=50, damage=2, armor=0),
                'Damage +3': Stat(cost=100, damage=3, armor=0),
                'Defense +1': Stat(cost=20, damage=0, armor=1),
                'Defense +2': Stat(cost=40, damage=0, armor=2),
                'Defense +3': Stat(cost=80, damage=0, armor=3)}

    maxcost = 0
    for wep in Weapons.keys():
        for arm in Armor.keys():
            for rngpc in range(len(Rings) + 1):
                for rng in combinations(Rings.keys(), rngpc):
                    mcost = Weapons[wep].cost
                    mdamage = MYDAMAGE + Weapons[wep].damage
                    marmor = MYARMOR + Weapons[wep].armor
                    mcost += Armor[arm].cost
                    mdamage += Armor[arm].damage
                    marmor += Armor[arm].armor
                    for ring in rng:
                        mcost += Rings[ring].cost
                        mdamage += Rings[ring].damage
                        marmor += Rings[ring].armor
                    mhit = MYHITPTS
                    
                    bdamage = BOSSDAMAGE
                    barmor = BOSSARMOR
                    bhit = BOSSHITPTS

                    myturn = True

                    while bhit > 0:
                        if myturn:
                            bhit = bhit - (max(1, mdamage - barmor))
                        else:
                            mhit = mhit - (max(1, bdamage - marmor))
                        myturn = not(myturn)
                    
                    if mhit < 0:
                        maxcost = max(maxcost, mcost)

    print(f'The min cost is = {maxcost}')


if __name__ == '__main__':
    main()

#Answer = 188