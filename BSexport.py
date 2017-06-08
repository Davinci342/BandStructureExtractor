# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 12:26:42 2017

@author: MaterialsTheory
"""

fh = open("test.txt","r") 
import numpy as np
BandNumber= 200,324
ArrayUp = np.array[BandNumber].reshape[BandNumber,1]
ArrayDown = np.array[BandNumber].reshape[BandNumber,1]
#ArrayK = np.array[] /this needs to be defined for the k-points
#note: ideally we will want to replace these predefined values with input functions for the user

for BandIteration in range(0,BandNumber):
    #fh.readline()
    #def chop_comment(line):#need to look over
        #in_quote = False
        #for i, ch in enumerate(line):
            #if not in_quote and ch == c_comment:
                #return line[:i]
            #return line[:i]
        #return line[:i]
        fh.readline()
        line = fh.readline()
        if '#' in line:
            while not '\n\n':
                fh.readline()
                if 'Spin.Up' in line:#trying to get program to recognize spin up and spin down lines
                    np.save in ArrayUp
                    while not '\n\n':
                        fh.readline()
                        if '    ' in line:
                            line.split()
                            np.save in ArrayUp
                else:
                    if 'Spin.Down' in line:
                        np.save in ArrayDown
                        while not '\n\n':
                            fh.readline()
                            if '    ' in line:
                                line.split()
                                np.save in ArrayDown
        else:
            pass
        BandIteration = BandIteration + 1
x = ArrayUp.element
y = ArrayDown.element
if True:#need to change;this is incorrect syntax
    -2 < x < 2
    ArrayUp2 = ArrayUp.Where([x]).ToArray()
if True:
    -2 < y < 2
    ArrayDown2 = ArrayDown.Where([x]).ToArray()
print (ArrayUp2)
print (ArrayDown2)
fh.close()
