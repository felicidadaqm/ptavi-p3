#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class smallSMILHandler(ContentHandler):

    def __init__(self):
        self.tag = []
        self.tag_dicc = {
                    'root-layout': ['width', 'height', 'background-color'],
                    'region': ['id', 'top', 'bottom', 'right', 'left'],
                    'img': ['src', 'region', 'begin', 'dur'],
                    'audio': ['src', 'begin', 'dur'],
                    'textstream': ['src', 'region']}

    def startElement(self, name, attrs):
        dicc = {}
        if name in self.tag_dicc:
            dicc['tag'] = name
            for attribute in self.tag_dicc[name]:
                dicc[attribute] = attrs.get(attribute, "")
            self.tag.append(dicc)

    def get_tags(self):
        return self.tag


if __name__ == "__main__":
    parser = make_parser()
    cHandler = smallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
