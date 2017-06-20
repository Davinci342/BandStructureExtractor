# -*- coding: utf-8 -*-
"""
Created on Mon Jun  15 06:13:42 2017

@author: MaterialsTheory
""" 

BSlist = []
UpList1 = []
DnList1 = []
    
with open("test.txt", "r") as fh: #finds Count (the number of lines of data) for one band.
    Count = 0
    for line in fh:
        if line == '\n':
            break
        Count += 1
   
with open("test.txt", "r") as fh: #makes the list from which data is refined
    for line in fh:
        if line != '\n':
            BSlist.append(line)
        else:
            continue

x = y = 0 #sorts the data into spin up or spin down, then in required eV range
for x in range(0,len(BSlist)):
    if 'Spin.Up' in BSlist[x]:
        for y in range (x+1,x+(Count)):
            if (float(BSlist[y].split()[1]) >= -2.0) and (float(BSlist[y].split()[1]) <= 2.0):
                UpList1.extend(BSlist[x:(x+(Count))])
                x = ((x // Count) * (Count)) + Count
                continue
    if 'Spin.Down' in BSlist[x]:
        for y in range (x+1,x+(Count)):
            if (float(BSlist[y].split()[1]) >= -2.0) and (float(BSlist[y].split()[1]) <= 2.0):
                DnList1.extend(BSlist[x:(x+(Count))])
                x = ((x // Count) * (Count)) + Count
                continue          

UpList2 = []#changing to csv form
x = y = 0
for x in range(0,Count):
    UpList2.append(str(x))
    if x != 0:
        y = x
        UpList2[x] = UpList2[x] + '\t' + UpList1[x].split()[0] + '\t' + UpList1[x].split()[1]
        while y in range(0,len(UpList1)):
            UpList2[x] = UpList2[x] + '\t' + UpList1[y].split()[1]
            y = y + Count
    if 'Spin.Up' in UpList1[x]:
        while y in range(0,len(UpList1)):
            UpList2[x] = UpList2[x] + '\t' + UpList1[y][UpList1[y].find('Band'):(UpList1[y].find('Band')+9)]
            y = y + Count 
            
DnList2 = []#changing to csv form
x = y = 0
for x in range(0,Count):
    DnList2.append(str(x))
    if x != 0:
        y = x
        DnList2[x] = DnList2[x] + '\t' + DnList1[x].split()[0] + '\t' + DnList1[x].split()[1]
        while y in range(0,len(DnList1)):
            DnList2[x] = DnList2[x] + '\t' + DnList1[y].split()[1]
            y = y + Count
    if 'Spin.Down' in DnList1[x]:
        while y in range(0,len(DnList1)):
            DnList2[x] = DnList2[x] + '\t' + DnList1[y][DnList1[y].find('Band'):(DnList1[y].find('Band')+9)]
            y = y + Count  

z = 0 #writes files
with open("spinup.txt", "w") as up:
    for z in range(0,len(UpList2)):
        up.write(UpList2[z])
        up.write('\n')
    
z = 0
with open("spindown.txt", "w") as dn:
    for z in range(0,len(DnList2)):
        dn.write(DnList2[z])
        dn.write('\n')
        
