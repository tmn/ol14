import json
import re
import urllib

from bs4 import BeautifulSoup
from flask import make_response

def create_json_response (data, status = 200):
    res = make_response(json.dumps(data), status)
    res.mimetype = 'application/json'
    return res


class Olympics (object):

    def __init__(self):
        pass

    def get_medals (self):
        url = 'https://en.wikipedia.org/wiki/2014_Winter_Olympics_medal_table'
        web = urllib.urlopen(url)

        soup = BeautifulSoup(web.read())
        table = soup.find_all('table', attrs={'class':'wikitable'})[0]
        rows = table.findAll('tr')

        list = {}

        for i in range(1, len(rows)-1):
            cols = rows[i].findAll('td')

            index = 0 if len(cols) == 5 else 1

            list[cols[index].find('span').string[1:-1]] = {
                'c': cols[index].find('a').string,
                'g': int(cols[index+1].string),
                's': int(cols[index+2].string),
                'b': int(cols[index+3].string),
                't': int(cols[index+1].string) + int(cols[index+2].string)+  int(cols[index+3].string)
            }

        return list


    def get_medals_based_on_country (self, country):
        list = self.get_medals()

        pattern = re.compile('%s' % country, re.IGNORECASE)

        if country.upper() in list:
            return [list[country.upper()]]

        res = [k for k in list.values() if pattern.search(k['c'])]

        return res if res is not None else []
