###
###    genPDBs.py
###
###  This code simply extracts all frames of a molecular dynamics
###  trajectory and converts each one into a PDB file whose names
###  are CAVER-friendly. 
### 
###  Usage: python3 genPDBs.py (see lines 27-28 below)
###  
###  Artur Hermano and Thirakorn Mokkawes, Manchester UK 2022
 
import pytraj as pt                                                         #before executing this program, make sure
import os                                                                   #to create a subdirectory called 'frames'
                                                                            #inside your working directory

def load_traj(traj_file,prmtop_file):                                       #this function takes a trajectory and a
    loaded_traj = pt.load(traj_file,top=prmtop_file)                        #topology files and load them into an 
    print('traj is loaded!')                                                #object, which is returned as variable
    return loaded_traj

def rename_all(input_dir):                                                  #this function takes a directory's path
    files = os.listdir(input_dir)                                           #and then each file that is inside of it
    for i in files:                                                         #gets properly renamed, e.g. the file   
        j='{:05}'.format(int(i.split('.')[1]))+'.pdb'                       #whose name is '.444' will be renamed to
        os.rename(os.path.join(input_dir,i), os.path.join(input_dir,j))     #'frame00444.pdb'

input_nc = './prod5all.nc'                                                  #insert your trajectory file name here
input_prmtop = './mut05_solv.prmtop'                                        #insert your topology file name here

input_traj=load_traj(input_nc,input_prmtop)                                 
pt.save('./frames/',input_traj,format='PDB',overwrite=True,options='multi') 
rename_all('./frames/')                                                     
