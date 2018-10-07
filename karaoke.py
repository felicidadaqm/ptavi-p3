#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
from collections import OrderedDict

class Print (smallsmilhandler.smallSMILHandler):

    def print_line(self): 
        exit = ""
        for dicc in self.tag:
            exit += str("\n" + dicc['tag'])
            for key in dicc:
                if key != 'tag' and dicc[key] != 'Null':
                    exit += str(key + "=" + dicc[key])
        print(exit)

if __name__ == "__main__":

    parser = make_parser()
    cHandler = Print()
    parser.setContentHandler(cHandler)

    try:
        fichero = sys.argv[1]
        parser.parse(open(fichero))
    except (FileNotFoundError, IndexError):
        sys.exit("Usage: python3 karaoke.py file.smil")

 #   print(cHandler.get_tags())
    cHandler.print_line()
