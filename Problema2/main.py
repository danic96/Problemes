#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

import sys
import urllib2
from bs4 import BeautifulSoup as bs

api_key = None


class WeatherClient(object):
    """docstring foe WeatherClient"""
    url_base = "http://api.wunderground.com/api/"
    url_service = {
        "almanac": "/almanac/q/CA/"
    }
    def __init__(self, api_key):
        super(WeatherClient, self).__init__()
        self.api_key = api_key

    def almanac(self, location):
        # baixar-se la web
        url = self.url_base + self.api_key + self.url_service["almanac"] + \
            location + ".xml"
        print url
        f = urllib2.urlopen(url)
        data = f.read()
        f.close()

        # llegir-la
        soup = bs(data, 'lxml')
        maximes = soup.find("temp_high")
        normal = maximes.find("normal").find("c").text
        record = maximes.find("record").find("c").text
        # retornar resultats
        return normal, record


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "API Key must be in CLI option"

    wc = WeatherClient(api_key)
    result = wc.almanac("Lleida")
    print result
