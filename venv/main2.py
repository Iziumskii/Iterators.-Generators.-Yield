from pprint import pprint
from hashlib import md5

def hash_generator(start, end):
    while (start < end):
        with open('countries-links.txt', encoding='utf-8') as file:
            for line in file:
                md5_line = md5(line.encode()).hexdigest()
                yield md5_line
                start += 1

for item in hash_generator(1, 250):
    print(item)