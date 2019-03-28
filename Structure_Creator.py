import os
import numpy as np
import glob

One_Atom = ["F", "Cl", "Br", "I"]
Lanth = {"La" : 4.70000, "Nd" : 4.64000, "Eu" : 4.57000, "Dy" : 4.51000, "Tm" : 4.45000, "Lu" : 4.40000}
Mult_Atom = []
Core_List = []
LigandList = []
dir_path = os.path.dirname(os.path.realpath(__file__))

Cores = dir_path + '/Cores/*.xyz'
Ligands = dir_path + '/Ligands/*.xyz'

CoreLength = len(Cores[:-5])
Corefiles = glob.glob(Cores)

LigLength = len(Ligands[:-5])
Ligfiles = glob.glob(Ligands)

for name in Ligfiles:
    Mult_Atom.append(name[LigLength:-4])

for name in Corefiles:
    Core_List.append(name[CoreLength:-4])

LigandList = Mult_Atom + One_Atom

def Main(Core):

    Pos = [0,0,0]

    with open(Core) as  f:
        H_pos = []
        count = 0
        next(f)
        next(f)
        for line in f:

            count += 1
            line = line.replace("   ", " ")
            line = line.replace("  ", " ")
            line = line[:-1].split(' ')
            Pos[0] = line[2]
            Pos[1] = line[4]
            Pos[2] = line[6]

            if Pos[0] == Pos[2]:
                replace = count

    newpath = dir_path + '/NewStructures/Plain/' + str(Core[CoreLength:-4]) + '/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    for item in One_Atom:
        count = -1

        newpath_ = newpath + str(item) + '/'
        
        if not os.path.exists(newpath_):
            os.makedirs(newpath_)

        file1 = open(newpath_ + str(item) + '.xyz', "w")
        with open(Core) as f:
            for line in f:
                if count == replace:
                    line1 = line.replace("H", item)
                    file1.write(line1)
                else:
                    file1.write(line)

                count += 1

        file1.close()

    for item in Mult_Atom:

        newpath_ = newpath + str(item) + '/'
        if not os.path.exists(newpath_):
            os.makedirs(newpath_)
        
        Lig = open(dir_path + '/Ligands/' + str(item) + '.xyz', "r")
        New = open(newpath_ + str(item) +  '.xyz', "w")
        Core_ = open(Core, "r")
        NumAtom1 = int(next(Core_))
        NumAtom2 = int(next(Lig))
        NewAtom = NumAtom1 + NumAtom2 - 2

        next(Core_)
        next(Lig)
        New.write(str(NewAtom) + '\n' + str(item) + '\n')
        count = 0
    
        Pos    = [0,0,0]
        Pos1   = [0,0,0]
        NewPos = [0,0,0]

        for line in Core_:
            count += 1
            if count == replace:
                line = line.replace("   ", " ")
                line = line.replace("  ", " ")
                line = line[:-1].split(' ')
                Pos[0] = line[2]
                Pos[1] = line[4]
                Pos[2] = line[6]

                for line1 in Lig:
                    line2 = line1.replace("   ", " ")
                    line2 = line2.replace("  ", " ")
                    line2 = line2[:-1].split(' ')
                    Atom = line2[0]
                    Pos1[0] = line2[2]
                    Pos1[1] = line2[4]
                    Pos1[2] = line2[6]

                    if not Pos1[0] == Pos1[1] == Pos[2]:
                        New.write(line1)
                    

            else:
                New.write(line)

        Lig.close()
        New.close()
        Core_.close()

    return

for files in Corefiles:
    Main(files)

for Cores in Core_List:

    for item in LigandList:
        PlainFile = dir_path + '/NewStructures/Plain/' + str(Cores) + '/' + str(item) + '/' + str(item) + '.xyz'
        PlainPathLength = len(dir_path + '/NewStructures/Plain/' + str(Cores) + '/' + str(item) + '/')
        
        with open(PlainFile) as f:
            lines = f.readlines()
            lines[0]= str(int(lines[0]) + 1) + '\n'

            for k,v, in Lanth.items():
                NewPath = dir_path + '/NewStructures/' + str(k) + '/' + str(Cores) + '/' + str(item) + '/'

                if not os.path.exists(NewPath):
                    os.makedirs(NewPath)

                LanthFiles = open(str(NewPath) + str(PlainFile[PlainPathLength:]), "w")

                count = 0
                
                for items in lines:
                    count += 1
                    if count == 3:
                        LanthFiles.write(str(k) + '\t0.00000\t\t' + str(v) + '\t0.00000\n')
                    LanthFiles.write(str(items))


                














                




                
