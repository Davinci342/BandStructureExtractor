# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 12:26:42 2017

@author: MaterialsTheory
"""

fh = open("test.txt","r") 
import numpy as np
BandNumber= 1641
c_comment = '#'
ArrayUp = np.spinup[BandNumber].reshape[BandNumber,2]
ArrayDown = np.spindown[BandNumber].reshape[BandNumber,2]

for BandIteration in range(0,BandNumber):
    fh.read(line)
    def chop_comment(line):#need to look over
        in_quote = False
        backslash_escape = False
        for i, ch in enumerate(line):
            if not in_quote and ch == c_comment:
                return line[:i]
    return line    
while not '\n\n':
                if True:#trying to get program to recognize spin up and spin down lines
                    fh.readline('Spin.Up')
                    store in ArrayUp  #this might only store the lines that define the bands, not the actual lines that contain data
                    fh.readline()
                    if
                else:
                    store in ArrayDown
                    if
return ArrayUp
return ArrayDown
print ArrayUp
print ArrayDown
fh.close()
