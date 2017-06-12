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
list = []
i = 7564
j = i+1


#ArrayK = np.array[] /this needs to be defined for the k-points
#note: ideally we will want to replace these predefined values with input functions for the user
for line in fh:
    fh.readline()
    if line.startswith('\n'):
        pass
    else:
        BSlist.append(line)
for i in range(len(BSlist[i:i+30])):
    if i <= 7594:
        list.append(line.split(BSlist[i]))
        print(list)
        if [2] in range(2,-2):
            BS.write(("BSlist[i+30]"))
#            str.index(str, beg=0 end=len(string))
fh.close()
BS.close()
up.close()
dn.close()
