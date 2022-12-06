### 
###          EXTRACT.PY
### 
### This program takes a Gaussian output file from a frequency calculation and from it extracts 
### the relevant energy values from the structure, as well as all charges and spin densities
### values for each atom of it. If your system is divided into sub-components (e.g. protein+substrate)
### you can also edit the numbers in the third part of this code to get the charges and spin densities
### for each one of the components (see below). Everything is written in a "final output" text file.
###
### Usage: python3 extract.py Gaussian_output_file.out Final_output_file.txt Number_of_Atoms_in_Your_System
###
### Artur Hermano, Manchester UK 2022
###

import sys
reading = open(sys.argv[1],'r')
writing = open(sys.argv[2],'w')
scf_list = []
file_line = reading.readline()
print('Reading file {} and extracting its energy values...'.format(sys.argv[1]))
while(file_line):
	file_line1 = ' '.join(file_line.rstrip().split())
	line = file_line1.split(' ')
	if (' '.join(line[0:2]) == 'Zero-point correction='):
		zero_point_correction = ' '.join(line)+'\n'
	if (' '.join(line[0:7]) == 'Sum of electronic and thermal Free Energies='):
		free_energy = ' '.join(line)+'\n'
	if (' '.join(line[0:2]) == 'SCF Done:') and (line[-4] == 'A.U.'):
		scf_list.append(' '.join(line))		
	file_line = reading.readline()
print('Done extracting energies.')

writing.write(scf_list[-1]+'\n')
writing.write(zero_point_correction)
writing.write(free_energy)
reading.close()                 #this was the first part of the code
                                #it simply extracts the energy values
                                #from the Gaussian output file and writes
                                #them in the .txt output file
########################################################################

reading = open(sys.argv[1],'r')
list_lines = reading.readlines()

print('Finding all charges and spin densities of each atom in your structure...')

last = max(idx for idx, val in enumerate(list_lines) if val.strip() == 'Mulliken charges and spin densities:')

for i in range(last,last+int(sys.argv[3])+2):
	writing.write(list_lines[i])

print('Done extracting charges and spin densities.')

reading.close()                 #this was the second part of the code
writing.close()                 #it prints the charges and spin densities
                                #of every atom from your cluster model
                                #in the .txt output file
#######################################################################


writing = open(sys.argv[2],'a')
reading = open(sys.argv[2],'r')

print('Grouping all charges and spin densities into the individual sub-components of your system...')

spinLIG,spinFE,spinPOR,spinO,spinSUB,spinPROT = 0.0,0.0,0.0,0.0,0.0,0.0
cargLIG,cargFE,cargPOR,cargO,cargSUB,cargPROT = 0.0,0.0,0.0,0.0,0.0,0.0

file_line = reading.readline()
while(file_line):
    file_line1 = ' '.join(file_line.rstrip().split())
    line = file_line1.split(' ')
    if len(line) == 4 and line[-1][-1] != ')':
    	if int(line[0]) in range(1,30):
    		spinLIG += float(line[3])
    		cargLIG += float(line[2])
    	if int(line[0]) == 30:
    		spinFE = float(line[3])
    		cargFE = float(line[2])
    	if int(line[0]) in range(31,67):
    		spinPOR += float(line[3])
    		cargPOR += float(line[2])
    	if int(line[0]) == 67:
    		spinO = float(line[3])
    		cargO = float(line[2])
    	if int(line[0]) in range(68,101):
    		spinSUB += float(line[3])
    		cargSUB += float(line[2])
    	if int(line[0]) in range(101,223):
    		spinPROT += float(line[3])
    		cargPROT += float(line[2])
    file_line = reading.readline()
writing.write('\n')
writing.write('CHARGES AND SPIN DENSITIES PER SUB-COMPONENT IN YOUR STRUCTURE:'+'\n')
writing.write('\n')
writing.write('Axial Ligand Charge: '+str(cargLIG)+'\n')
writing.write('Axial Ligand Spin Density: '+str(spinLIG)+'\n')
writing.write('\n')
writing.write('Iron(Fe) Charge: '+str(cargFE)+'\n')
writing.write('Iron(Fe) Spin Density: '+str(spinFE)+'\n')
writing.write('\n')
writing.write('Porphyrin ring Charge: '+str(cargPOR)+'\n')
writing.write('Porphyrin ring Spin Density: '+str(spinPOR)+'\n')
writing.write('\n')
writing.write('Oxygen Charge: '+str(cargO)+'\n')
writing.write('Oxygen Spin Density: '+str(spinO)+'\n')
writing.write('\n')
writing.write('Substrate Charge: '+str(cargSUB)+'\n')
writing.write('Substrate Spin Density: '+str(spinSUB)+'\n')
writing.write('\n')
writing.write('Protein Charge: '+str(cargPROT)+'\n')
writing.write('Protein Spin Density: '+str(spinPROT)+'\n')

reading.close()            #this is the third and final part of the code
writing.close()            #for it to work properly, you must edit it for
                           #your own system accordingly to its atom numbers,
                           #e.g. in my system above I have a system composed
                           #of 6 components: axial ligand(atoms #1-29),
                           #iron(atom #30),porphyrin ring(atoms #31-66), 
                           #oxygen(atom #67), substrate(atoms #68-100) and
                           #protein(atoms #101-222). Feel free to add/delete
                           #components to fit your needs
#########################################################################
print('Done.')
