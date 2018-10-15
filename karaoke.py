#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from urllib.request import urlretrieve
import smallsmilhandler
import sys
import json


class KaraokeLocal:

    def __init__(self):     # Initialize the program
        parser = make_parser()
        cHandler = smallsmilhandler.smallSMILHandler()
        parser.setContentHandler(cHandler)
        self.tag = cHandler.get_tags()

        file = sys.argv[1]
        parser.parse(open(file))

    def __str__(self):      # Prints tags in order, except the empty ones
        exit = ""
        for dicc in self.tag:
            exit += str("\n" + dicc['tag'] + "\t")
            for key in dicc:
                if key != 'tag' and dicc[key] != '':
                    exit += str(key + "=\"" + dicc[key] + "\"\t")
        return exit

    def do_json(self, json_name=''):    # Creates a json file
        file = sys.argv[1]
        if json_name == '':
            json_name = file.replace('.smil', '.json')
        with open(json_name, 'w') as json_file:
            json.dump(self.tag, json_file)

    def do_local(self):     # Downloads remote multimedia content
        for dicc in self.tag:
            if 'src' in dicc and 'http://' in dicc['src']:
                url = dicc['src']
                name = url[url.rfind('/')+1:]
                urlretrieve(dicc['src'], filename=name)


if __name__ == "__main__":

    try:
        karaoke = KaraokeLocal()
    except (FileNotFoundError, IndexError):
        sys.exit("Usage: python3 karaoke.py file.smil")

    print(karaoke)
    karaoke.do_json()
    karaoke.do_local()
    karaoke.do_json('local.json')
    print(karaoke)
