import numpy as np


def getmirrors(amap):

    def getmirror(bmap):

        # Find locations of duplicate rows

        duprows = list()

        for rindex, crow in enumerate(bmap[:-1]):
            if crow == bmap[rindex+1]:
                duprows.append(rindex)

        # For each dup found, see if there is a mirror image

        if duprows:
            maxfound = list()
            for entry in duprows:
                index = entry
                index2 = entry + 1
                found = True
                while index >= 0 and index2 < len(bmap):
                    if bmap[index] != bmap[index2]:
                        found = False
                        break
                    else:
                        index -= 1
                        index2 += 1
                if found:
                    maxfound.append(entry)
                else:
                    maxfound.append(-1)
            maxf = max(maxfound) + 1
        else:
            maxf = 0
        return maxf

    r = getmirror(amap)
    c = getmirror(np.array(amap).T.tolist())

    return r, c


    
def main():

    # Fetch the puzzle data

    #filename = r'./Day-13/input-example.txt'
    filename = r'./Day-13/input.txt'

    indivmap = list()
    sum = 0

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():  # look for a blank line
                indivmap.append(list(line.strip()))
            else:
                # Find mirror points and sum results
                mrow, mcol = getmirrors(indivmap)
                sum += (mrow * 100) + mcol
                indivmap = list()
        # Catch the last map at the end of file.
        mrow, mcol = getmirrors(indivmap)
        sum += (mrow * 100) + mcol

    print('Final sum = ', sum)

if __name__ == '__main__':
    main()

# Answer: 27742