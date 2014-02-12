import ConfigParser
import json
import os
import redis
import urllib

from bs4 import BeautifulSoup
from flask import make_response

config = ConfigParser.ConfigParser()
config.read([os.path.dirname(os.path.dirname(__file__)) + '/config'])

app_config = {
    'DEBUG': config.getboolean('olympics_server_config', 'debug'),
    'REDIS_DB': int(config.get('olympics_server_config', 'redis_db')),
    'REDIS_HOST': config.get('olympics_server_config', 'redis_host'),
    'REDIS_PORT': int(config.get('olympics_server_config', 'redis_port'))
}

try:
    app_config['REDIS_PW'] = config.get('olympics_server_config', 'redis_pw')
except ConfigParser.NoOptionError:
    app_config['REDIS_PW'] = None

def create_json_response (data, status = 200):
    res = make_response(json.dumps(data), status)
    res.mimetype = 'application/json'
    return res


class Olympics (object):

    def __init__(self):
        self.redis = redis.Redis(
            host = app_config['REDIS_HOST'],
            port = app_config['REDIS_PORT'],
            password = app_config['REDIS_PW']
        )

    def get_medals (self):
        url = 'https://en.wikipedia.org/wiki/2014_Winter_Olympics_medal_table'
        web = urllib.urlopen(url)

        soup = BeautifulSoup(web.read())
        table = soup.find_all('table', attrs={'class':'wikitable'})[0]
        rows = table.findAll('tr')

        list = []

        for i in range(1, len(rows)-1):
            cols = rows[i].findAll('td')

            index = 0 if len(cols) == 5 else 1

            list.append({
                'c': cols[index].find('a').string,
                'cc': cols[index].find('span').string[1:-1],
                'g': int(cols[index+1].string),
                's': int(cols[index+2].string),
                'b': int(cols[index+3].string),
                't': int(cols[index+1].string) + int(cols[index+2].string)+  int(cols[index+3].string)
            })

        return create_json_response(list)


    def get_medals_based_on_country (self, country):
        return country

