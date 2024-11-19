import hashlib
import re


DAY = '14'

#SALT = 'abc'
SALT = 'jlmsuwbz'


def get_md5_of_string(input_string):
    return hashlib.md5(input_string.encode()).hexdigest()

def main():
    hashes_looking = list()
    hashes_found = list()
    index = 0

    
    while len(hashes_found) < 64:
        hash = hashlib.md5((SALT+str(index)).encode()).hexdigest()
        hash_2b_added = None
        if hash3 := re.search(r'(.)\1{2}', hash):
            hash_2b_added = hash3.group(0)
        hash5s = re.findall(r'(.)\1{4}', hash)
        for hash5 in hash5s:
            if hash5*3 in [x[0] for x in hashes_looking]:
                temp_found = [x for x in hashes_looking if x[0] == hash5*3]
                hashes_looking = [x for x in hashes_looking if x[0] != hash5*3]
                hashes_found.extend(temp_found)
        hashes_looking = [[h, n-1, i] for h, n, i in hashes_looking if n-1 > 0]
        if hash_2b_added:
            hashes_looking.append([hash_2b_added, 1000, index])
        index += 1

    print(f'Final index: {hashes_found[63][2]}')


if __name__ == '__main__':
    main()

#Answer: 35186