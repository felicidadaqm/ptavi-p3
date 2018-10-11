#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
import smallsmilhandler
import sys
from collections import OrderedDict
import json
from urllib.request import urlretrieve

class KaraokeLocal():

    def __init__(self):
        parser = make_parser()
        cHandler = smallsmilhandler.smallSMILHandler()
        parser.setContentHandler(cHandler)
        self.tag = cHandler.get_tags()

        file = sys.argv[1]
        try:
            parser.parse(open(file))
        except (FileNotFoundError):
            sys.exit("Usage: python3 karaoke.py file.smil")


    def __str__(self): 
        exit = ""
        for dicc in self.tag:
            exit += str("\n" + dicc['tag'] + "\t")
            for key in dicc:
                if key != 'tag' and dicc[key] != '':
                    exit += str(key + "=\"" + dicc[key] + "\"\t")
        print(exit)

    def to_json(self, json_name=''):
        file = sys.argv[1]
        if json_name == '':
            name = file[:file.rfind('.')]
            json_name = name + '.json' 
        with open(json_name, 'w') as json_file:
            json.dump(self.tag, json_file)
            letters = json.dumps(self.tag)
            print(letters)

    def download(self):
        for dicc in self.tag:
            if 'src' in dicc and 'http://' in dicc['src']:
                url = dicc['src']
                name= url[url.rfind('/')+1:]
                print(name)
                print(url)
                urlretrieve(dicc['src'], filename=name) 

if __name__ == "__main__":

    try:
        karaoke = KaraokeLocal()
    except (FileNotFoundError, IndexError):
        sys.exit("Usage: python3 karaoke.py file.smil")

    karaoke.__str__()
    karaoke.to_json()
    karaoke.download()
