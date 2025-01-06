from functools import reduce
import operator

# Really wanted to use OOP on this one. Good article I referenced:
# https://openbookproject.net/courses/python4fun/logic.html
# but my solution didn't turn out to be much like the article above.


DAY = '24'


class Connector:
    all_Connectors = dict()
    all_outputs = dict()

    def __init__(self, name):
        if name not in Connector.all_Connectors:
            Connector.all_Connectors[name] = self

            self.value = None
            self.name = name

            if self.name[0] == 'z':
                self.monitor = True
                Connector.all_outputs[name] = None
            else:
                self.monitor = False
            self.connects = []   # These are the connections to gate inputs pins.

    def connect(self, iGate):
        self.connects.append(iGate)
        iGate.inputs[self.name] = None

    def set(self, value):
        self.value = int(value)
        for gate in self.connects:
            gate.inputs[self.name] = value
            gate.evaluate()
        if self.monitor:
            Connector.all_outputs[self.name] = int(value)

def create_Connector(name):
    if name in Connector.all_Connectors:
        return Connector.all_Connectors[name]
    return Connector(name)


class LGate():        # multiple input gates, one output
    def __init__(self, name, i=None, o=None):
        self.name = name
        self.inputs = dict()
        self.output = None


class And(LGate):       # AND Gate
    def __init__(self, name):
        LGate.__init__(self, name)

    def connect(self, oconn):
        self.output = oconn

    def evaluate(self):
        if not (len(self.inputs) < 2 or None in self.inputs.values()):
            outval = int(all(self.inputs.values()))
            self.output.set(outval)


class Or(LGate):         # OR gate.
    def __init__(self, name):
        LGate.__init__(self, name)

    def connect(self, oconn):
        self.output = oconn

    def evaluate(self):
        if not (len(self.inputs) < 2 or None in self.inputs.values()):
            outval = int(any(self.inputs.values()))
            self.output.set(outval)


class Xor(LGate):         # XOR gate.
    def __init__(self, name):
        LGate.__init__(self, name)

    def connect(self, oconn):
        self.output = oconn

    def evaluate(self):
        if not (len(self.inputs) < 2 or None in self.inputs.values()):
            outval = int(reduce(operator.xor, self.inputs.values()))
            self.output.set(outval)    


def generate_input(inp):
    for line in inp:
        yield line

def print_output(out_dict):
    output = [(int(k[1:]), v) for k, v in out_dict.items()]
    output.sort(key=lambda x: x[0], reverse=True)
    dec_output = int("".join([str(x[1]) for x in output]), 2)
    print(f'Output = {dec_output}')

def main():
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input-example.txt'
    filename = fr'./AdventOfCode/2024/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    get_input = generate_input(input_data)

    inputs = dict()
    line = next(get_input)
    while line:   # Read until the blank line for input info
        inp, val = line.split(': ')
        inputs[inp] = int(val)
        line = next(get_input)

    gate_index = 0
    for line in get_input:  # Read the rest of the input file for gate info
        line = line.replace('-> ', '')
        i1, opr, i2, out = line.split(' ')
        g_ref = 'g' + str(gate_index)
        
        match opr:
            case 'AND':
                gate = And(g_ref)
            case 'OR':
                gate = Or(g_ref)
            case 'XOR':
                gate = Xor(g_ref)
            case _:
                print(f'Error in parsing.')
        conn = create_Connector(out)
        gate.connect(conn)
        conn = create_Connector(i1)
        conn.connect(gate)
        conn = create_Connector(i2)
        conn.connect(gate)

        gate_index += 1

    for name, val in inputs.items():
        Connector.all_Connectors[name].set(val)

    print_output(Connector.all_outputs)

if __name__ == '__main__':
    main()

# Answer = 59364044286798