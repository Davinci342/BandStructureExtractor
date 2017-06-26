# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 14:48:43 2017

@author: MaterialsTheory
"""

# -*- coding: utf-8 -*

import numpy as np

DOSlist = []

infilename = str(input("Enter input bandstructure text file-name with the extension (.txt, .log, etc...): "))
upoutfilename = str(input("Enter output file-name for UP BANDS with extension (.txt, .log, etc...): "))
downoutfilename = str(input("Enter output file-name for DOWN BANDS with extension (.txt, .log, etc...): "))


lwbnd = -3.0
upbnd = 3.0


#Count the total lines for a band

with open(infilename, "r") as fh: 
    Count = 0
    for line in fh:
        if line == '\n':
            break
        Count += 1

#Copies data into a list

with open(infilename, "r") as fh:
    for line in fh:
        if 'energy' in line:
            for line in fh:
                if line != '\n':
                    DOSlist.append(line) 
                else:
                    continue

bandnum = len(DOSlist)//Count//2-1
datap = Count-1

        

q=-1


#determine total number of bands in energy range
for x in range(0,len(DOSlist)):
    if 'Spin.Up' in DOSlist[x]:
        q=q+1        
        w=0
        for y in range (x+1,x+(Count)):
            if x == 0:
                UpListx[y-1,0] = BSlist[y].split()[0]
                DnListx[y-1,0] = BSlist[y].split()[0]
                continue
            UpListy[w,q-1] = BSlist[y].split()[1]
            w=w+1
            continue
        x = x + Count

dumpbin = np.zeros((datap,1))
outbin = np.zeros((datap,totband))

#print them out

j=-1
for z in range(0,bandnum):
    h=0
    for x in range(0,datap):
        dumpbin[x,0]=DOSlist[x,z]
        if dumpbin[x,0] >= lwbnd and dumpbin[x,0] <= upbnd:
            h=1
            continue
    if h == 1:
        j = j+1
        for y in range(0,datap):
            outbin[y,j] = dumpbin[y,0]
            continue

with open(upoutfilename, "w") as up:
    for x in range(0,datap):
        s = str(DOSlist[x,0])
        for z in range(0,totband):
            s = s + '\n' + str(outbin[x,z])
            continue
        s = s + '\n'
        up.write(s)


#print them out
