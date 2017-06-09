# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 12:26:42 2017

@author: MaterialsTheory
"""

fh = open("test.txt","r")
up = open("spinup.txt","w")
dn = open("spindown.txt","w")
c_comment = '#'
#ArrayK = np.array[] /this needs to be defined for the k-points
#note: ideally we will want to replace these predefined values with input functions for the user
    #fh.readline()
    #def chop_comment(line):#need to look over
        #in_quote = False
        #for i, ch in enumerate(line):
           #if not in_quote and ch == c_comment:
                #return line[:i]
           # return line[:i]
       # return line[:i]
fh.readlines()
for line in fh:
    if c_comment in line:
        if 'Spin.Up' in line:
            up.write(line)
            fh.readline()
            list = []
            list.append()
            if [1] in range(-2,2):
                up.write(line)
       
                    break
        if 'Spin.Down' in line:
            dn.write(line)
            if '    ' in line:
                float(line.split())
                if [1] in range(-2,2):
                    dn.write(line)
        
                    if '    ' in line:
                        float(line.split())
                        np.save in ArrayUp
            else:
                np.save in ArrayDown
                while not '\n\n':
                    fh.readline()
                    if '    ' in line:
                        line.split()
                        np.save in ArrayDown
         elif '\n' in line:
             pass
fh.close()
