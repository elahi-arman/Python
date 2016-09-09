import requests
import bs4
import re
from unidecode import unidecode
from pandas import DataFrame

class Wikitable():

    def __init__(self, soup):
        self.soup = soup
        self.table = soup.find('table', {
                        'class': 'wikitable'
                     })
        self.headers, self.rows = self._parseTable(self.table)

    def _parseTable(self, table):
        """
            Parse table into headers and rows

            Args:
                param1 (BS4.element.table): table to parse

            Returns:
                ([headers], [rows])
        """

        headers = []
        rows = []

        #remove cite-notes of the form [8]
        noCiteNotes = re.compile("\[[0-9]*\]")
        noDelimiters = re.compile(",|\n")

        for descendant in table.descendants:
            if descendant.name == 'th':
                headers.append(descendant.text)
            elif descendant.name == 'tr':
                tr = []
                for td in descendant.children:
                    if type(td) == bs4.element.NavigableString:
                        if td.string is not '\n':
                            tr.append(str(td.string))
                    else:
                        if td.text is not '\n':
                            string = re.sub(noCiteNotes, '', td.text)
                            tr.append(re.sub(noDelimiters, '', string))
                rows.append([text for text in tr if text != '\n'])

        # the first tr is the headers which is already caught by the th filter
        del rows[0]

        return (headers, rows)


    def toCSV(self, filePath):
        """
            Writes the Table as a CSV to the specified file regardless of existence

            Args:
                param1 (str): path to a file .

            Returns:
                None

            Side Effects:
                Writes to the file specified by filepath

            Use this as opposed to self.df.to_csv from pandas as this method
            goes through the extra step of normalizing unicode characters using
            the unidecode module. If Unicode characters are not a problem,
            then self.df.to_csv is much faster.
        """

        noBrackets = re.compile("\[|\]")

        with open(filePath, 'w+') as f:
            f.write(str(self.headers))
            f.write('\n\n')

            for row in self.rows:
                f.write(re.sub(noBrackets, '', unidecode(str(row) + '\n')))

    def toPandasDF(self):
        """ Assembles DataFrame from the headers and rows of the Wikitable """
        return DataFrame(self.rows, columns = self.headers)


if __name__ == '__main__':

    r = requests.get('https://en.wikipedia.org/wiki/List_of_stadiums_by_capacity')
    d = Wikitable(bs4.BeautifulSoup(r.content, 'html5lib'))
    d.toCSV('stadiums.csv')
