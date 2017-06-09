# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 12:26:42 2017

@author: MaterialsTheory
"""

fh = open("test.txt","r")
BS = open("bandstructure.txt","w")
up = open("spinup.txt","w")
dn = open("spindown.txt","w")
BSlist = []
CBSlist = []
Testlist = []
i = 0
j = i+1


#ArrayK = np.array[] /this needs to be defined for the k-points
#note: ideally we will want to replace these predefined values with input functions for the user
for line in fh:
    fh.readline()
    if line.startswith('\n'):
        pass
    else:
        BSlist.append(line)
for i in BSlist: 
    while i <= 30:
        list(line.split(BSlist[i]))
        if [1] in range(-2,2):
            CBSlist.append(BSlist[i:i+30])
            break
fh.close()
BS.close()
