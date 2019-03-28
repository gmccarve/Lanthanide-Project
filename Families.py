import collections

f_block = ['lanthanum', 'cerium', 'praseodymium', 'neodymium', 'promethium',
           'samarium', 'europium', 'gadolinium', 'dysprosium',
           'holmium', 'thulium', 'ytterbium', 'lutetium', 'terbium', 'erbium',]

Ln = ['La1 ', 'Ce1 ', 'Pr1 ', 'Nd1 ', 'Pm1 ', 'Sm1 ', 'Eu1 ', 'Gd1 ', 'Tb1 ',
        'Dy1 ', 'Ho1 ', 'Er1 ', 'Tm1 ', 'Yb1 ', 'Lu1 ',]


searchpath = 'C:/Research/Crystal Database/Clean DataBase/Data/'
searchpath1 = 'C:/Research/Crystal Database/Clean DataBase/Singles/'
path1 = searchpath + 'Chemical Names.txt'
path2 = searchpath + 'Families1.txt'
path3 = searchpath + 'Results1.txt'

names = open(path1, 'r')
fam = open(path2, 'w')
fam1 = open(path3, 'w')

track = []
track1 = []
count = 0
count1 = 0


for line in names:
    if '(iii)' in line:
        line = line.replace('(iii)', '')
    count += 1
    line = line.lower()
    for item in f_block:
        if item in line:
            if 'catena' not in line:
                line1 = line.find(item)
                line2 = line[:line1]
                #line2 = line.replace(item, '')
                track.append(line2[11:])
                track1.append(line)

counter = collections.Counter(track)

for key, value in counter.items():
    if value > 1 :
        #fam.write(str(key[:-1]) + '\n')
        fam.write(str(key) + '\n')
        fam.write('>>>' + str(value) + '\n')
        count1 += 1
        
for item in track1:
    fam1.write(item)
    

#print (count)
print (count1)

names.close()
fam.close()
                    
                        
