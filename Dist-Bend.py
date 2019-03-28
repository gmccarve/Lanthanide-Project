import math
import os


path = os.path.dirname(os.path.realpath(__file__))

path1 = str(path) + '/orca.xyz'
path2 = path1

data = open(path + '/LA.txt', "w")
LA = path + '/Atoms.txt'

BtA = 0.529177249
AtP = BtA * 100

if path2.endswith('xyz'):
    with open(LA) as f:
        for line in f:
            Atom = line[:-1].split(' ')
            if len(Atom) == 2:
                Atom1 = Atom[0]
                Atom2 = Atom[1]

                with open(path1) as g:
                    count = -2
                    for line in g:
                        line = line.replace('    ', ' ')
                        line = line.replace('   ', ' ')
                        line = line.replace('  ', ' ')
                        count += 1
                        if str(count) == str(Atom1):
                            line1 = line[:-1].split(' ')
                            #print (line1)
                            #print (line1[])
                            d_x1 = float(line1[2])
                            d_y1 = float(line1[3])
                            d_z1 = float(line1[4])                            
                            #print (str(d_z1))
                            
                        if str(count) == str(Atom2):
                            line1 = line[:-1].split(' ')
                            #print (line1)
                            d_x2 = float(line1[2])
                            d_y2 = float(line1[3])
                            d_z2 = float(line1[4])
                            #print (str(d_z2))

                X = (d_x1 - d_x2)**2
                Y = (d_y1 - d_y2)**2
                Z = (d_z1 - d_z2)**2
                distance = ((X + Y + Z)**0.5)# * 100
                #data.write(str(Atom1) + ' ' + str(Atom2) + ' - ' + str(distance))
                data.write(str(distance))

            data.write('\n')
                
            if len(Atom) == 3:
                Atom1 = Atom[0]
                Atom2 = Atom[1]
                Atom3 = Atom[2]

                with open(path1) as g:
                    count = -2
                    for line in g:
                        line = line.replace('    ', ' ')
                        line = line.replace('   ', ' ')
                        line = line.replace('  ', ' ')
                        count += 1
                        if str(count) == str(Atom1):
                            line1 = line[:-1].split(' ')
                            d_x1 = float(line1[2])
                            d_y1 = float(line1[3])
                            d_z1 = float(line1[4])

                            #rint (str(count) + ' '  + str(d_z1))
                        if str(count) == str(Atom2):
                            line1 = line[:-1].split(' ')
                            #print (line1)
                            d_x2 = float(line1[2])
                            d_y2 = float(line1[3])
                            d_z2 = float(line1[4])

                            #print (str(count) + ' '  + str(d_z2))
                        if str(count) == str(Atom3):
                            line1 = line[:-1].split(' ')
                            d_x3 = float(line1[2])
                            d_y3 = float(line1[3])
                            d_z3 = float(line1[4])

                            #print (str(count) + ' '  + str(d_x3))

                            
                X12 = (d_x1 - d_x2)**2
                Y12 = (d_y1 - d_y2)**2
                Z12 = (d_z1 - d_z2)**2
                distance12 = ((X12 + Y12 + Z12)**0.5) * 100

                X23 = (d_x3 - d_x2)**2
                Y23 = (d_y3 - d_y2)**2
                Z23 = (d_z3 - d_z2)**2
                distance23 = ((X23 + Y23 + Z23)**0.5) * 100

                X13 = (d_x1 - d_x3)**2
                Y13 = (d_y1 - d_y3)**2
                Z13 = (d_z1 - d_z3)**2
                distance13 = ((X13 + Y13 + Z13)**0.5) * 100

                XYZ1 = distance12**2 + distance23**2 - distance13**2
                XYZ2 = 2 * distance12 * distance23
                XYZ = XYZ1/XYZ2
        
                bend = math.acos(XYZ)
                bend = bend * 57.2958
                #print (bend)
                #data.write(str(Atom1) + ' ' + str(Atom2) +  ' ' + str(Atom3) + ' - ' + str(bend))
                data.write(str(bend))
                 
    
            

"""if path2 == 'coord':
    with open(LA) as f:
        for line in f:
            Atom = line[:-1].split(' ')
            if len(Atom) == 2:
                Atom1 = Atom[0]
                Atom2 = Atom[1]
                
                with open(path1) as g:
                    count = -1
                    for line in g:
                        count += 1
                        if str(count) == str(Atom1):
                            d_x = float(line[0:-48])
                            d_y = float(line[-48:-25])
                            d_z = float(line[-25:-3])
                        
                        if str(count) == str(Atom2):
                            d_xn = float(line[0:-48])
                            d_yn = float(line[-48:-25])
                            d_zn = float(line[-25:-3])

                        
                X = (d_xn - d_x)**2
                Y = (d_yn - d_y)**2
                Z = (d_zn - d_z)**2
                distance = ((X + Y + Z)**0.5) * AtP
                #data.write(str(Atom1) + ' ' + str(Atom2) + ' - ' + str(distance))
                data.write(str(distance))
            
            data.write('\n')
            #data.write(' \n')
    
            if len(Atom) == 3:
                Atom = line[:-1].split(' ')
                Atom1 = Atom[0]
                Atom2 = Atom[1]
                Atom3 = Atom[2]
                
                with open(path1) as g:
                    count = -1
                    for line in g:
                        count += 1
                        if str(count) == str(Atom1):
                            d_x1 = float(line[0:-48])
                            d_y1 = float(line[-48:-25])
                            d_z1 = float(line[-25:-3])
                    
                        if str(count) == str(Atom2):
                            d_x2 = float(line[0:-48])
                            d_y2 = float(line[-48:-25])
                            d_z2 = float(line[-25:-3])

                        if str(count) == str(Atom3):
                            d_x3 = float(line[0:-48])
                            d_y3 = float(line[-48:-25])
                            d_z3 = float(line[-25:-3])                        

                        
                    X12 = (d_x1 - d_x2)**2
                    Y12 = (d_y1 - d_y2)**2
                    Z12 = (d_z1 - d_z2)**2
                    distance12 = ((X12 + Y12 + Z12)**0.5)
                    #print (distance12)

                    X13 = (d_x1 - d_x3)**2
                    Y13 = (d_y1 - d_y3)**2
                    Z13 = (d_z1 - d_z3)**2
                    distance13 = ((X13 + Y13 + Z13)**0.5)
                    #print (distance13)

                    X23 = (d_x3 - d_x2)**2
                    Y23 = (d_y3 - d_y2)**2
                    Z23 = (d_z3 - d_z2)**2
                    distance23 = ((X23 + Y23 + Z23)**0.5)
                    #print (distance23)

                    XYZ1 = distance12**2 + distance23**2 - distance13**2
                    XYZ2 = 2 * distance12 * distance23
                    XYZ = XYZ1/XYZ2
        
                    bend = math.acos(XYZ)
                    bend = bend * 57.2958
                    #print (bend)
                    #data.write(str(Atom1) + ' ' + str(Atom2) +  ' ' + str(Atom3) + ' - ' + str(bend))
                    data.write(str(bend))
                    #print (bend)   
                    """

data.close()


            
        




            
