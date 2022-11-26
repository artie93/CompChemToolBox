### 
###              PROTVERIFY.PY 
### 
### This code takes as input the .pdb file outputted by the H++ server and shows
### all ASP, GLU and HIS residues in the protein and their respective protonation
### states - useful for manually building your topology with psfgen in NAMD.
### 
### Important: Delete all empty lines from your H++ file before using this code!
### Usage: python3 protverify.py H++file.pdb
### 
### Artur Hermano, Campinas SP Brazil, 2019

import sys
file = open(sys.argv[1],'r')
line = file.readline()
prot = []
HSP = []
HSE = []
HSD = []
i = 3
while(line):
        x = line.split()
        if x[0] == 'ATOM':
                if x[3] == "ASP" or x[3] == "GLU":
                        if x[2] == "HD2" or x[2] == "HE2":
                                prot.append(x[3]+'  '+x[4])
                if x[3] == "HIS" or x[3] == "HSP" or x[3] == "HSE" or x[3] == "HSD":
                        if x[2] == "HD1":
                                i = i + 2
                        if x[2] == "HE2":
                                i = i + 1
                        if x[2] == "O":
                                if i % 3 == 0:
                                        HSP.append(x[4])
                                if i % 4 == 0:
                                        HSE.append(x[4])
                                if i % 5 == 0:
                                        HSD.append(x[4])
                                i = 3
        line = file.readline()
print
print
if len(prot) == 1:
        print("In this pH, the following acid residue (RESID) is protonated:")
        for h in prot:
                print(h)
else:
        if len(prot) != 0:
                print("In this pH, the following acid residues (RESID) are protonated:")
                for h in prot:
                        print(h)
        else:
                print("In this pH, there are no protonated acid residues in this molecule!")
print
print
###################################################################################################
if len(HSP) == 1:
        print("In this pH, the only HSP histidine in this structure is the residue (RESID):",' '.join(HSP))
else:
        if len(HSP) != 0:
                print("In this pH, the HSP histidines in this structure are the residues (RESID):",' '.join(HSP))
        else:
                print("In this pH, there are no HSP histidines in this structure!")
print
print
###################################################################################################
if len(HSE) == 1:
        print("In this pH, the only HSE histidine in this structure is the residue (RESID):",' '.join(HSE))
else:
        if len(HSE) != 0:
                print("In this pH, the HSE histidines in this structure are the residues (RESID):",' '.join(HSE))
        else:
                print("In this pH, there are no HSE histidines in this structure!")
print
print
###################################################################################################
if len(HSD) == 1:
        print("In this pH, the only HSD histidine in this structure is the residue (RESID):",' '.join(HSD))
else:
        if len(HSD) != 0:
                print("In this pH, the HSD histidines in this structure are the residues (RESID):",' '.join(HSD))
        else:
                print("In this pH, there are no HSD histidines in this structure!")
print
print
file.close()
