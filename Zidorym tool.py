import urllib.request, requests, time, os, json
from bs4 import BeautifulSoup

database = {}

def html(url):
    buffer = urllib.request.urlopen(url).read().decode('utf-8')
    return BeautifulSoup(buffer, 'html.parser')

def db():
    global database
    waifudb = "G:/Users/Jozhus/Documents/Python/data/waifudb.txt"
    file = open(waifudb, 'r')
    database = json.loads(file.read())
    page = html("http://zidorym.sunnyday.jp/aaaaa/index.php")
    database[page.find_all('span')[4].text] = page.find_all('img')[0]['id']
    database[page.find_all('span')[6].text] = page.find_all('img')[1]['id']
    file = open(waifudb, 'w')
    file.write(json.dumps(database))
    file.close()
    
def check(target):
    global database
    print('Checking ranking...')
    rank = dict()
    lead = 500
    lines = [x.text for x in html("http://zidorym.sunnyday.jp/aaaaa/ranking.php").find_all('span')[5:]]
    for i, x in enumerate(lines[::3]):
        rank[x] = int(lines[1::3][i].split(' ')[1])
    others = list(rank.values())
    others.remove(rank[target])
    if rank[target] < max(others) + lead:
        vote([database[target]], max(others) - rank[target] + lead)

def vote(ID = [], amount = 1):
    print('Voting ' + str(amount*len(ID)) + ' times...')
    for x in range(amount):
        for things in ID:
            requests.post(url = "http://zidorym.sunnyday.jp/aaaaa/vote.php", data={'id':str(things)})
    print('Done!')

def loop():
    target = 'Akari Akaza'
    while(1):
        os.system('cls')
        print('Updating database...')
        db()
        check(target)

def find(name):
    args = name.split(' ')
    possibles = {}
    for key in database:
        if any(arg.lower() in key.lower() for arg in args):
            possibles[key] = database[key]
    return possibles
    
def key(ID):
    value = {database[key]:key for key in database}
    return value[str(ID)]
    
#loop()
