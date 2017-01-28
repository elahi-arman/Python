import requests
import bs4

def write_game_to_file(fileTitle, url, tableType='_basic'):

    if '_basic' not in tableType or '_advanced' not in tableType:
        tableType = '_basic'

    r = requests.get(url);
    soup = bs4.BeautifulSoup(r.content, 'lxml')
    lastPlayer = ''
    players = dict()
    fields = []
    count = 0

    table_bodies = soup.find_all("tbody")
    print (table_bodies)
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

    # fields[0] = 'Players'
    # with open(fileTitle, 'w+') as f:
    #     f.write(str(fields))
    #     f.write('\n')
    #     for player in players:
    #         f.write(str(player) + '\t',)
    #         for stats in players[player]:
    #             f.write(str(stats) + '\t')
    #         f.write('\n')

def read_file_from_urls(url_file):
    with open(url_file, 'r') as urls:
        for url in urls:
            write_game_to_file(url[-18:-5] + '.txt', url)

if __name__ == '__main__':
    read_file_from_urls('1617Warriors/games.txt')
