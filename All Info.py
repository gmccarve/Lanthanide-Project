import glob
import shutil
from shutil import copyfile
import os
from itertools import islice

f_block = ['lanthanum', 'cerium', 'praseodymium', 'neodymium', 'promethium', 'samarium', 'europium', 'gadolinium', 'dysprosium', 'holmium', 'thulium', 'ytterbium', 'lutetium', 'terbium', 'erbium',]

Ln = ['La1', 'Ce1', 'Pr1', 'Nd1', 'Pm1', 'Sm1', 'Eu1', 'Gd1', 'Tb1', 'Dy1', 'Ho1', 'Er1', 'Tm1', 'Yb1', 'Lu1',]

searchpath = 'C:/Users/Gavin/Desktop/Research/Crystal Database/Clean DataBase/'
path1 = searchpath + 'Data/'
path2 = path1 + 'DataBase Results2.csv'
Bonds = open(path2, 'w')
path3 = path1 + 'Chemical Names.txt'
Name1 = open(path3, 'w')
path4 = searchpath + 'No Bond Data/'
path5 = searchpath + 'Cleaner/'

if not os.path.exists(path4):
    os.makedirs(path4)

path = searchpath + 'Cleaner/*.CIF'

length = len(path[:-5])
files = glob.glob(path)
track3 = []
    
for name in files:
    track = []
    track1 = []
    count1 = 0
        
    with open(name) as f:
        itf = iter(f)
        count2, count3, sm, mean, name2 =   0, 0, 0, 0, ''
        for line in itf:
            if line.startswith('_chemical_formula_sum '):
                comp = line[23:-2]
            for item in Ln:
                if item in line:
                    if '1_555 ' in line:
                        count1 += 1
                        #line1 = line[:-12].replace(' ', ',')
                        line1 = line[:-12]
                        line1 = line1.replace(' ', ',')
                        track.append(line1[:-6] + ',' + ',' + line1[-6:] + '\n')
                        track1.append(line[-18:-12] + '\n')
                        sm +=  float(line[-18:-12])
                            
            if line.startswith('_chemical_name_systematic'):
                while count3 < 2:
                    name1 = next(itf)
                    if ';' in name1:
                        count3 += 1
                    else:
                        name2 = name2 + name1.replace('\n', '')

    
    if len(track) != 0 :
        if 'catena' not in name2 and 'clathrate' not in name2:
            Name1.write(name[length:-4] + '  ,  ' +  name2 + '\n')
            #shutil.copy(name, path5)
        if count1 == 0:
            count1 = 0
            #shutil.copy(name, path4)
            remove(name)
        else:
            mean = sm / count1
               
            Bonds.write("File Name - " + name[length:-4] + '\n')
            Bonds.write("Full Name - " + str(name2) + '\n')
            Bonds.write("Composition - " + str(comp) + '\n')
            Bonds.write("Minimum Bond Length - " + str(min(track1)))
            Bonds.write("Average Bond Length - " + "%.3f" % round(mean, 3) + '\n')
            Bonds.write("Bonds - "  + '\n')
            
            for items in track:
                Bonds.write('        ' + items)
            Bonds.write('\n')

    
    #track3.append(name[length:length+6])

    
                       
Bonds.close()
Name1.close()



