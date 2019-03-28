import math
import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

Atoms = {'H ': 1, 'C ': 6, 'O ': 8, 'Br': 35, 'F ': 9}

dir_path = os.path.dirname(os.path.realpath(__file__))

#path = dir_path + '/*.xyz'
#files = glob.glob(path)


path = dir_path + '/test.xyz'

data = open(dir_path + '/test.txt', 'w')


with open(path) as f:
    size = next(f)
    skip = next(f)
    sz = 100
#    coul = np.zeros( (int(size),int(size)) )
#    Z_ij = np.zeros((int(size),1))
    coul = np.zeros((100,100))
    Z_ij = np.zeros((100,1))
    Pos = {}
    count = 0

    for line in f:
        element = line[0:2]
        keyy = 'Atom' + str(count)
        Z_ij[count] = Atoms[element]
                
        line = line.replace('   ', ' ')
        line = line.replace('  ', ' ')
        line1 = line[:-1].split(' ')

        Pos[keyy] = [float(line1[2]), float(line1[4]), float(line1[6])]

        count += 1
        
    for i in range(int(size)):
        for j in range(int(size)):
            Z_i = Z_ij[i]
            Z_j = Z_ij[j]

            if i == j:
                coul[i,i] = 0.5 * Z_i ** 2.4                

            else:
                X = (Pos['Atom' + str(i)][0] - Pos['Atom' + str(j)][0])**2
                Y = (Pos['Atom' + str(i)][1] - Pos['Atom' + str(j)][1])**2
                Z = (Pos['Atom' + str(i)][2] - Pos['Atom' + str(j)][2])**2
                dist = ((X + Y + Z)**0.5)

                coul[i,j] = (Z_i * Z_j) / dist           


    plt.matshow(coul,fignum=None)
    plt.show()

data.close()




    
