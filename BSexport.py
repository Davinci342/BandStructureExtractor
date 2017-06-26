# -*- coding: utf-8 -*

import numpy as np

BSlist = []

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
        if line != '\n':
            BSlist.append(line) 
        else:
            continue

#Let's define the number of bands, datapoints per band, and up and down matrices
bandnum = len(BSlist)//Count//2-1
datap = Count-1
UpListx = np.zeros((datap,1))
UpListy = np.zeros((datap,bandnum))

DnListx = np.zeros((datap,1))
DnListy = np.zeros((datap,bandnum))

#break the list up into energy (listx) and k-matrix (listy) for both up and down bands
        
x = y = 0
q=-1
for x in range(0,len(BSlist)):
    if 'Spin.Up' in BSlist[x]:
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

x = y = 0
q=-1
for x in range(0,len(BSlist)):
    if 'Spin.Down' in BSlist[x]:
        q=q+1        
        w=0
        for y in range (x+1,x+(Count)):
            DnListy[w,q-1] = BSlist[y].split()[1]
            w=w+1
            continue
        x = x + Count

#determine total number of up bands in energy range

totband=0
for z in range(0,bandnum):
    h=0
    for x in range(0,datap):
        if UpListy[x,z] >= lwbnd and UpListy[x,z] <= upbnd:
            h=1
            continue
    if h == 1:
        totband=totband+1
        continue

dumpbin = np.zeros((datap,1))
outbin = np.zeros((datap,totband))

#print them out

j=-1
for z in range(0,bandnum):
    h=0
    for x in range(0,datap):
        dumpbin[x,0]=UpListy[x,z]
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
        s = str(UpListx[x,0])
        for z in range(0,totband):
            s = s + '\t' + str(outbin[x,z])
            continue
        s = s + '\n'
        up.write(s)

#determine total number of down bands in energy range

totband=0
for z in range(0,bandnum):
    h=0
    for x in range(0,datap):
        if DnListy[x,z] >= lwbnd and DnListy[x,z] <= upbnd:
            h=1
            continue
    if h == 1:
        totband=totband+1
        continue

dumpbin = np.zeros((datap,1))
outbin = np.zeros((datap,totband))

#print them out

j=-1
for z in range(0,bandnum):
    h=0
    for x in range(0,datap):
        dumpbin[x,0]=DnListy[x,z]
        if dumpbin[x,0] >= lwbnd and dumpbin[x,0] <= upbnd:
            h=1
            continue
    if h == 1:
        j = j+1
        for y in range(0,datap):
            outbin[y,j] = dumpbin[y,0]
            continue

with open(downoutfilename, "w") as up:
    for x in range(0,datap):
        s = str(DnListx[x,0])
        for z in range(0,totband):
            s = s + '\t' + str(outbin[x,z])
            continue
        s = s + '\n'
        up.write(s)
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
        
