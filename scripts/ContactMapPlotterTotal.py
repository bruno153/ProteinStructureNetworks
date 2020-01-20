# THIS SOFTWARE IS DESIGNED TO PLOT
# MULTIPLE CONTACT MAPS FROM MD
# SNAPSHOTS

import Point
import matplotlib.pyplot as plt
distLim = 5
aminomaxsize = 30

def isOnList(list, x):
    for i in list:
        if i == x:
            return True
    return False

#AQUIRE FILE NAME
print "Insert file name:"
name = raw_input()

text = open((name + ".pdb"), "r")
out = open((name + "_total.txt"), "w")

resseq = []
tag = ""
line = " "

title = ""
model = ""

aminoList = []
atomList = []

#present amino acid numbers list
chainList = []
nameList = []
first = True

finalMatrix=[]


while True:
    
    #FOR EVERY PROTEIN MODEL
    line = text.readline()
    #WHILE THE FILE HAS NOT ENDED
    if line == "":
        break

    while not(tag.find("TER") > -1):
        #AQUIRE TAG
        tag = line.split(" ")[0]
        #remove whitespace
        tag.replace("\n", "")
        
        #INTERPRET TAG
        if tag == "TITLE":
            title = line[10:]
        if tag == "MODEL":
            model = int(line[5:])
        if tag == "ATOM":
            aminoacidNumber = int(line[23:26])
            posX = float(line[31:38])
            posY = float(line[39:46])
            posZ = float(line[47:54])
            aminoacidName = str(line[17:20])
            #INITIALIZE THE AMINO ACID NUMBER LIST
            if len(chainList) == 0:
                chainList.append(aminoacidNumber)
                nameList.append(aminoacidName)
            #IF IT'S A DIFFERENT AMINO ACID, APPEND TO AMINOLIST
            if chainList[-1] != aminoacidNumber:
                aminoList.append(atomList)
                chainList.append(aminoacidNumber)
                nameList.append(aminoacidName)
                atomList = []
            atomList.append(Point.Point(posX, posY, posZ))
        line = text.readline()
    aminoList.append(atomList)
    #out.write("TITLE " + title)
    #out.write("MODEL" + str(model) + "\n")
    #out.write("SIZE " + str(len(aminoList)) + "\n")

    #START THE CONTACT MATRIX
    #graph = Graph.Graph(len(aminoList))

    contactmatrix = [[0 for i in range(len(aminoList))] for j in range(len(aminoList))]

    halt = False
    for i in range(0, len(aminoList)):
        for j in range(i, len(aminoList)):
            if i != j:
                flag = False
                for iAtom in aminoList[i]:
                    for jAtom in aminoList[j]:
                        dist = iAtom.distTo(jAtom)
                        if dist > aminomaxsize:
                            halt = True
                            break
                        if dist < distLim:
                            flag = True
                    if halt:
                        halt = False
                        break
                if flag:
                    #CONNECT THE TWO ON THE GRAPH
                    contactmatrix[i][j] = 1
                    contactmatrix[j][i] = 1
                    flag = False
            else:
            	contactmatrix[i][i] = 1
    #plt.imshow(contactmatrix, cmap='binary', interpolation='nearest')
    #plt.show()
    #plt.savefig(name+"_maps/"+str(model)+".png")
    if finalMatrix == []:
        finalMatrix = contactmatrix
    else:
        add = []
        #sum two matrices
        for i in range(len(finalMatrix)):
            line = []
            for j in range(len(finalMatrix)):
                line.append(finalMatrix[i][j]+contactmatrix[i][j])
            add.append(line)
        finalMatrix = add


        #finalMatrix += contactmatrix


    print "Done Model " + str(model)
    title = ""
    model = ""
    tag = ""
    aminoList = []
    atomList = []
    #plt.imshow(finalMatrix, cmap='rainbow', interpolation='nearest')
    #plt.colorbar()
    #plt.show()

for i in finalMatrix:
    for j in i:
        out.write(str(j)+" ")
    out.write("\n")
plt.imshow(finalMatrix, cmap='rainbow', interpolation='nearest')
plt.show()