#!/usr/bin/env python3
# Maintainer: Michael Rhodes. 

# This is a super simple python script that prettifies xml from either a supplied file or stdin in. 

from sys import argv, stdin
import xml.dom.minidom

xml_contents = ""
if len(argv) == 2: 
    filename = argv[1]

    with open(filename, 'r') as file:
        xml_contents = file.read()
else:
    xml_contents = stdin.read()


file_dom = xml.dom.minidom.parseString(xml_contents)
print(file_dom.toprettyxml())
