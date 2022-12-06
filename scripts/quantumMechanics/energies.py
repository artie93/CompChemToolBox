####
#### ENERGIES.PY
#### This program takes as input two output 
#### files FROM THE PROGRAM EXTRACT.PY and 
#### shows the energy differences between them!
####
#### Usage: python3 energies.py OUTPUT_FILE_1 OUTPUT_FILE_2 
####
#### The output_file_1 should refer to the initial 
#### structure, while output_file_2 should refer to
#### the final structure. You can adjust it to your own 
#### specific needs, but if you have any questions, just e-mail artur.hermano@hotmail.com
#### 
#### Artur Hermano, Manchester, UK, 2022

import sys
start = open(sys.argv[1],'r')
end = open(sys.argv[2],'r')

start_E,start_ZPE,start_G = 0,0,0
end_E,end_ZPE,start_G = 0,0,0

line_start = start.readline()
while(line_start):
	line1 = ' '.join(line_start.rstrip().split())
	line = line1.split(' ')
	if (' '.join(line[0:2]) == 'SCF Done:'):
		start_E = float(line[4])
	if (' '.join(line[0:2]) == 'Zero-point correction='):
		start_ZPE = float(line[-2])
	if (' '.join(line[0:2]) == 'Sum of'):
		start_G = float(line[-1])
	line_start = start.readline()

line_end = end.readline()
while(line_end):
	line1 = ' '.join(line_end.rstrip().split())
	line = line1.split(' ')
	if (' '.join(line[0:2]) == 'SCF Done:'):
		end_E = float(line[4])
	if (' '.join(line[0:2]) == 'Zero-point correction='):
		end_ZPE = float(line[-2])
	if (' '.join(line[0:2]) == 'Sum of'):
		end_G = float(line[-1])
	line_end = end.readline()
print()
print("The energy difference from {} to {} is {} kcal/mol".format(sys.argv[1][:-4],sys.argv[2][:-4],(end_E - start_E)*627.51))
print()
print("The energy difference with zero-point correction from {} to {} is {} kcal/mol".format(sys.argv[1][:-4],sys.argv[2][:-4],(end_E + end_ZPE - start_E - start_ZPE)*627.51))
print()
print("The free energy from {} to {} is {} kcal/mol".format(sys.argv[1][:-4],sys.argv[2][:-4],(end_G - start_G)*627.51))
print()

