import glob
import shutil
from shutil import copyfile
import os

f_block = ['lanthanum', 'cerium', 'praseodymium', 'neodymium', 'promethium',
           'samarium', 'europium', 'gadolinium', 'terbium', 'dysprosium',
           'holmium', 'erbium', 'thulium', 'ytterbium', 'lutetium']

Actinides = ['Ac', 'Th', 'Pa', ' U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No' , 'Lr']

D_block = [' Sc', ' Ti', ' V', ' Cr', ' Mn', ' Fe', ' Co', ' Ni', ' Cu', ' Zn',
           ' Y1', 'Y1', 'Y2', 'Y3', 'Y4', ' Zr', ' Nb', ' Mo', ' Tc', ' Ru', ' Rh', ' Pd', ' Ag', 'Cd',
           ' Hf', ' Ta', ' W', ' Re', ' Os', ' Ir', ' Pt', ' Au', ' Hg']

P_block = [' Si', ' Ga', ' Ge', ' As', ' Se', ' In',
           ' Sn', ' Sb', ' Te', ' Tl', ' Pb', ' Bi', ' Po', ' At', 'Al']

Mixed1 = [' Ce', ' Pr', ' Nd', ' Pm', ' Sm', ' Eu', ' Gd', ' Td',
          ' Dy', ' Ho', ' Er', ' Tm', ' Yb', ' Lu']

Mixed2 = [' La', ' Ce', ' Pr', ' Nd', ' Pm', ' Sm', ' Eu', ' Gd',
          ' Tb', ' Dy', ' Ho', ' Er', ' Tm', ' Yb', ' Lu']

Multiple = ['La1']

Bank = ['Ce1', 'Pr1', 'Nd1', 'Pm1', 'Sm1', 'Eu1', 'Gd1', 'Tb1',
        'Dy1', 'Ho1', 'Er1', 'Tm1', 'Yb1', 'Lu1', 'end']

Ln =    ['La1', 'Ce1', 'Pr1', 'Nd1', 'Pm1', 'Sm1', 'Eu1', 'Gd1',
         'Tb1', 'Dy1', 'Ho1', 'Er1', 'Tm1', 'Yb1', 'Lu1',]

searchpath = 'C:/Users/Gavin/Desktop/Research/Crystal DataBase/Full DataBase/'
Finalpath = 'C:/Users/Gavin/Desktop/Research/Crystal DataBase/Clean2/'
results1 = open(Finalpath + 'Actinides.txt', 'w')
results2 = open(Finalpath + 'D_block.txt', 'w')
results3 = open(Finalpath + 'P_block.txt', 'w')
results4 = open(Finalpath + 'Mixed.txt', 'w')
results5 = open(Finalpath + 'Multiples.txt', 'w')
results6 = open(Finalpath + 'Singles.txt', 'w')
results7 = open(Finalpath + 'Disordered.txt', 'w')
results8 = open(Finalpath + 'No Bonds.txt', 'w')
results9 = open(Finalpath + 'Cat_Clath.txt', 'w')

track  = []
track1 = []

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
counta = 0

for items in f_block:
    print (items)
    path = searchpath + items + '/*.CIF'
    path2 = Finalpath + 'Actinides/' + items + '/'
    path3 = Finalpath + 'Clean/' + items + '/'
    path4 = Finalpath + 'D_Block/' + items + '/'
    path5 = Finalpath + 'P_Block/' + items + '/'
    path6 = Finalpath + 'Mixed/' + items + '/'
    path7 = Finalpath + 'Multiples/' + items + '/'
    path8 = Finalpath + 'Disordered/' + items + '/'
    path9 = Finalpath + 'No Bonds/' + items + '/'
    patha = Finalpath + 'Cat_Clath/' + items + '/'
    
    length = len(path[:-5])
    files = glob.glob(path)

    if not os.path.exists(path2):
        os.makedirs(path2)
    if not os.path.exists(path3):
        os.makedirs(path3)
    if not os.path.exists(path4):
        os.makedirs(path4)
    if not os.path.exists(path5):
        os.makedirs(path5)
    if not os.path.exists(path6):
        os.makedirs(path6)
    if not os.path.exists(path7):
        os.makedirs(path7)
    if not os.path.exists(path8):
        os.makedirs(path8)
    if not os.path.exists(path9):
        os.makedirs(path9)        
    if not os.path.exists(patha):
        os.makedirs(patha)        

    for name in files:
        bonds = 0
        with open(name) as f:
            for line in f:
                if '? ' in line:
                    track1.append(name[length:-4])
                """for item in Ln:
                    if item in line and '1_555 ' in line:
                        bonds += 1"""
                if 'clathrate' in line or 'catena' in line:
                    counta += 1
                    results9.write(name[length:-4]+ '  ' + item + '  ' + line[22:-1] + '\n')
                    track.append(name[length:-4])
                    #shutil.copy(name, patha)
                if line.startswith('_chemical_formula_sum'):
                    form = line[22:-1] 
                    for item in Actinides:
                        if item in line:
                            count2 += 1
                            #shutil.copy(name, path2)
                            results1.write(name[length:-4]+ '  ' + item + '  ' + line[22:-1] + '\n')
                            track.append(name[length:-4])
                    for item in D_block:
                        if item in line:
                            count3 += 1
                            #shutil.copy(name, path4)
                            results2.write(name[length:-4]+ '  ' + item + '  ' + line[22:-1] + '\n')
                            track.append(name[length:-4])
                    for item in P_block:
                        if item in line:
                            count4 += 1
                            #shutil.copy(name, path5)
                            results3.write(name[length:-4]+ '  ' + item + '  ' + line[22:-1] + '\n')
                            track.append(name[length:-4])
                    for item in Mixed1:
                        if item in line:
                            count5 += 1
                            #shutil.copy(name, path6)
                            results4.write(name[length:-4]+ '  ' + item + '  ' + line[22:-1] + '\n')
                            track.append(name[length:-4])
                    for item in Multiple:
                        if item not in line:
                            count6 += 1
                            #shutil.copy(name, path7)
                            results5.write(name[length:-4]+ '  ' + item + '  ' + line[22:-1] + '\n')
                            track.append(name[length:-4])
                    

        if name[length:-4] in track1:
            results7.write(name[length:-4] + '\n')
            #shutil.copy(name, path8)
            count1 += 1
            track.append(name[length:-4])
        """if bonds == 0:
            results8.write(name[length:-4] + '\n')
            #shutil.copy(name, path9)
            count8 += 1
            track.append(name[length:-4])"""
        if name[length:-4] not in track:
            results6.write(name[length:-4] + '  ' + form + '\n')
            #shutil.copy(name, path3)
            count7 += 1
            
    del Mixed1[0]
    Mixed1.append(Mixed2[0])
    del Mixed2[0]

    del Multiple[0]
    Multiple.append(Bank[0])
    del Bank[0]
  

print('Disordered : ' + str(count1))
print('Actinides  : ' + str(count2))
print('D-Block    : ' + str(count3))
print('P-Block    : ' + str(count4))
print('Mixed      : ' + str(count5))
print('No Bonds   : ' + str(count8))
print('Multiple   : ' + str(count6))
print('Cat/Clath  : ' + str(counta))
print('Singles    : ' + str(count7))


results1.close()
results2.close()
results3.close()
results4.close()
results5.close()
results6.close()
results7.close()
results8.close()
results9.close()



    








    
