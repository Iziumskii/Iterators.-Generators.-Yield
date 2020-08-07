from pprint import pprint
import requests
import json

class CountryIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start - 1
        self.session = requests.Session()

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current == self.end:
            raise StopIteration
        return self.read_file(self.current)
        #return self.get_search(), self.read_file(self.current)


    def read_file(self, n):
        with open("countries.json", encoding='utf-8') as js:
            json_data = json.load(js)
            js_data = json_data[n]["name"]["official"]
            return  self.get_search(js_data)

    def get_search(self, country):
        result = self.session.get(
            'https://en.wikipedia.org/w/api.php',
            params={
                'action': 'opensearch',
                'format': 'json',
                'search': country,
            }
        )
        result = result.json()
        try:
            return self.create_link(result[0], result[3][0])
        except IndexError:
            return self.create_link(result[0], 'Страница не найдена')

    def create_link(self, cointry, link):
        with open("countries-links.txt", "a", encoding='utf-8') as file:
            file.write(f'{cointry} - {link}' + '\n')


for item in CountryIterator(1, 250):
    pprint(item)



