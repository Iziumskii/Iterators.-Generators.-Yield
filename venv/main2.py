from pprint import pprint
from hashlib import md5

def hash_generator(start, end):
    while (start < end):
        with open('countries-links.txt', encoding='utf-8') as file:
            f_line = file.read()
            md5_line = md5(f_line.encode()).hexdigest()
        yield md5_line
        #yield f_line
        start += 1

for item in hash_generator(1, 250):
    print(item)