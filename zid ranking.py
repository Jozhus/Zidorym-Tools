import urllib.request, json
from bs4 import BeautifulSoup

ranks = {}
rankdb = "G:/Users/Jozhus/Documents/Python/data/rankdb.txt"
ranking = "G:/Users/Jozhus/Documents/Python/data/rank.txt"
life = 3000

while (1):
    buffer = urllib.request.urlopen("http://zidorym.sunnyday.jp/aaaaa/index.php").read().decode('utf-8')
    page = BeautifulSoup(buffer, 'html.parser')
    file = open(rankdb, 'r')
    ranks = json.loads(file.read())
    file.close()
    for x in range(2):
        ID = page.find_all('img')[x]['id']
        rank = page.find_all('li')[3+(x*4)].text.encode('ascii', 'ignore').decode('utf-8').split(' ')[1]
        name = page.find_all('span')[4+(x*2)].text.encode('ascii', 'ignore').decode('utf-8')
        score = page.find_all('span')[5+(x*2)].text.encode('ascii', 'ignore').decode('utf-8').split(' ')[1]
        if not name in ranks:
            print('+ ' + name)
        ranks[name] = {'rank' : rank, 'score' : score, 'ID' : ID, 'life' : life}
    delete = []
    for name in ranks:
        ranks[name]['life'] -= 1
        if ranks[name]['life'] <= 0:
            print('- ' + name)
            delete.append(name)
    for name in delete:
        del ranks[name]
    file = open(rankdb, 'w')
    file.write(json.dumps(ranks))
    file.close()
    keys = [int(key['rank']) for key in ranks.values()]
    keys.sort()
    file = open(ranking, 'w')
    ranks2 = {ranks[name]['rank'] : {'name' : name, 'score' : ranks[name]['score'], 'ID' : ranks[name]['ID']} for name in ranks}
    file.write("Rank: Name" + ' '*21 + ": Score" + '  ' + ": Life : ID\n")
    for i in range(1, len(ranks) + 1):
        for name in ranks:
            if int(ranks[name]['rank']) == i:
                file.write(str(i) + ' '*(4 - len(str(i))) + ': ' + name + ' '*(25 - len(name)) + ': ' + ranks[name]['score'] + ' '*(7 - len(ranks[name]['score'])) + ': ' + str(ranks[name]['life']) + ' '*(5 - len(str(ranks[name]['life']))) + ': ' + ranks[name]['ID'] + '\n')
    file.close()
