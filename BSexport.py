# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 12:26:42 2017

@author: MaterialsTheory
"""

fh = open("test.txt","r")
BS = open("bandstructure.csv","w")
up = open("spinup.csv","w")
dn = open("spindown.csv","w")
BSlist = []
list = []
i = 7564
j = i+1


#ArrayK = np.array[] /this needs to be defined for the k-points
#note: ideally we will want to replace these predefined values with input functions for the user
for line in fh:
    if line.startswith('\n'):
        pass
    else:             
        BSlist.append(line) 
for i in range(len(BSlist[i:i+30])):
   if i <= 7594:
       list.append(line.split(BSlist[i]))
       print(list)
       print("\n")
       if [1] in range(2,-2):
           BS.write((str(BSlist[i+30])))
fh.close()
BS.close()
up.close()
dn.close()#edit
