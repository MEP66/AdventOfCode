from dataclasses import dataclass

DAY = '03'

@dataclass
class DeliveryBoy:
    x: int = 1
    y: int = 1

    def get_pos(self):
        return (self.x, self.y)
    
    def move(self, direction: str):
        match direction:
            case '^':
                self.y += 1
            case '>':
                self.x += 1
            case 'v':
                self.y -= 1
            case '<':
                self.x -= 1
        return self.get_pos()

def main():
    #filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read()

    santa = DeliveryBoy()
    robot_santa = DeliveryBoy()

    all_visited = {santa.get_pos()}
    santas_turn = True

    for dir in input_data:
        if santas_turn:
            all_visited.add(santa.move(dir))
        else:
            all_visited.add(robot_santa.move(dir))
        santas_turn = not santas_turn
    
    print(len(all_visited))
    

if __name__ == '__main__':
    main()

#Answer = 2631