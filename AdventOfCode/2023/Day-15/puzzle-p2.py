# puzzle-p1 (Day 15)

from collections import defaultdict
from collections import OrderedDict

def main():

    # Fetch the puzzle data

    #filename = r'./Day-15/input-example.txt'
    filename = r'./Day-15/input.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        input = f.read()
        inputlist = input.strip().split(',')

    # loop over data

    results = defaultdict()

    for item in inputlist:
        if item[-1] == '-':
            itemstr = item[:-1]
            itemval = 0
        else:
            itemtemp = item.split('=')
            itemstr = itemtemp[0]
            itemval = int(itemtemp[1])
        
        # Calculate hash
            
        hash = 0
        for xltr in itemstr:
            hash += int(ord(xltr))
            hash *= 17
            hash = hash % 256
  
        if itemval == 0:
            if hash in results.keys():
                if itemstr in results[hash].keys():
                    del results[hash][itemstr]
        else:
            if hash not in results.keys():
                results[hash] = OrderedDict()
            results[hash][itemstr] = itemval

    # Add up results
            
    sum = 0
    for hkey, hvalue in results.items():
        for index , iitem in enumerate(hvalue.items()):
            subtotal = (1 + hkey) * (index + 1) * iitem[1]
            sum += subtotal
  
    print('Final sum value = ', sum)


if __name__ == '__main__':
    main()

# Answer = 295719
    