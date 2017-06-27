# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 14:31:16 2017

@author: rithv
"""

import numpy as np

DOSlist = []

infilename = ("DOStest.txt")
outfilename = ("DOStestout.txt")
 
uprng = 2.0
lwrng = -2.0

with open(infilename, "r") as fh: 
    Count = 0
    for line in fh: 
        Count += 1

with open(infilename, "r") as fh:
    for line in fh:
        if 'energy' in line:
            for line in fh:
                DOSlist.append(line)
                
datap = Count-8
dumpbin = np.zeros((datap,3))

y=z=0
for x in range(0,datap):
    dumpbin[x,0]=float(DOSlist[x].split()[0])
    dumpbin[x,1]=float(DOSlist[x].split()[1])    
    dumpbin[x,2]=float(DOSlist[x].split()[2])

        
   
with open(outfilename, "w") as ot:
    for x in range(0,len(dumpbin)):
            if dumpbin[x,0] >= lwrng and dumpbin[x,0] <= uprng:
                ot.write(str(dumpbin[x,0])+ "\t\t\t")
                ot.write(str(dumpbin[x,1])+ "\t\t\t")
                ot.write(str(dumpbin[x,2])+ "\n")
         
                


                

