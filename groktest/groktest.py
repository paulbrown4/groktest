#!/usr/bin/python

from pygrok import Grok
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input", dest="input", help="Text or file with the data to parse.")
parser.add_option("-p", "--pattern", dest="pattern", help="Grok pattern(s) to test.")
(options, args) = parser.parse_args()

def grokmatch(text,pattern):
    grok = Grok(pattern)
    output = grok.match(text)
    return(output) 

def main():
    contents = open(options.input, "r").readlines()
    patterns = open(options.pattern, "r").readlines()
    
    for line in contents:
        print("----")
        print("Line: " + line.strip("\n") + "\n  Matches: ")
        for pattern in patterns: 
            result = grokmatch(line, pattern)
            if result is not None:
                print("    Pattern: " + pattern.strip("\n"))
                print("    " + str(result) + "\n")
    
if __name__ == "__main__" :
    main()
    
