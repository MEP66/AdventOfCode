import hashlib

DAY = 'x'

SEED = 'abc'
SEED = 'ojvtpuvg'

def main():
    
    password = list()
    suffix = 1
    for i in range(8):
        while True:
            str2hash = SEED + str(suffix)
            myhash = hashlib.md5(str2hash.encode()).hexdigest()
            if myhash[:5] == '00000':
                password.append(myhash[5])
                suffix += 1
                break
            else:
                suffix += 1
    print(''.join(password))


if __name__ == '__main__':
    main()

#Answer = 4543c154