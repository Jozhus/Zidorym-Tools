import urllib.request, json
from bs4 import BeautifulSoup
while(1):
    buffer = urllib.request.urlopen("http://zidorym.sunnyday.jp/aaaaa/index.php").read().decode('utf-8')
    waifudb = "G:/Users/Jozhus/Documents/Python/data/waifudb.txt"
    file = open(waifudb, 'r')
    database = json.loads(file.read())
    file.close()
    page = BeautifulSoup(buffer, 'html.parser')
    old = len(database)
    if page.find_all('span')[4].text not in database:
        print(page.find_all('img')[0]['id'])
    elif database[page.find_all('span')[4].text] != page.find_all('img')[0]['id']:
        print(page.find_all('span')[4].text.encode('ascii', 'ignore').decode('utf-8') + ' : ' + page.find_all('img')[0]['id'])
    database[page.find_all('span')[4].text] = page.find_all('img')[0]['id']
    if page.find_all('span')[6].text not in database:
        print(page.find_all('img')[1]['id'])
    elif database[page.find_all('span')[6].text] != page.find_all('img')[1]['id']:
        print(page.find_all('span')[6].text.encode('ascii', 'ignore').decode('utf-8') + ' : ' + page.find_all('img')[1]['id'])
    database[page.find_all('span')[6].text] = page.find_all('img')[1]['id']
    if old != len(database):
        print(len(database))
    file = open(waifudb, 'w')
    file.write(json.dumps(database))
    file.close()
