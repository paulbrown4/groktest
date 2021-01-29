#!/usr/bin/python

from pygrok import Grok
from optparse import OptionParser
from PyQt4 import QtXmlPatterns

parser = OptionParser()
parser.add_option("-i", "--input", dest="input", help="Text or file with the data to parse.")
parser.add_option("-p", "--pattern", dest="pattern", help="Grok pattern(s) to test.")
(options, args) = parser.parse_args()

def grokmatch(text,pattern):
    grok = Grok(pattern)
    output = grok.match(text)
    if output is None:
        return("No matches found")
    else:
        return(output) 

def main():
    contents = open(options.input, "r").readlines()
    patterns = open(options.pattern, "r").readlines()
    print(type(patterns)) 
    print(type(contents))
    
    for line in contents:
        for pattern in patterns: 
            print("----")
            print("Line: " + line.strip("\n"))
            print("Pattern:" + pattern.strip("\n"))
            result = grokmatch(line, pattern)
            
            print(result)
    
if __name__ == "__main__" :
    main()
    