# Software designed to calculate closeness centrality
# of amino acid residues in a protein structure provided 
# by a pdb file. It is now intended for single or 
# multiple protein structures uses.
#
# Input: protein strucutre in pdb file
# Output: Closeness list in txt file
#         Event log in txt file
#
# python ProteinCloseness.py
# Insert file name:
# 4dc2_no_substrate
# Done Model
# Done LOL



import Point
import Graph
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

out = open((name + "_betweenness.txt"), "w")

text = open((name + ".pdb"), "r")

log = open((name + "_log.txt"), "w")

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
    out.write("TITLE " + title)
    out.write("MODEL" + str(model) + "\n")
    out.write("SIZE " + str(len(aminoList)) + "\n")

    #START THE CONTACT MATRIX
    graph = Graph.Graph(len(aminoList))
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
                    graph.addEdge(i, j)
                    flag = False
    bet = Graph.Betweenness(graph)
    betList = bet.getBet()
    for i in range(0, graph.size()):
        out.write(str(chainList[i]) + " - " + str(betList[i]) + "\n")


    if first:
        first = False
        #PRINT MISSING AMINOACIDS
        log.write("Warning: these amino acids were missing on the pdb file:\n")
        for i in range(1, chainList[-1]):
            if not isOnList(chainList, i):
                log.write(str(i) + "\n")
        log.write("--\n")
        #PRINT THE REST OF REPORT
        log.write("List of amino acids:\n")
        for i in range(0, len(chainList)):
            log.write(str(chainList[i])+" - "+nameList[i]+ "- No. of Atoms: "+ str(len(aminoList[i]))+"\n")


    print "Done Model " + str(model)
    #RESET EVERYTHING
    title = ""
    model = ""
    tag = ""
    aminoList = []
    atomList = []
    chainList = []
print "Done"