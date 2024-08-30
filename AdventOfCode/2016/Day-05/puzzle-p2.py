import hashlib

DAY = 'x'

SEED = 'abc'
SEED = 'ojvtpuvg'

def main():
    
    password = list()
    suffix = 1
    posfound = list()
    for i in range(8):
        while True:
            str2hash = SEED + str(suffix)
            myhash = hashlib.md5(str2hash.encode()).hexdigest()
            if myhash[:5] == '00000':
                pos = myhash[5]
                if pos.isdigit():
                    pos = int(pos)
                    char = myhash[6]
                    if pos < 8 and pos not in posfound:
                        password.append((pos, char))
                        posfound.append(pos)
                        print((pos, char, posfound))
                        suffix += 1
                        break
                    else:
                        suffix += 1
                else:
                    suffix += 1
            else:
                suffix += 1
    password.sort(key = lambda x: x[0])
    print(''.join([x[1] for x in password]))


if __name__ == '__main__':
    main()

#Answer = 1050cbbd