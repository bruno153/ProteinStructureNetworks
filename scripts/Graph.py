'''
    PATCH: FEBRUARY 2017

    ADDED CLOSENESS CENTRALITY
	
	---------------------------
	PATCH: AUGUST 2017
	
	ADDED CONTACT MATRIX GENERATOR

    ---------------------------
    PATCH: SEPTEMBER 2018

    NOW contactList RETURN LIST CONTAINS
    -1 when i = j.

    FIXED isNextTo and addEDGE METHODS
    ACCEPTING VERTICES NOT CONTAINED WITHIN
    THE GRAPH V SET.
'''
from collections import deque
import error
import numpy as np
import random as rnd

class Graph:
    def __init__(self, V): #inicialization
        self._V = V
        self._E = 0
        self._nextTo = [[]]
        for i in range(0, V):
            self._nextTo.append([])

    def isNextTo(self, v, w): #checks if two edges are next to each other
        if not(v < self._V and w < self._V):
            error.err("Graph does not contain this edge.")
        for i in self._nextTo[v]:
            if i == w:
                return True
        return False


            
    def addEdge(self, i, j): #add a edge to the graph
        if not(self.isNextTo(i, j)):
            self._nextTo[i].append(j)
            self._nextTo[j].append(i)
            self._E += 1
    
    def showEdges(self): #prints the adjacency matrix
        print self._E
        for i in range(0, self._V):
            print self._nextTo[i]
    
    def adjList(self, v):
        return self._nextTo[v]

    def size(self):
        return self._V
    
    def adj(self, v):
        return self._nextTo[v]
		
    def contactList(self):
		contactMatrix = []
		tmpLine = []
		for i in range(self._V):
			for j in range(self._V):
				if i == j:
					tmpLine.append(-1)
				else:
				    if self.isNextTo(i, j):
					   tmpLine.append(1)
				    else:
					   tmpLine.append(0)
			contactMatrix.append(tmpLine)
			tmpLine = []
		return contactMatrix



class BFS:
    def __init__(self, G, S):
        self._G = G
        self._S = S
        self._marked = [False]*G.size()
        self._edgeTo = [0]*G.size()
        self._distTo = [-1]*G.size()
        queue = deque([S])
        self._distTo[S] = 0
        self._marked[S] = True
        
        while len(queue) > 0:
            v = queue.popleft()
            for j in self._G.adj(v):
                if not(self._marked[j]):
                    self._distTo[j] = self._distTo[v] + 1
                    self._edgeTo[j] = v
                    self._marked[j] = True
                    queue.append(j)
                    
        #print self._marked
    
    def distance(self, v):
        if self._distTo[v] == -1:
            error.err("Vertex " + str(v) + " is not connected")
        return self._distTo[v]

    def distanceList(self):
        return self._distTo
    
    def path(self, v):
        if self._distTo[v] == -1:
            error.err("Vertex " + str(v) + " is not connected")
        queue = deque([v])
        k = v
        while self._edgeTo[k] != self._S:
            k = self._edgeTo[k]
            queue.append(k)
        
        paths = []
        queue.reverse()
        paths.append(self._S)

        for i in queue:
            paths.append(i)
        return paths


# In[40]:

class Betweenness:
    def __init__(self, G):
        bet = [0]*G.size()
        for s in range(0, G.size()):
            S = deque()
            P = []
            for i in range(0, G.size()):
                P.append(deque())
            sig = [0]*G.size()
            d = [-1]*G.size()
            sig[s] = 1
            d[s] = 0
            Q = deque()
            Q.append(s)
            while len(Q) > 0:
                v = Q.popleft()
                S.append(v)
                for w in G.adj(v):
                    #fist time seen w
                    if d[w] < 0:
                        Q.append(w)
                        d[w] = d[v] + 1
                    if d[w] == d[v] + 1:
                        sig[w] = sig[w] + sig[v]
                        P[w].append(v)
            
            delt = [0]*G.size()
            #print sig
            while len(S) > 0:
                w = S.pop()
                for v in P[w]:
                    delt[v] = delt[v] + (((1.0*sig[v])/sig[w]) * (1 + delt[w]))
                if w != s:
                    bet[w] = bet[w]+delt[w]
        
        N = ((G.size() - 1) * (G.size() - 2))/2.0
        for i in range(0, len(bet)):
            bet[i] = (bet[i]/(2.0*N))
        self._bet = bet
    def getBet(self):
        return self._bet

class Closeness:
    def __init__(self, G):
        clo = [0]*G.size()
        for s in range(0, G.size()):
            bfs = BFS(G, s)
            dist = bfs.distanceList()
            clo[s] = 1.0/sum(dist)
        self._clo = clo

    def getClo(self):
        return self._clo

class Eigenvector:
    def __init__(self, G):
        adjMatrix = G.contactList()
        eigVector = np.random.rand(G.size())
        for i in range(100):
            tmp = np.dot(adjMatrix, eigVector)
            tmpnom = np.linalg.norm(tmp)
            eigVector = tmp/tmpnom
        self._eig = eigVector

    def getEig(self):
        return self._eig

class Degree:
    def __init__(self, G):
        self._deg = []
        for i in range(G.size()):
            self._deg.append(len(G.showEdges(i)))

    def getDeg(self):
        return self._deg

class RandomWalk:
    def __init__(self, G):
        self._state = 0
        self._G = G

    def walk(self):
        l = self._G.adjList(self._state)
        n = rnd.randint(0, len(l)-1)
        self._state = l[n]
        return l[n]

