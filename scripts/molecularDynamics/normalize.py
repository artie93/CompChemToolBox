###
###          NORMALIZE.PY
###
### This program takes a series of output files obtained from cpptraj-based 
### analysis of MD simulations whose format must be .txt (change it at will on line 20) and 
### on line 20) and contents should be in the standard cpptraj output format. Output files
### taken as input by this program include the ones given off by the modules lie, rmsd, 
### distance, angleinfo and dihedral. The result is a list of normalized average values for each input file.
###
### Usage: python3 normalize.py
###
### Artur Hermano, Manchester UK 2023
###


import os
variables = {}

dir_path = os.getcwd()
list_of_files = sorted(file for file in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path,file)) and file[-4:] == '.txt' and file[:4] != 'rmsf')

for file in list_of_files:
	
	reading = open(file,'r')
	values = []
	file_line = reading.readline()
	file_line = reading.readline()
	while(file_line):
		
		file_line1 = ' '.join(file_line.rstrip().split())
		line = file_line1.split(' ')
		values.append(float(line[1]))
		
		file_line = reading.readline()
	
	top = max(values)
	bot = min(values)
	ran = top - bot
	normalized_values = [(i-bot)/ran for i in values]
	variables[file[:-4]] = sum(normalized_values)/len(normalized_values)


	reading.close()           
	
for i,j in variables.items():
	print('The normalized average of '+str(i)+' is '+str(j)+' !!'+'\n')
