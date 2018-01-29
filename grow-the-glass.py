import json

import requests
from bs4 import BeautifulSoup


def line_notify(token, message):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + token}
    requests.post(url, data={'message': message}, headers=headers)


if __name__ == '__main__':
    with open('config.json') as f:
        config = json.load(f)
    
    res = requests.get('https://github.com/users/{}/contributions'.format(config['username']))
    html = BeautifulSoup(res.content, 'html5lib')
    attrs = html.find_all(attrs={'class': 'day'})[-1].attrs
    date = attrs['data-date']
    count = int(attrs['data-count'])
    
    if count == 0:
        message = '{}はまだコミットしてません！'.format(date)
        line_notify(config['line_token'], message)
