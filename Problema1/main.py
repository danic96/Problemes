#PERMET EXECUTAR EL FITXER SENSE "python" DAVANT
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Client web per www.udl.cat

@author: dcv4@alumnes.udl.cat
'''

import urllib2
from bs4 import BeautifulSoup


class Client(object):

    def get_web(self, page):
        '''baixarse la web'''
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html

    def search_text(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find_all("div", "featured-links-item")
        resultats = []
        for element in elements:
            data = element.find("time")["datetime"]
            title = element.find("span", "flink-title")
            if title:
                title = title.getText()
            else:
                title = "Sense text"
            print title
            resultats.append((title,data))
        return resultats

    def main(self):
        web = self.get_web("http://www.udl.cat/")
        # TODO: buscar el text
        resultat = self.search_text(web)
        # FIXME: impreimir resultat
        print resultat


if __name__ == "__main__":
    client = Client()
    client.main()
