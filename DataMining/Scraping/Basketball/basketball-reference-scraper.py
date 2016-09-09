import requests
import bs4
from  OrderedSet import OrderedSet

def write_game_to_file(fileTitle, url, tableType='_basic'):

    if '_basic' not in tableType or '_advanced' not in tableType:
        tableType = '_basic'

    r = requests.get(url);
    soup = bs4.BeautifulSoup(r.content, 'html5lib')
    lastPlayer = ''
    players = dict()
    fields = []
    count = 0

    table_bodies = soup.find_all("tbody")
    useful_tables = []

    for body in table_bodies:
        parent_id =  str(body.find_parent("table").get('id'))
        if (tableType in parent_id):
            useful_tables.append(body)


    for table in useful_tables:
        for descendant in table.descendants:
            if descendant.name == 'th':
                fields.append(descendant.text)
            if descendant.name == 'td':
                if " " in descendant.text:
                    lastPlayer = descendant.text
                    players[descendant.text] = []
                else:
                    players[lastPlayer].append(descendant.text)

    fields[0] = 'Players'
    with open(fileTitle, 'w+') as f:
        f.write(str(fields))
        f.write('\n')
        for player in players:
            f.write(str(player) + '\t',)
            for stats in players[player]:
                f.write(str(stats) + '\t')
            f.write('\n')

if __name__ == '__main__':
    urls = [
            'http://www.basketball-reference.com/boxscores/201606020GSW.html',
            'http://www.basketball-reference.com/boxscores/201606050GSW.html',
            'http://www.basketball-reference.com/boxscores/201606080CLE.html',
            'http://www.basketball-reference.com/boxscores/201606100CLE.html',
            'http://www.basketball-reference.com/boxscores/201606130GSW.html',
            'http://www.basketball-reference.com/boxscores/201606160CLE.html',
            'http://www.basketball-reference.com/boxscores/201606190GSW.html'
           ]
    for i in range(1, 8):
        write_game_to_file('game' + str(i) + '.txt', urls[i-1])
