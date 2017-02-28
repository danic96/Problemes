#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

import sys

api_key = None


class WeatherClient(object):
    """docstring foe WeatherClient"""
    def __init__(self, api_key):
        super(WeatherClient, self).__init__()
        self.api_key = api_key


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "API Key must be in CLI option"

    wc = WeatherClient(api_key)
    result = wc.almanac("Lleida")
