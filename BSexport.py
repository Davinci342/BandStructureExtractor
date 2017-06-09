# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 12:26:42 2017

@author: MaterialsTheory
"""

fh = open("test.txt","r")
BS = open("bandstructure.txt","w")
up = open("spinup.txt","w")
dn = open("spindown.txt","w")
c_comment = '#'
#ArrayK = np.array[] /this needs to be defined for the k-points
#note: ideally we will want to replace these predefined values with input functions for the user
fh.readlines()
for line in fh:
    if c_comment in line:
        if 'Spin.Up' in line:
            BS.write(line)
        elif 'Spin.Down' in line:
            BS.write(line)
    if '    ' in line:
            float(line.split())
            if [1] in range(-2,2):
                BS.write(line)
fh.close()
fh_ = open("bandstructure.txt","r")
fh_.readlines()
for line in fh_:
    if c_comment in line:
        if 'Spin.Up' in line:
            up.write(line)
    if '    ' in line:
        up.write(line)
fh_.readlines()
for line in fh_:
    if c_comment in line:
        if 'Spin.Down' in line:
            dn.write(line)
    if '    ' in line:
        dn.write(line)
fh_.close()
