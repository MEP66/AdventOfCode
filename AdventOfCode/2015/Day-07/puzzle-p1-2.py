import re

DAY = '07'


class LGate():
    instances = []

    def get(name):
        for i in LGate.instances:
            if i.name == name:
                return i[0]
        return None
        #return [i for i in LGate.instances if i.name == name][0]

    def __init__(self, out):
        self.name = out
        self.oc = out
        LGate.instances[self.name] = self

class INPUT(LGate):
    def __init__(self, inp, out):
        super().__init__(out)

        self.iv = int(inp)
        self.ov = self.iv

    def i_setter(self, value):
        self.ov = value

class AND(LGate):
    def __init__(self, inp1, inp2, out):
        if inp1.isdigit():
            self.i1v = int(inp1)
            self.i1c = None
        else:
            self.i1v = None
            self.i1c = inp1
        
        if inp2.isdigit():
            self.i2v = int(inp2)
            self.i2c = None
        else:
            self.i2v = None
            self.i2c = inp2
        self.ov = None

    def i1_setter(self, value):
        self.i1v = value
        return self.eval()

    def i2_setter(self, value):
        self.i2v = value
        return self.eval()
    
    def eval(self):
        if self.i1v == None or self.i2v == None:
            self.ov = None
        else:
            self.ov = self.i1v & self.i2v
        return self.ov

class OR(LGate):
    def __init__(self, name, inp1, inp2, out):
        self.name = name
        self.i1 = inp1
        self.i2 = inp2
        self.o = out

class NOT(LGate):
    def __init__(self, name, inp, out):
        self.name = name
        self.i = inp
        self.o = out

    def eval(self):
        self.o = ~self.o

class LSHIFT(LGate):
    def __init__(self, name, inp, cnt, out):
        self.name = name
        self.i = inp
        self.c = cnt
        self.o = out

    def eval(self, count):
        for _ in range(self.c):
            self.o = self.i << self.c

class RSHIFT(LGate):
    def __init__(self, name, inp, cnt, out):
        self.name = name
        self.i = inp
        self.c = cnt
        self.o = out     

    def eval(self):
        #if self.o < 0:
        #    self.o = self.o + 2**16
        for _ in range(self.c):
            self.o = self.i >> self.c

class Connector:
    instances = dict()

    def get(name):
        for i in Connector.instances.values():
            if i.name == name:
                return i[0]
        return None
        #return [i for i in Connector.instances if i.name == name][0]

    def __init__(self, name):
        self.name = name
        self.conns = []
        Connector.instances[self.name] = self

    def connect(self, input_connection):
        if input_connection not in self.conns:
            self.conns.append(input_connection)

def main():
    filename = fr'./AdventOfCode/2015/Day-{DAY}/input-example.txt'
    #filename = fr'./AdventOfCode/2015/Day-{DAY}/input.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    for line in input_data:
        firstsplit = line.split(' -> ')
        output = firstsplit[1]

        operation = re.search(r'AND|OR|NOT|LSHIFT|RSHIFT', firstsplit[0])
        if not operation:
            input = int(firstsplit[0])
            output = firstsplit[1]

            gate = INPUT(input, output)

            if Connector.get(gate.oc) == None:
                Connector(gate.oc)

            continue
        
        match operation.group():
            case 'AND':
                operation = re.match('([a-z0-9]+) AND ([a-z0-9]+)', firstsplit[0])
                input1 = operation[1]
                input2 = operation[2]

                gate = AND(input1, input2, output)

                if Connector.get(gate.oc) == None:
                    Connector(gate.oc)

                if gate.i1c is not None:
                    if Connector.get(gate.i1c) == None:
                        conn = Connector(gate.i1c)
                    conn.connect(gate.i1_setter)
                
                if gate.i2c is not None:
                    if Connector.get(gate.i2c) == None:
                        conn = Connector(gate.i2c)
                    conn.connect(gate.i2_setter)

            case 'OR':
                operation = re.match('([a-z0-9]+) OR ([a-z0-9]+)', firstsplit[0])
                input1 = operation[1]
                input2 = operation[2]

                gate = OR(input1, input2, output)

                if Connector.get(gate.oc) == None:
                    Connector(gate.oc)

                if gate.i1c is not None:
                    if Connector.get(gate.i1c) == None:
                        conn = Connector(gate.i1c)
                    conn.connect(gate.i1_setter)
                
                if gate.i2c is not None:
                    if Connector.get(gate.i2c) == None:
                        conn = Connector(gate.i2c)
                    conn.connect(gate.i2_setter)

            case 'NOT':
                operation = re.match('NOT ([a-z]+)', firstsplit[0])
                input = operation[1]

                gate = NOT(input, output)

                if Connector.get(gate.oc) == None:
                    Connector(gate.oc)

                if gate.ic is not None:
                    if Connector.get(gate.ic) == None:
                        conn = Connector(gate.ic)
                    conn.connect(gate.i_setter)

            case 'LSHIFT':
                operation = re.match('([a-z]+) LSHIFT ([0-9]+)', firstsplit[0])
                input = operation[1]
                count = operation[2]

                gate = LSHIFT(input, count, output)

                if Connector.get(gate.oc) == None:
                    Connector(gate.oc)

                if gate.ic is not None:
                    if Connector(gate.ic) == None:
                        conn = Connector(gate.ic)
                    conn.connect(gate.i_setter)

            case 'RSHIFT':
                operation = re.match('([a-z]+) RSHIFT ([0-9]+)', firstsplit[0])
                input = operation[1]
                count = operation[2]

                gate = LSHIFT(input, count, output)

                if Connector.get(gate.oc) == None:
                    Connector(gate.oc)

                if gate.ic is not None:
                    if Connector(gate.ic) == None:
                        conn = Connector(gate.ic)
                    conn.connect(gate.i_setter)

    pass

if __name__ == '__main__':
    main()
