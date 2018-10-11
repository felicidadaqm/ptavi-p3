#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
import smallsmilhandler
import sys
from collections import OrderedDict
import json
from urllib.request import urlretrieve
import urllib

class Print (smallsmilhandler.smallSMILHandler):

    def print_line(self): 
        exit = ""
        for dicc in self.tag:
            exit += str("\n" + dicc['tag'] + "\t")
            for key in dicc:
                if key != 'tag' and dicc[key] != '':
                    exit += str(key + "=\"" + dicc[key] + "\"\t")
        print(exit)

    def print_json(self):
        with open('karaoke.json', 'w') as json_file:
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

    parser = make_parser()
    cHandler = Print()
    parser.setContentHandler(cHandler)

    fichero = sys.argv[1]

    try:
        parser.parse(open(fichero))
    except (FileNotFoundError, IndexError):
        sys.exit("Usage: python3 karaoke.py file.smil")

    cHandler.print_line()
    cHandler.print_json()
    cHandler.download()
