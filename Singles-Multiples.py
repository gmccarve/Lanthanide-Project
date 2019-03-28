import glob
import shutil
import os

f_block = ['lanthanum', 'cerium', 'praseodymium', 'neodymium', 'promethium', 'samarium', 'europium', 'gadolinium', 'terbium',
           'dysprosium', 'holmium', 'erbium', 'thulium', 'ytterbium', 'lutetium']

Multiple = ['La1 ']
Bank = ['Ce1 ', 'Pr1 ', 'Nd1 ', 'Pm1 ', 'Sm1', 'Eu1 ', 'Gd1 ', 'Tb1 ', 'Dy1 ', 'Ho1 ', 'Er1 ', 'Tm1 ', 'Yb1', 'Lu1 ', 'end']

Ln = ['La1', 'Ce1', 'Pr1', 'Nd1', 'Pm1', 'Sm1', 'Eu1', 'Gd1', 'Tb1', 'Dy1', 'Ho1', 'Er1', 'Tm1', 'Yb1', 'Lu1',]

searchpath = 'C:/Research/Crystal DataBase/Pop DataBase/'

name3 = open(searchpath + 'Singles.txt', 'w')
name4 = open(searchpath + 'Multiples.txt', 'w')

track = []
count = 0
count1 = 0

for key in f_block:
    print (key)
    path = searchpath + key + '/*.CIF'
    path1 = searchpath + 'Singles/' 
    path2 = searchpath + 'Multiples/' + key + '/' 
    length = len(path[:-5])
    files = glob.glob(path)

    if not os.path.exists(path2):
        os.makedirs(path2)
    if not os.path.exists(path1):
        os.makedirs(path1)

    for name in files:
        count2 = 0
        with open(name) as f:
            for line in f:
                if line.startswith('_chemical_formula_sum'):
                    comp = line[23:-2]
                    for item in Multiple:
                        if item in comp:
                            name3.write(name[length:-4] + '  -  ' + comp + '\n')
                            count1 += 1
                            track.append(name)

                for item in Ln:
                    if item in line and '1_555 ' in line:
                        count2 += 1

                            
        if name in track and count2 != 0:
            shutil.copy(name, path1)
            
        if name not in track:
            name4.write(name[length:-4] + '  -  ' + comp + '\n')
            shutil.copy(name, path2)
            count += 1
            

    del Multiple[0]
    Multiple.append(Bank[0])
    del Bank[0]
                            

name3.close()
name4.close()

print (count)
print (count1)






    








    
