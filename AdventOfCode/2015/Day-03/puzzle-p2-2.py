from dataclasses import dataclass

DAY = '03'

@dataclass
class DeliveryBoy:
    x: int = 1
    y: int = 1

    def move(self, direction):
        match direction:
            case '^':
                self.y += 1
            case '>':
                self.x += 1
            case 'v':
                self.y -= 1
            case '<':
                self.x -= 1
    
        return(self.x, self.y)


def main():
    #filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read()

    santa = DeliveryBoy
    robot_santa = DeliveryBoy

    all_visited = {santa}
    santas_turn = True

    for direction in input_data:
        if santas_turn:
            all_visited.add(santa.move(direction))
        else:
            all_visited.add(robot_santa.move(direction))
        
        santas_turn = not santas_turn
    
    print(len(all_visited))
    

if __name__ == '__main__':
    main()

#Answer = 2631