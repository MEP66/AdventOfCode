import re
from dataclasses import dataclass


DAY = '07'

@dataclass
class LGate:
    value: int
    dist: bool
    inputs: list
    operation: str

def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    all_gates = dict()

    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    for line in input_data:
        firstsplit = line.split(' -> ')
        output = firstsplit[1]

        operation = re.search(r'AND|OR|NOT|LSHIFT|RSHIFT', firstsplit[0])

        if not operation:
            output = firstsplit[1]
            if firstsplit[0].isdigit():
                input = int(firstsplit[0])
                all_gates[output] = LGate(input, False, [input], 'WIRE')

            else:
                input = firstsplit[0]
                all_gates[output] = LGate(None, False, [input], 'WIRE')

            continue

        match operation.group():
            case 'AND':
                operation = re.match('([a-z0-9]+) AND ([a-z0-9]+)', firstsplit[0])

                if operation[1].isdigit():
                    input1 = int(operation[1])
                else:
                    input1 = operation[1]

                if operation[2].isdigit():
                    input2 = int(operation[2])
                else:
                    input2 = operation[2]

                all_gates[output] = LGate(None, False, [input1, input2], 'AND')

            case 'OR':
                operation = re.match('([a-z0-9]+) OR ([a-z0-9]+)', firstsplit[0])

                if operation[1].isdigit():
                    input1 = int(operation[1])
                else:
                    input1 = operation[1]

                if operation[2].isdigit():
                    input2 = int(operation[2])
                else:
                    input2 = operation[2]

                all_gates[output] = LGate(None, False, [input1, input2], 'OR')

            case 'NOT':
                operation = re.match('NOT ([a-z]+)', firstsplit[0])
                input = operation[1]

                all_gates[output] = LGate(None, False, [input], 'NOT')

            case 'LSHIFT':
                operation = re.match('([a-z]+) LSHIFT ([0-9]+)', firstsplit[0])
                input = operation[1]
                count = int(operation[2])

                all_gates[output] = LGate(None, False, [input, count], 'LSHIFT')

            case 'RSHIFT':
                operation = re.match('([a-z]+) RSHIFT ([0-9]+)', firstsplit[0])
                input = operation[1]
                count = int(operation[2])
                all_gates[output] = LGate(None, False, [input, count], 'RSHIFT')

    gate_dist_count = 0
    total_gates = len(all_gates)
    while gate_dist_count < total_gates:
        for label, gate in all_gates.items():
            if gate.value is not None and gate.dist == False:
                for search_input_gate in all_gates.values():
                    for index, input in enumerate(search_input_gate.inputs):
                        if input == label:
                            search_input_gate.inputs[index] = gate.value
                gate.dist = True
                gate_dist_count += 1

        for label, gate in all_gates.items():
            if not gate.dist:
                if all(isinstance(x, int) for x in gate.inputs):
                    match gate.operation:
                        case 'WIRE':
                            gate.value = gate.inputs[0]
                        case 'AND':
                            gate.value = gate.inputs[0] & gate.inputs[1]
                        case 'OR':
                            gate.value = gate.inputs[0] | gate.inputs[1]
                        case 'NOT':
                            gate.value = ~gate.inputs[0]
                        case 'LSHIFT':
                            gate.value = gate.inputs[0] << gate.inputs[1]
                        case 'RSHIFT':
                            gate.value = gate.inputs[0] >> gate.inputs[1]

    print(all_gates['a'].value)

if __name__ == '__main__':
    main()

#Answer = 14710 (No code change. Changed input file.)