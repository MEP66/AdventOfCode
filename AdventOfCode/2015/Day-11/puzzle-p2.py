

DAY = '11'

BOT = ord('a')
TOP = ord('z')
FORBIDDEN = [ord('i'), ord('o'), ord('l')]


def increment(mylist, pos):


    mylist[pos] += 1
    if mylist[pos] in FORBIDDEN:
        mylist[pos] += 1
    if mylist[pos] > TOP:
        mylist[pos] = BOT
        increment(mylist, pos - 1)
    return

def main():

    INPUT = 'hepxcrrq'
    INPUT = 'hepxxyzz'
    
    input_data = list(bytes(INPUT, 'utf-8'))
    num_inp = len(input_data)
    num_inp_m1 = num_inp - 1
    num_inp_m2 = num_inp - 2
    num_inp_m4 = num_inp - 4

    while True:
        increment(input_data, -1)
        tri_req_found = False
        for i in range(num_inp_m2):
            if input_data[i] == input_data[i+1] - 1:
                if input_data[i+1] == input_data[i+2] - 1:
                    tri_req_found = True
                    break
        
        dbl_req_found = False
        if tri_req_found:
            for i in range(num_inp_m1):
                if input_data[i] == input_data[i + 1] and i < num_inp_m4:
                    for j in range(i + 2, num_inp_m1):
                        if input_data[j] == input_data[j + 1]:
                            dbl_req_found = True
                            break
        if dbl_req_found:
            break

    print(input_data)
    print(''.join(list(map(chr, input_data))))

if __name__ == '__main__':
    main()

#Answer = heqaabcc
