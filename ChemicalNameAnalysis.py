import glob
import shutil
from shutil import copyfile
import os
from itertools import islice

f_block = ['Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium',
           'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium',
           'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium']

searchpath = 'C:/Research/Crystal Database/Pop DataBase/Data/'
path1 = searchpath + 'Names.txt'
results = open(path1, "w")
count2 = 0

path = 'C:/Research/Crystal Database/Pop DataBase/Singles/*.CIF'
length = len(path[:-5])
files = glob.glob(path)
    
for name in files:
    count1 = 0
        
    with open(name) as f:
        itf = iter(f)
        name2 = ''
        for line in itf:
            if line.startswith('_chemical_name_systematic'):
                while count1 < 2:
                    name1 = next(itf)
                    if name1.startswith(';'):
                        count1 += 1
                    else:
                        name2 = name2 + name1.replace('\n', '')
            if line.startswith('_chemical_formula_sum '):
                name1 = line[23:-2]
                count = 0
                a = 0
                b = 3
                for i in range(len(name1)):
                    if name1[a:b].isdigit():
                        count += int(name1[a:b])
                        a += 3
                        b += 3
                    elif name1[a:b-1].isdigit():
                        count += int(name1[a:b-1])
                        a += 2
                        b += 2
                    elif name1[a:b-2].isdigit():
                        count += int(name1[a:b-2])
                        a += 1
                        b += 1
                    else:
                        a += 1
                        b += 1
                    
                
        results.write(name[length:-4]  + '  -  ' + name2 + '  -  ' + str(count) + '\n')
        count2 += 1



"""for item in f_block:
    print (item)
    path = 'C:/Research/Crystal Database/' + item + '/*.CIF'

    length = len(path[:-5])
    files = glob.glob(path)
    
    for name in files:
        count1 = 0
        
        with open(name) as f:
            itf = iter(f)
            name2 = ''
            for line in itf:
                if line.startswith('_chemical_name_systematic'):
                    while count1 < 2:
                        name1 = next(itf)
                        if name1.startswith(';'):
                            count1 += 1
                        else:
                            name2 = name2 + name1.replace('\n', '')
                    results.write(name[length:-4] + '  -  ' + name2 + '\n')
                    count2 += 1"""
                     
results.close()
print (count2) 



               

