import json

file = open("G:/Users/Jozhus/Documents/Python/data/waifudb.txt", 'r')
db = json.loads(file.read())

def display():
    flipped = {int(db[x]):x for x in db}
    indexes = list(flipped.keys())
    indexes.sort()
    for i, x in enumerate(indexes):
        print(str(i + 1) + ' '*(3 - len(str(i + 1))) + ': ' + str(x) + ' '*(6 - len(str(x)))  + ': ' + flipped[x].encode('ascii', 'ignore').decode('utf-8'))

display()
input()
