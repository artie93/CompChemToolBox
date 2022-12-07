###
###                         charmm2amber.py
###
### this program takes a .pdb file and formats all its atoms names into amber-standard names
### usage: python3 charmm2amber.py input_file.pdb output_file.pdb
### Artur Hermano, contact: artur.hermano@hotmail.com
###
###

import sys 
reading = open(sys.argv[1],'r')
writing = open(sys.argv[2],'w')

lines = reading.readlines()
for i in lines:
	if (len(i)<11 or ',' in i):
		writing.write(i)
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'ALA'):
		writing.write(i.replace("HN","H ").replace("OT1","O  ").replace("OT2","OXT"))
	
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'THR'):
		writing.write(i.replace("HT1","H3 ").replace("HT2","H2 ").replace("HT3","H1 "))
	
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'ILE'):
		writing.write(i.replace(" HD1","HD12").replace(" HD2","HD13").replace(" HD3","HD11").replace("CD ","CD1").replace("HG11","HG13"))
	
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'PRO'):
		writing.write(i.replace("HB1","HB3").replace("HG1","HG3").replace("HD1","HD3"))
	
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'HSP' or ' '.join(i.rstrip().split()).split(' ')[3] == 'HSD' or ' '.join(i.rstrip().split()).split(' ')[3] == 'HSE'):
		writing.write(i.replace("HSP","HIP").replace("HSE","HIE").replace("HSD","HID").replace("HB1","HB3"))
	
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'LEU'):
		writing.write(i.replace("HB1","HB3"))
		
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'ASP'):
		writing.write(i.replace("HB1","HB3"))
		
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'PHE'):
		writing.write(i.replace("HB1","HB3"))
	
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'SER'):
		writing.write(i.replace("HB1","HB3").replace("HG1","HG "))
		
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'TYR'):
		writing.write(i.replace("HB1","HB3"))
	
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'GLN'):
		writing.write(i.replace("HB1","HB3").replace("HG1","HG3"))
	
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'ARG'):
		writing.write(i.replace("HB1","HB3").replace("HG1","HG3").replace("HD1","HD3"))
	
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'GLY'):
		writing.write(i.replace("HA1","HA3"))
	
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'LYS'):
		writing.write(i.replace("HB1","HB3").replace("HG1","HG3").replace("HD1","HD3").replace("HE1","HE3"))
	
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'TRP'):
		writing.write(i.replace("HB1","HB3"))
	
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'ASN'):
		writing.write(i.replace("HB1","HB3"))
	
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'GLU'):
		writing.write(i.replace("HB1","HB3").replace("HG1","HG3"))
		
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'CYM'):
		writing.write(i.replace("HB1","HB3").replace("HG1","HG ").replace("CYM","CYS"))
		
	elif (' '.join(i.rstrip().split()).split(' ')[3] == 'MET'):
		writing.write(i.replace("HB1","HB3").replace("HG1","HG3"))
	else:
		writing.write(i)
		
reading.close()
writing.close()
