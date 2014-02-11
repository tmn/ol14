import ConfigParser
import os
import redis
import urllib

from bs4 import BeautifulSoup
from lxml import etree


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


class Olympics (object):

    def __init__(self):
        self.redis = redis.Redis(
            host = app_config['REDIS_HOST'],
            port = app_config['REDIS_PORT'],
            password = app_config['REDIS_PW']
        )

    def test (self):
        return 'asdf'

    def get_medals (self):
        url = 'https://en.wikipedia.org/wiki/2014_Winter_Olympics_medal_table'
        web = urllib.urlopen(url)

        soup = BeautifulSoup(web.read())
        print soup.find_all('table', attrs={'class':'wikitable'})

        return 'Lol'

