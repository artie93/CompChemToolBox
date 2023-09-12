###
###              replace.py
###
###  This code does the very simple but very useful task of
###  correcting the content of a file whose index places ran
###  out of space so they were turned into '****', e.g.
###
###    .         .                      .      . 
###    .         .                      .      .
###    .         .                      .      .
###  99700     value1                99700   value1
###  99800     value2     is         99800   value2
###  99900     value3  converted     99900   value3
###  *****     value4       to      100000   value4
###  *****     value5               100100   value5
### 
###  This code does this for every file inside your working
###  directory, creating new 'clean" files. Please adjust
###  your index limit and step in the lines 36 and 40 below.
###
###  Artur Hermano, Campinas SP Brazil, 2021
###

import os

dir_path = os.getcwd()

list_of_files = sorted(file for file in os.listdir(
    dir_path) if os.path.isfile(os.path.join(dir_path, file)))

for file in list_of_files:
    reading = open(file, 'r')
    writing = open(''.join([str(file), '_clean.dat']), 'w')

    line = reading.readline()
    count = 100000000                        #your limit beyond which you get **** in your indexes
    while(line):
        line1 = ' '.join(line.rstrip().split())
        line = line1.split(' ')
        if line[0] != '********':
            writing.write('\t'.join(line)+'\n')
        else:
            writing.write('\t'.join([str(count), line[1]])+'\n')
            count += 100                     #the pace at which your index increases
        line = reading.readline()

    reading.close()
    writing.close()
