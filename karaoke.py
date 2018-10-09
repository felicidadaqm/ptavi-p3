#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
from collections import OrderedDict
import json

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

if __name__ == "__main__":

    parser = make_parser()
    cHandler = Print()
    parser.setContentHandler(cHandler)

    fichero = sys.argv[1]

    try:
        parser.parse(open(fichero))
    except (FileNotFoundError, IndexError):
        sys.exit("Usage: python3 karaoke.py file.smil")

 #   print(cHandler.get_tags())
    cHandler.print_line()
    cHandler.print_json()
