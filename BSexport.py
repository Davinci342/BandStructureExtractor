# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 12:26:42 2017

@author: MaterialsTheory
"""

fh = open("test.txt","r") 
import numpy as np
BandNumber= 200,324
c_comment = '#'
ArrayUp = np.spinup[BandNumber].reshape[BandNumber,2]
ArrayDown = np.spindown[BandNumber].reshape[BandNumber,2]

for BandIteration in range(0,BandNumber):
    #fh.readline()
    #def chop_comment(line):#need to look over
        #in_quote = False
        #for i, ch in enumerate(line):
            #if not in_quote and ch == c_comment:
                #return line[:i]
            #return line[:i]
        #return line[:i]
    if True:
        fh.readline('c_comment')
        while not '\n\n':
                if True:#trying to get program to recognize spin up and spin down lines
                    fh.readline('Spin.Up')
                    if True:
                        fh.readline('"____"')
                        np.save in ArrayUp
                else:
                    if True:
                        fh.readline('"____"')
                        np.save in ArrayDown
                    return ArrayUp
                    return ArrayDown
x = ArrayUp.element
y = ArrayDown.element
if True:
    -2 < x < 2
    ArrayUp2 = ArrayUp.Where([x]).ToArray()
if True:
    -2 < y < 2
    ArrayDown2 = ArrayDown.Where([x]).ToArray()
print (ArrayUp2)
print (ArrayDown2)
fh.close()
